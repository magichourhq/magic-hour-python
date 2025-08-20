import pytest
import tempfile
import os
import io
import pathlib
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
        mock_put.assert_called_once_with(url=mock.ANY, content=data)

    os.remove(tmp_path)


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
        mock_put.assert_awaited_once_with(url=mock.ANY, content=data)

    os.remove(tmp_path)


def test_upload_file_with_binary_io():
    data = b"test image data"
    file_obj = io.BytesIO(data)
    file_obj.name = "test.png"  # Required for extension detection

    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    with mock.patch("httpx.Client.put") as mock_put:
        mock_put.return_value = mock.Mock(
            status_code=200, raise_for_status=lambda: None
        )
        result = client.v1.files.upload_file(file_obj)
        assert result == "api-assets/id/video.mp4"
        mock_put.assert_called_once_with(
            url=mock.ANY,
            content=data,
        )


@pytest.mark.asyncio
async def test_async_upload_file_with_binary_io():
    data = b"test audio data"
    file_obj = io.BytesIO(data)
    file_obj.name = "test.wav"

    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    with mock.patch("httpx.AsyncClient.put", new_callable=mock.AsyncMock) as mock_put:
        mock_put.return_value = mock.Mock(
            status_code=200, raise_for_status=lambda: None
        )
        result = await client.v1.files.upload_file(file_obj)
        assert result == "api-assets/id/video.mp4"
        mock_put.assert_awaited_once_with(url=mock.ANY, content=data)


# Test pathlib.Path input
def test_upload_file_with_pathlib_path():
    data = b"test data"
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(data)
        tmp_path = pathlib.Path(tmp.name)

    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    with mock.patch("httpx.Client.put") as mock_put:
        mock_put.return_value = mock.Mock(
            status_code=200, raise_for_status=lambda: None
        )
        result = client.v1.files.upload_file(tmp_path)
        assert result == "api-assets/id/video.mp4"
        mock_put.assert_called_once_with(url=mock.ANY, content=data)

    os.remove(tmp_path)


# Test error cases
def test_upload_file_nonexistent_file():
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    with pytest.raises(
        FileNotFoundError, match="File not found: /nonexistent/file.mp4"
    ):
        client.v1.files.upload_file("/nonexistent/file.mp4")


def test_upload_file_unsupported_file_type():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
        tmp.write(b"test data")
        tmp_path = tmp.name

    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    with pytest.raises(ValueError, match="Could not determine file type"):
        client.v1.files.upload_file(tmp_path)

    os.remove(tmp_path)


def test_upload_file_binary_io_without_name():
    data = b"test data"
    file_obj = io.BytesIO(data)
    # Intentionally not setting name attribute

    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    with pytest.raises(
        ValueError, match="File-like object must have a 'name' attribute"
    ):
        client.v1.files.upload_file(file_obj)


def test_upload_file_binary_io_with_non_string_name():
    data = b"test data"
    file_obj = io.BytesIO(data)
    file_obj.name = 123  # Non-string name

    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    with pytest.raises(
        ValueError, match="File-like object must have a 'name' attribute of type str"
    ):
        client.v1.files.upload_file(file_obj)


def test_upload_file_no_upload_url_returned():
    data = b"test data"
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(data)
        tmp_path = tmp.name

    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    # Mock the upload_urls.create to return empty items
    with mock.patch.object(client.v1.files.upload_urls, "create") as mock_create:
        mock_create.return_value = mock.Mock(items=[])

        with pytest.raises(
            ValueError, match="No upload URL was returned from the server"
        ):
            client.v1.files.upload_file(tmp_path)

    os.remove(tmp_path)


def test_upload_file_http_error():
    data = b"test data"
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(data)
        tmp_path = tmp.name

    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    with mock.patch("httpx.Client.put") as mock_put:
        # Mock HTTP error response
        mock_response = mock.Mock()
        mock_response.raise_for_status.side_effect = Exception("Upload failed")
        mock_put.return_value = mock_response

        with pytest.raises(Exception, match="Upload failed"):
            client.v1.files.upload_file(tmp_path)

    os.remove(tmp_path)


# Test different file types to ensure proper type detection
def test_upload_different_file_types():
    test_cases = [
        (".mp4", "video"),
        (".mov", "video"),
        (".webm", "video"),
        (".mp3", "audio"),
        (".wav", "audio"),
        (".png", "image"),
        (".jpg", "image"),
        (".jpeg", "image"),
    ]

    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    for extension, expected_type in test_cases:
        data = b"test data"
        with tempfile.NamedTemporaryFile(delete=False, suffix=extension) as tmp:
            tmp.write(data)
            tmp_path = tmp.name

        with mock.patch("httpx.Client.put") as mock_put:
            mock_put.return_value = mock.Mock(
                status_code=200, raise_for_status=lambda: None
            )

            # Mock the upload_urls.create to verify correct type is passed
            with mock.patch.object(
                client.v1.files.upload_urls, "create"
            ) as mock_create:
                mock_create.return_value = mock.Mock(
                    items=[
                        mock.Mock(
                            upload_url="https://test.com/upload",
                            file_path="api-assets/id/video.mp4",
                        )
                    ]
                )

                result = client.v1.files.upload_file(tmp_path)
                assert result == "api-assets/id/video.mp4"

                # Verify the correct type and extension were passed
                call_args = mock_create.call_args
                items = call_args.kwargs["items"]
                assert len(items) == 1
                assert items[0]["type_"] == expected_type
                assert items[0]["extension"] == extension[1:]  # without the dot

        os.remove(tmp_path)


# Test URL handling - should skip upload and return URL as is
def test_upload_file_with_http_url():
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    http_url = "http://example.com/image.jpg"
    result = client.v1.files.upload_file(http_url)

    assert result == http_url


def test_upload_file_with_https_url():
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    https_url = "https://example.com/video.mp4"
    result = client.v1.files.upload_file(https_url)

    assert result == https_url


@pytest.mark.asyncio
async def test_async_upload_file_with_http_url():
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    http_url = "http://example.com/audio.mp3"
    result = await client.v1.files.upload_file(http_url)

    assert result == http_url


@pytest.mark.asyncio
async def test_async_upload_file_with_https_url():
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    https_url = "https://example.com/document.pdf"
    result = await client.v1.files.upload_file(https_url)

    assert result == https_url


# Test blob path handling - should skip upload and return blob path as is
def test_upload_file_with_blob_path():
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    blob_path = "api-assets/user123/image.jpg"
    result = client.v1.files.upload_file(blob_path)

    assert result == blob_path


def test_upload_file_with_blob_path_different_format():
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    blob_path = "api-assets/project456/video.mp4"
    result = client.v1.files.upload_file(blob_path)

    assert result == blob_path


@pytest.mark.asyncio
async def test_async_upload_file_with_blob_path():
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    blob_path = "api-assets/user789/audio.wav"
    result = await client.v1.files.upload_file(blob_path)

    assert result == blob_path


@pytest.mark.asyncio
async def test_async_upload_file_with_blob_path_different_format():
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    blob_path = "api-assets/session101/photo.png"
    result = await client.v1.files.upload_file(blob_path)

    assert result == blob_path


# Test that URL and blob path handling doesn't make HTTP requests
def test_upload_file_with_url_does_not_make_http_requests():
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    with mock.patch("httpx.Client.put") as mock_put:
        with mock.patch.object(client.v1.files.upload_urls, "create") as mock_create:
            result = client.v1.files.upload_file("https://example.com/file.jpg")

            # Should not call upload_urls.create or make HTTP PUT request
            mock_create.assert_not_called()
            mock_put.assert_not_called()

            assert result == "https://example.com/file.jpg"


def test_upload_file_with_blob_path_does_not_make_http_requests():
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    with mock.patch("httpx.Client.put") as mock_put:
        with mock.patch.object(client.v1.files.upload_urls, "create") as mock_create:
            result = client.v1.files.upload_file("api-assets/user123/file.mp4")

            # Should not call upload_urls.create or make HTTP PUT request
            mock_create.assert_not_called()
            mock_put.assert_not_called()

            assert result == "api-assets/user123/file.mp4"


@pytest.mark.asyncio
async def test_async_upload_file_with_url_does_not_make_http_requests():
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    with mock.patch("httpx.AsyncClient.put", new_callable=mock.AsyncMock) as mock_put:
        with mock.patch.object(
            client.v1.files.upload_urls, "create", new_callable=mock.AsyncMock
        ) as mock_create:
            result = await client.v1.files.upload_file("http://example.com/file.mp3")

            # Should not call upload_urls.create or make HTTP PUT request
            mock_create.assert_not_awaited()
            mock_put.assert_not_awaited()

            assert result == "http://example.com/file.mp3"


@pytest.mark.asyncio
async def test_async_upload_file_with_blob_path_does_not_make_http_requests():
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    with mock.patch("httpx.AsyncClient.put", new_callable=mock.AsyncMock) as mock_put:
        with mock.patch.object(
            client.v1.files.upload_urls, "create", new_callable=mock.AsyncMock
        ) as mock_create:
            result = await client.v1.files.upload_file("api-assets/user456/file.wav")

            # Should not call upload_urls.create or make HTTP PUT request
            mock_create.assert_not_awaited()
            mock_put.assert_not_awaited()

            assert result == "api-assets/user456/file.wav"


# Test file position preservation for file-like objects
def test_upload_file_preserves_file_position():
    data = b"test data for position preservation"
    file_obj = io.BytesIO(data)
    file_obj.name = "test.mp4"

    # Move to middle of file
    file_obj.seek(5)
    original_position = file_obj.tell()

    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)

    with mock.patch("httpx.Client.put") as mock_put:
        mock_put.return_value = mock.Mock(
            status_code=200, raise_for_status=lambda: None
        )
        client.v1.files.upload_file(file_obj)

        # Verify position was restored
        assert file_obj.tell() == original_position

        # Verify the full content was uploaded (not just from position 5)
        mock_put.assert_called_once_with(
            url=mock.ANY,
            content=data,  # Full data, not data[5:]
        )
