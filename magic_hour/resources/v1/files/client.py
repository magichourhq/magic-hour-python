import typing_extensions
from magic_hour.core import AsyncBaseClient, SyncBaseClient
from magic_hour.resources.v1.files.upload_urls import (
    AsyncUploadUrlsClient,
    UploadUrlsClient,
)
import os
import mimetypes
import httpx
from pathlib import Path


def _get_file_type_and_extension(file_path: str):
    """Determine file type and extension from file path.

    Args:
        file_path: Path to the file

    Returns:
        Tuple of (file_type, extension) where file_type is one of "video", "audio", or "image"
        and extension is the lowercase file extension without the dot
    """
    ext = Path(file_path).suffix.lower()
    if ext.startswith("."):
        ext = ext[1:]  # Remove the leading dot

    file_type: typing_extensions.Literal["audio", "image", "video"] | None = None
    mime, _ = mimetypes.guess_type(file_path)
    if mime:
        if mime.startswith("video/"):
            file_type = "video"
        elif mime.startswith("audio/"):
            file_type = "audio"
        elif mime.startswith("image/"):
            file_type = "image"

    if not file_type:
        raise ValueError(
            f"Could not determine file type for {file_path}. "
            "Supported types: video (mp4, m4v, mov, webm), "
            "audio (mp3, mpeg, wav, aac, aiff, flac), "
            "image (png, jpg, jpeg, webp, avif, jp2, tiff, bmp)"
        )

    return file_type, ext


class FilesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.upload_urls = UploadUrlsClient(base_client=self._base_client)

    def upload_file(self, local_file_path: str) -> str:
        """Upload a file to Magic Hour's storage or return the path if it's already a URL.

        Args:
            local_file_path: Path to the local file to upload or a URL

        Returns:
            The file path that can be used in other API calls. If the input is a URL,
            it will be returned as-is.

        Raises:
            FileNotFoundError: If the local file is not found
            ValueError: If the file type is not supported
            httpx.HTTPStatusError: If the upload fails
        """
        # If the input is already a URL, return it as-is
        if local_file_path.startswith(("http://", "https://")):
            return local_file_path

        if not os.path.isfile(local_file_path):
            raise FileNotFoundError(f"File not found: {local_file_path}")

        file_type, extension = _get_file_type_and_extension(local_file_path)
        response = self.upload_urls.create(
            items=[{"extension": extension, "type_": file_type}]
        )

        if not response.items:
            raise ValueError("No upload URL was returned from the server")

        upload_info = response.items[0]

        with open(local_file_path, "rb") as f:
            headers = {"Content-Type": "application/octet-stream"}
            with httpx.Client() as client:
                response = client.put(
                    upload_info.upload_url, content=f.read(), headers=headers
                )
                response.raise_for_status()

        return upload_info.file_path


class AsyncFilesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.upload_urls = AsyncUploadUrlsClient(base_client=self._base_client)

    async def upload_file(self, local_path_or_url: str) -> str:
        """Upload a file to Magic Hour's storage asynchronously or return the path if it's already a URL.

        Args:
            local_path_or_url: Path to the local file to upload or a URL

        Returns:
            The file path that can be used in other API calls. If the input is a URL,
            it will be returned as-is.

        Raises:
            FileNotFoundError: If the local file is not found
            ValueError: If the file type is not supported
            httpx.HTTPStatusError: If the upload fails
        """
        # If the input is already a URL, return it as-is
        if local_path_or_url.startswith(("http://", "https://")):
            return local_path_or_url

        if not os.path.isfile(local_path_or_url):
            raise FileNotFoundError(f"File not found: {local_path_or_url}")

        file_type, extension = _get_file_type_and_extension(local_path_or_url)
        response = await self.upload_urls.create(
            items=[{"extension": extension, "type_": file_type}]
        )

        if not response.items:
            raise ValueError("No upload URL was returned from the server")

        upload_info = response.items[0]

        async with httpx.AsyncClient() as client:
            with open(local_path_or_url, "rb") as f:
                headers = {"Content-Type": "application/octet-stream"}
                response = await client.put(
                    upload_info.upload_url, content=f.read(), headers=headers
                )
                response.raise_for_status()

        return upload_info.file_path
