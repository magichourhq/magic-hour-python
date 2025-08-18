from magic_hour.core import AsyncBaseClient, SyncBaseClient
from magic_hour.resources.v1.files.upload_urls import (
    AsyncUploadUrlsClient,
    UploadUrlsClient,
)
from magic_hour.types.params.v1_files_upload_urls_create_body_items_item import (
    V1FilesUploadUrlsCreateBodyItemsItem,
)
import typing_extensions
import os
import mimetypes
import httpx
from pathlib import Path
import typing
import io
import pathlib


def _get_file_type_and_extension(file_path: str):
    """
    Determine file type and extension from file path.

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


def _process_file_input(
    file: typing.Union[str, pathlib.Path, typing.BinaryIO, io.IOBase],
) -> tuple[
    str | None,
    typing.BinaryIO | io.IOBase | None,
    typing_extensions.Literal["audio", "image", "video"],
    str,
]:
    """
    Process different file input types and return standardized information.

    Args:
        file: Path to the local file to upload, a URL, or a file-like object

    Returns:
        Tuple of (file_path, file_to_upload, file_type, extension)

    Raises:
        FileNotFoundError: If the local file is not found
        ValueError: If the file type is not supported or file-like object is invalid
    """
    # If the input is already a URL, return it as-is
    if isinstance(file, str) and file.startswith(("http://", "https://")):
        raise ValueError("URL input should be handled separately")

    # Accept pathlib.Path and file-like objects
    if isinstance(file, pathlib.Path):
        file_path = str(file)
        file_to_upload = None
    elif isinstance(file, (io.IOBase, typing.BinaryIO)):
        file_path = None
        file_to_upload = file
    else:
        file_path = file
        file_to_upload = None

    if file_path is not None:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        file_type, extension = _get_file_type_and_extension(file_path)
    else:
        if file_to_upload is None:
            raise ValueError("file_to_upload is None for file-like object case.")
        file_name = getattr(file_to_upload, "name", None)
        if not isinstance(file_name, str):
            raise ValueError(
                "File-like object must have a 'name' attribute of type str for extension detection."
            )
        file_type, extension = _get_file_type_and_extension(file_name)

    return file_path, file_to_upload, file_type, extension


def _prepare_file_for_upload(
    file_path: str | None, file_to_upload: typing.BinaryIO | io.IOBase | None
) -> bytes:
    """
    Read file content for upload, handling both file paths and file-like objects.

    Args:
        file_path: Path to the file (if using file path)
        file_to_upload: File-like object (if using file-like object)

    Returns:
        File content as bytes

    Raises:
        ValueError: If both or neither parameters are provided
    """
    if file_path is not None:
        with open(file_path, "rb") as f:
            return f.read()
    else:
        if file_to_upload is None:
            raise ValueError("file_to_upload is None for file-like object case.")
        pos = file_to_upload.tell() if hasattr(file_to_upload, "tell") else None
        if hasattr(file_to_upload, "seek"):
            file_to_upload.seek(0)
        content = file_to_upload.read()
        if pos is not None and hasattr(file_to_upload, "seek"):
            file_to_upload.seek(pos)
        return content


class FilesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.upload_urls = UploadUrlsClient(base_client=self._base_client)

    def upload_file(
        self,
        file: typing.Union[str, pathlib.Path, typing.BinaryIO, io.IOBase],
    ) -> str:
        """
        Upload a file to Magic Hour's storage and return the path if it's already a URL.

        Args:
            file: Path to the local file to upload, a URL, or a file-like object

        Returns:
            The file path that can be used in other API calls.
            If the input is a URL, it will be returned as-is.

        Raises:
            FileNotFoundError: If the local file is not found
            ValueError: If the file type is not supported
            httpx.HTTPStatusError: If the upload fails
        """
        # If the input is already a URL, return it as-is
        if isinstance(file, str) and file.startswith(("http://", "https://")):
            return file

        file_path, file_to_upload, file_type, extension = _process_file_input(file)

        response = self.upload_urls.create(
            items=[
                V1FilesUploadUrlsCreateBodyItemsItem(
                    extension=extension, type_=file_type
                )
            ]
        )

        if not response.items:
            raise ValueError("No upload URL was returned from the server")

        upload_info = response.items[0]

        with httpx.Client() as client:
            content = _prepare_file_for_upload(
                file_path=file_path, file_to_upload=file_to_upload
            )
            response = client.put(url=upload_info.upload_url, content=content)
            response.raise_for_status()

        return upload_info.file_path


class AsyncFilesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.upload_urls = AsyncUploadUrlsClient(base_client=self._base_client)

    async def upload_file(
        self,
        file: typing.Union[str, pathlib.Path, typing.BinaryIO, io.IOBase],
    ) -> str:
        """Upload a file to Magic Hour's storage asynchronously or return the path if it's already a URL.

        Args:
            file: Path to the local file to upload, a URL, or a file-like object

        Returns:
            The file path that can be used in other API calls. If the input is a URL,
            it will be returned as-is.

        Raises:
            FileNotFoundError: If the local file is not found
            ValueError: If the file type is not supported
            httpx.HTTPStatusError: If the upload fails
        """
        # If the input is already a URL, return it as-is
        if isinstance(file, str) and file.startswith(("http://", "https://")):
            return file

        file_path, file_to_upload, file_type, extension = _process_file_input(file)

        response = await self.upload_urls.create(
            items=[
                V1FilesUploadUrlsCreateBodyItemsItem(
                    extension=extension, type_=file_type
                )
            ]
        )

        if not response.items:
            raise ValueError("No upload URL was returned from the server")

        upload_info = response.items[0]

        async with httpx.AsyncClient() as client:
            content = _prepare_file_for_upload(
                file_path=file_path, file_to_upload=file_to_upload
            )
            response = await client.put(url=upload_info.upload_url, content=content)
            response.raise_for_status()

        return upload_info.file_path
