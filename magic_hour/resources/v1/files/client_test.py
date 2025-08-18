import pytest
import tempfile
import os
from unittest import mock

from magic_hour import AsyncClient, Client
from magic_hour.environment import Environment


def test_upload_file_local():
    data = b"test data"
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(data)
        tmp_path = tmp.name

    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    with mock.patch("httpx.Client.put") as mock_put:
        mock_put.return_value = mock.Mock(
            status_code=200, raise_for_status=lambda: None
        )
        result = client.v1.files.upload_file(tmp_path)
        assert result == "api-assets/id/video.mp4"
        mock_put.assert_called_once_with(
            mock.ANY,
            content=data,
            headers={"Content-Type": "application/octet-stream"},
        )

    os.remove(tmp_path)


def test_upload_file_url():
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    url = "https://example.com/file.mp4"
    with mock.patch("httpx.Client.put") as mock_put:
        mock_put.return_value = mock.Mock(
            status_code=200, raise_for_status=lambda: None
        )
        result = client.v1.files.upload_file(url)
        assert result == url
        mock_put.assert_not_called()


@pytest.mark.asyncio
async def test_async_upload_file_local():
    data = b"test data"
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(data)
        tmp_path = tmp.name

    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    with mock.patch("httpx.AsyncClient.put", new_callable=mock.AsyncMock) as mock_put:
        mock_put.return_value = mock.Mock(
            status_code=200, raise_for_status=lambda: None
        )
        result = await client.v1.files.upload_file(tmp_path)
        assert result == "api-assets/id/video.mp4"
        mock_put.assert_awaited_once_with(
            mock.ANY,
            content=data,
            headers={"Content-Type": "application/octet-stream"},
        )

    os.remove(tmp_path)


@pytest.mark.asyncio
async def test_async_upload_file_url():
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    url = "https://example.com/file.mp3"
    with mock.patch("httpx.Client.put") as mock_put:
        mock_put.return_value = mock.Mock(
            status_code=200, raise_for_status=lambda: None
        )
        result = await client.v1.files.upload_file(url)
        assert result == url
        mock_put.assert_not_called()
