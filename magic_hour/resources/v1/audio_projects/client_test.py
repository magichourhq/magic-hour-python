import datetime
import pytest
import httpx
from pathlib import Path
from typing import Any, Generator, Literal, Union, List
from unittest.mock import Mock, AsyncMock

from magic_hour.types import models
from magic_hour.resources.v1.audio_projects.client import (
    AudioProjectsClient,
    AsyncAudioProjectsClient,
)


class DummyResponse(models.V1AudioProjectsGetResponse):
    """Helper response with defaults"""

    def __init__(
        self,
        *,
        status: Literal[
            "complete", "queued", "rendering", "error", "canceled"
        ] = "complete",
        download_url: Union[str, None] = None,
        error: Union[str, None] = None,
    ):
        # Create error object if error string is provided
        error_obj = None
        if error:
            error_obj = models.V1AudioProjectsGetResponseError(
                code="TEST_ERROR", message=error
            )

        super().__init__(
            id="test-id",
            created_at=datetime.datetime.now().isoformat(),
            credits_charged=0,
            downloads=[
                models.V1AudioProjectsGetResponseDownloadsItem(
                    url=download_url, expires_at="2024-01-01T00:00:00Z"
                )
            ]
            if download_url
            else [],
            enabled=True,
            error=error_obj,
            name="test-name",
            status=status,
            type="test-type",
        )


@pytest.fixture
def mock_base_client() -> Generator[Mock, None, None]:
    yield Mock()


@pytest.fixture
def mock_async_base_client() -> Generator[AsyncMock, None, None]:
    yield AsyncMock()


def test_delete_calls_base_client(mock_base_client: Mock) -> None:
    client = AudioProjectsClient(base_client=mock_base_client)
    client.delete(id="123")

    mock_base_client.request.assert_called_once()
    call = mock_base_client.request.call_args[1]
    assert call["method"] == "DELETE"
    assert "/v1/audio-projects/123" in call["path"]


def test_get_calls_base_client(mock_base_client: Mock) -> None:
    client = AudioProjectsClient(base_client=mock_base_client)
    mock_base_client.request.return_value = DummyResponse()

    resp = client.get(id="abc")

    mock_base_client.request.assert_called_once()
    assert isinstance(resp, models.V1AudioProjectsGetResponse)
    assert resp.id == "test-id"


def test_check_result_no_wait_no_download(mock_base_client: Mock) -> None:
    client = AudioProjectsClient(base_client=mock_base_client)
    mock_base_client.request.return_value = DummyResponse(status="queued")

    resp = client.check_result(
        id="xyz",
        wait_for_completion=False,
        download_outputs=False,
    )

    assert resp.downloaded_paths is None


def test_check_result_wait_until_complete(
    monkeypatch: Any, mock_base_client: Mock
) -> None:
    client = AudioProjectsClient(base_client=mock_base_client)

    # First calls return queued, then complete
    mock_base_client.request.side_effect = [
        DummyResponse(status="queued"),
        DummyResponse(status="queued"),
        DummyResponse(status="complete"),
    ]

    monkeypatch.setattr("time.sleep", lambda _: None)  # type: ignore

    resp = client.check_result(
        id="xyz", wait_for_completion=True, download_outputs=False
    )

    assert resp.status == "complete"
    assert resp.downloaded_paths is None


def test_check_result_download_outputs(
    tmp_path: Path, mock_base_client: Mock, monkeypatch: Any
) -> None:
    client = AudioProjectsClient(base_client=mock_base_client)

    file_url = "https://example.com/file.mp3"
    mock_base_client.request.return_value = DummyResponse(
        status="complete",
        download_url=file_url,
    )

    # Create a mock response for httpx
    mock_request = httpx.Request("GET", "https://example.com/file.mp3")
    mock_response = httpx.Response(200, content=b"fake mp3", request=mock_request)

    # Mock the httpx.Client class
    class MockClient:
        def __init__(self):
            pass

        def __enter__(self) -> "MockClient":
            return self

        def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
            pass

        def get(self, url: str) -> httpx.Response:
            return mock_response

    monkeypatch.setattr(httpx, "Client", MockClient)

    resp = client.check_result(
        id="xyz",
        wait_for_completion=True,
        download_outputs=True,
        download_directory=str(tmp_path),
    )

    assert resp.status == "complete"
    assert resp.downloaded_paths
    saved_file = Path(resp.downloaded_paths[0])
    assert saved_file.exists()
    assert saved_file.read_bytes() == b"fake mp3"


def test_check_result_error_status(mock_base_client: Mock) -> None:
    client = AudioProjectsClient(base_client=mock_base_client)
    mock_base_client.request.return_value = DummyResponse(status="error", error="Boom!")

    resp = client.check_result(
        id="err", wait_for_completion=True, download_outputs=False
    )
    assert resp.status == "error"
    assert resp.error is not None
    assert resp.error.message == "Boom!"
    assert resp.downloaded_paths is None


def test_check_result_canceled_status(mock_base_client: Mock) -> None:
    client = AudioProjectsClient(base_client=mock_base_client)
    mock_base_client.request.return_value = DummyResponse(status="canceled")

    resp = client.check_result(
        id="cancel", wait_for_completion=True, download_outputs=False
    )
    assert resp.status == "canceled"
    assert resp.downloaded_paths is None


def test_check_result_poll_interval_default(
    mock_base_client: Mock, monkeypatch: Any
) -> None:
    client = AudioProjectsClient(base_client=mock_base_client)

    # First calls return queued, then complete
    mock_base_client.request.side_effect = [
        DummyResponse(status="queued"),
        DummyResponse(status="complete"),
    ]

    # Mock time.sleep to track calls
    sleep_calls: List[float] = []

    def mock_sleep(seconds: float) -> None:
        sleep_calls.append(seconds)

    monkeypatch.setattr("time.sleep", mock_sleep)

    resp = client.check_result(
        id="xyz", wait_for_completion=True, download_outputs=False
    )

    assert resp.status == "complete"
    # Should have slept once with default interval (0.5)
    assert len(sleep_calls) == 1
    assert sleep_calls[0] == 0.5


def test_check_result_poll_interval_custom(
    mock_base_client: Mock, monkeypatch: Any
) -> None:
    client = AudioProjectsClient(base_client=mock_base_client)

    # Set custom poll interval
    monkeypatch.setenv("MAGIC_HOUR_POLL_INTERVAL", "1.0")

    # First calls return queued, then complete
    mock_base_client.request.side_effect = [
        DummyResponse(status="queued"),
        DummyResponse(status="complete"),
    ]

    # Mock time.sleep to track calls
    sleep_calls: List[float] = []

    def mock_sleep(seconds: float) -> None:
        sleep_calls.append(seconds)

    monkeypatch.setattr("time.sleep", mock_sleep)

    resp = client.check_result(
        id="xyz", wait_for_completion=True, download_outputs=False
    )

    assert resp.status == "complete"
    # Should have slept once with custom interval (1.0)
    assert len(sleep_calls) == 1
    assert sleep_calls[0] == 1.0


def test_check_result_poll_interval_multiple_polls(
    mock_base_client: Mock, monkeypatch: Any
) -> None:
    client = AudioProjectsClient(base_client=mock_base_client)

    # Set custom poll interval
    monkeypatch.setenv("MAGIC_HOUR_POLL_INTERVAL", "0.1")

    # Multiple calls return queued before complete
    mock_base_client.request.side_effect = [
        DummyResponse(status="queued"),
        DummyResponse(status="queued"),
        DummyResponse(status="queued"),
        DummyResponse(status="complete"),
    ]

    # Mock time.sleep to track calls
    sleep_calls: List[float] = []

    def mock_sleep(seconds: float) -> None:
        sleep_calls.append(seconds)

    monkeypatch.setattr("time.sleep", mock_sleep)

    resp = client.check_result(
        id="xyz", wait_for_completion=True, download_outputs=False
    )

    assert resp.status == "complete"
    # Should have slept 3 times with custom interval (0.1)
    assert len(sleep_calls) == 3
    assert all(sleep_time == 0.1 for sleep_time in sleep_calls)


@pytest.mark.asyncio
async def test_async_delete_calls_base_client(
    mock_async_base_client: AsyncMock,
) -> None:
    client = AsyncAudioProjectsClient(base_client=mock_async_base_client)
    await client.delete(id="456")

    mock_async_base_client.request.assert_called_once()
    call = mock_async_base_client.request.call_args[1]
    assert call["method"] == "DELETE"
    assert "/v1/audio-projects/456" in call["path"]


@pytest.mark.asyncio
async def test_async_get_calls_base_client(mock_async_base_client: AsyncMock) -> None:
    client = AsyncAudioProjectsClient(base_client=mock_async_base_client)
    mock_async_base_client.request.return_value = DummyResponse()

    resp = await client.get(id="zzz")

    mock_async_base_client.request.assert_called_once()
    assert isinstance(resp, models.V1AudioProjectsGetResponse)
    assert resp.id == "test-id"


@pytest.mark.asyncio
async def test_async_check_result_no_wait_no_download(
    mock_async_base_client: AsyncMock,
) -> None:
    client = AsyncAudioProjectsClient(base_client=mock_async_base_client)
    mock_async_base_client.request.return_value = DummyResponse(status="queued")

    resp = await client.check_result(
        id="xyz",
        wait_for_completion=False,
        download_outputs=False,
    )

    assert resp.downloaded_paths is None


@pytest.mark.asyncio
async def test_async_check_result_wait_until_complete(
    mock_async_base_client: AsyncMock, monkeypatch: Any
) -> None:
    client = AsyncAudioProjectsClient(base_client=mock_async_base_client)

    # First calls return queued, then complete
    mock_async_base_client.request.side_effect = [
        DummyResponse(status="queued"),
        DummyResponse(status="queued"),
        DummyResponse(status="complete"),
    ]

    monkeypatch.setattr("time.sleep", lambda _: None)  # type: ignore

    resp = await client.check_result(
        id="xyz", wait_for_completion=True, download_outputs=False
    )

    assert resp.status == "complete"
    assert resp.downloaded_paths is None


@pytest.mark.asyncio
async def test_async_check_result_download_outputs(
    tmp_path: Path, mock_async_base_client: AsyncMock, monkeypatch: Any
) -> None:
    client = AsyncAudioProjectsClient(base_client=mock_async_base_client)

    file_url = "https://example.com/file.mp3"
    mock_async_base_client.request.return_value = DummyResponse(
        status="complete",
        download_url=file_url,
    )

    # Create a mock response for httpx
    mock_request = httpx.Request("GET", "https://example.com/file.mp3")
    mock_response = httpx.Response(200, content=b"fake mp3", request=mock_request)

    # Mock the httpx.AsyncClient class
    class MockAsyncClient:
        def __init__(self):
            pass

        async def __aenter__(self) -> "MockAsyncClient":
            return self

        async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
            pass

        async def get(self, url: str) -> httpx.Response:
            return mock_response

    monkeypatch.setattr(httpx, "AsyncClient", MockAsyncClient)

    resp = await client.check_result(
        id="xyz",
        wait_for_completion=True,
        download_outputs=True,
        download_directory=str(tmp_path),
    )

    assert resp.status == "complete"
    assert resp.downloaded_paths
    saved_file = Path(resp.downloaded_paths[0])
    assert saved_file.exists()
    assert saved_file.read_bytes() == b"fake mp3"


@pytest.mark.asyncio
async def test_async_check_result_error_status(
    mock_async_base_client: AsyncMock,
) -> None:
    client = AsyncAudioProjectsClient(base_client=mock_async_base_client)
    mock_async_base_client.request.return_value = DummyResponse(
        status="error", error="Boom!"
    )

    resp = await client.check_result(
        id="err", wait_for_completion=True, download_outputs=False
    )
    assert resp.status == "error"
    assert resp.error is not None
    assert resp.error.message == "Boom!"
    assert resp.downloaded_paths is None


@pytest.mark.asyncio
async def test_async_check_result_canceled_status(
    mock_async_base_client: AsyncMock,
) -> None:
    client = AsyncAudioProjectsClient(base_client=mock_async_base_client)
    mock_async_base_client.request.return_value = DummyResponse(status="canceled")

    resp = await client.check_result(
        id="cancel", wait_for_completion=True, download_outputs=False
    )
    assert resp.status == "canceled"
    assert resp.downloaded_paths is None


@pytest.mark.asyncio
async def test_async_check_result_poll_interval_default(
    mock_async_base_client: AsyncMock, monkeypatch: Any
) -> None:
    client = AsyncAudioProjectsClient(base_client=mock_async_base_client)

    # First calls return queued, then complete
    mock_async_base_client.request.side_effect = [
        DummyResponse(status="queued"),
        DummyResponse(status="complete"),
    ]

    # Mock time.sleep to track calls
    sleep_calls: List[float] = []

    def mock_sleep(seconds: float) -> None:
        sleep_calls.append(seconds)

    monkeypatch.setattr("time.sleep", mock_sleep)

    resp = await client.check_result(
        id="xyz", wait_for_completion=True, download_outputs=False
    )

    assert resp.status == "complete"
    # Should have slept once with default interval (0.5)
    assert len(sleep_calls) == 1
    assert sleep_calls[0] == 0.5


@pytest.mark.asyncio
async def test_async_check_result_poll_interval_custom(
    mock_async_base_client: AsyncMock, monkeypatch: Any
) -> None:
    client = AsyncAudioProjectsClient(base_client=mock_async_base_client)

    # Set custom poll interval
    monkeypatch.setenv("MAGIC_HOUR_POLL_INTERVAL", "2.0")

    # First calls return queued, then complete
    mock_async_base_client.request.side_effect = [
        DummyResponse(status="queued"),
        DummyResponse(status="complete"),
    ]

    # Mock time.sleep to track calls
    sleep_calls: List[float] = []

    def mock_sleep(seconds: float) -> None:
        sleep_calls.append(seconds)

    monkeypatch.setattr("time.sleep", mock_sleep)

    resp = await client.check_result(
        id="xyz", wait_for_completion=True, download_outputs=False
    )

    assert resp.status == "complete"
    # Should have slept once with custom interval (2.0)
    assert len(sleep_calls) == 1
    assert sleep_calls[0] == 2.0


@pytest.mark.asyncio
async def test_async_check_result_poll_interval_multiple_polls(
    mock_async_base_client: AsyncMock, monkeypatch: Any
) -> None:
    client = AsyncAudioProjectsClient(base_client=mock_async_base_client)

    # Set custom poll interval
    monkeypatch.setenv("MAGIC_HOUR_POLL_INTERVAL", "0.3")

    # Multiple calls return queued before complete
    mock_async_base_client.request.side_effect = [
        DummyResponse(status="queued"),
        DummyResponse(status="queued"),
        DummyResponse(status="queued"),
        DummyResponse(status="complete"),
    ]

    # Mock time.sleep to track calls
    sleep_calls: List[float] = []

    def mock_sleep(seconds: float) -> None:
        sleep_calls.append(seconds)

    monkeypatch.setattr("time.sleep", mock_sleep)

    resp = await client.check_result(
        id="xyz", wait_for_completion=True, download_outputs=False
    )

    assert resp.status == "complete"
    # Should have slept 3 times with custom interval (0.3)
    assert len(sleep_calls) == 3
    assert all(sleep_time == 0.3 for sleep_time in sleep_calls)
