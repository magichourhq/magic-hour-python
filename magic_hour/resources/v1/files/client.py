import httpx
import io
import mimetypes
import os
import pathlib
import typing
import typing_extensions

from magic_hour.helpers.logger import get_sdk_logger
from magic_hour.resources.v1.files.upload_urls import (
    AsyncUploadUrlsClient,
    UploadUrlsClient,
)
from magic_hour.types.params.v1_files_upload_urls_create_body_items_item import (
    V1FilesUploadUrlsCreateBodyItemsItem,
)
from make_api_request import AsyncBaseClient, SyncBaseClient
from pathlib import Path


logger = get_sdk_logger(__name__)


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

    file_type: typing.Union[
        typing_extensions.Literal["audio", "image", "video"], None
    ] = None
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
):
    """
    Process different file input types and return standardized information.

    Args:
        file: Path to the local file to upload, or a file-like object

    Returns:
        Tuple of (file_path, file_to_upload, file_type, extension)

    Raises:
        FileNotFoundError: If the local file is not found
        ValueError: If the file type is not supported or file-like object is invalid
    """

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
    file_path: typing.Union[str, None],
    file_to_upload: typing.Union[typing.BinaryIO, io.IOBase, None],
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
    """
    Client for uploading files to Magic Hour's storage.

    The Files client provides functionality to upload media files (images, videos, audio)
    to Magic Hour's secure storage. Once uploaded, files can be referenced in other API
    calls using the returned file path.

    Supported file types:
    - **Images**: PNG, JPG, JPEG, WebP, AVIF, JP2, TIFF, BMP
    - **Videos**: MP4, M4V, MOV, WebM
    - **Audio**: MP3, MPEG, WAV, AAC, AIFF, FLAC
    """

    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.upload_urls = UploadUrlsClient(base_client=self._base_client)

    def upload_file(
        self,
        file: typing.Union[str, pathlib.Path, typing.BinaryIO, io.IOBase],
    ) -> str:
        """
        Upload a file to Magic Hour's storage.

        This method uploads a file to Magic Hour's secure cloud storage and returns
        a file path that can be used as input for other Magic Hour API endpoints.
        The file type is automatically detected from the file extension or MIME type.

        Args:
            file: The file to upload. Can be:
                - **str**: Path to a local file (e.g., "/path/to/image.jpg")
                - **str**: URL of the file to upload, this will be skipped and the URL will be returned as is
                - **str**: if the string begins with "api-assets", the file will be assumed to be a blob path and already uploaded to Magic Hour's storage
                - **pathlib.Path**: Path object to a local file
                - **typing.BinaryIO or io.IOBase**: File-like object (must have a 'name' attribute)

        Returns:
            str: The uploaded file's path in Magic Hour's storage system.
                This path can be used as input for other API endpoints, such for `.assets.image_file_path`.

        Raises:
            FileNotFoundError: If the specified local file doesn't exist.
            ValueError: If the file type is not supported or file-like object is invalid.
            httpx.HTTPStatusError: If the upload request fails (network/server errors).

        Examples:
            Upload a local image file:

            ```python
            from magic_hour import Client
            from os import getenv

            client = Client(token=getenv("MAGIC_HOUR_API_TOKEN"))

            # Upload from file path
            file_path = client.v1.files.upload_file("/path/to/your/image.jpg")
            print(f"Uploaded file: {file_path}")

            # Use the uploaded file in other API calls
            result = client.v1.ai_image_upscaler.create(
                assets={"image_file_path": file_path}, style={"upscale_factor": 2}
            )
            ```

            Upload using pathlib.Path:

            ```python
            from pathlib import Path

            image_path = Path("./assets/photo.png")
            file_path = client.v1.files.upload_file(image_path)
            ```

            Upload from a file-like object:

            ```python
            with open("video.mp4", "rb") as video_file:
                file_path = client.v1.files.upload_file(video_file)
            ```
        """

        if isinstance(file, str) and file.startswith(("http://", "https://")):
            logger.info(f"{file} is a url. Skipping upload and returning the URL.")
            return file
        elif isinstance(file, str) and file.startswith("api-assets"):
            logger.info(
                f"{file} is begins with api-assets, assuming it's a blob path.. Skipping upload and returning the path."
            )
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

        with httpx.Client(timeout=None) as client:
            content = _prepare_file_for_upload(
                file_path=file_path, file_to_upload=file_to_upload
            )

            upload_response = client.put(url=upload_info.upload_url, content=content)
            upload_response.raise_for_status()

        logger.info(
            f"Uploaded {file_path} to Magic Hour storage at {upload_info.file_path}."
        )
        return upload_info.file_path


class AsyncFilesClient:
    """
    Async client for uploading files to Magic Hour's storage.

    The AsyncFilesClient provides asynchronous functionality to upload media files
    (images, videos, audio) to Magic Hour's secure storage. This is ideal for
    applications that need to handle multiple file uploads concurrently or integrate
    with async frameworks like FastAPI or aiohttp.

    Supported file types:
    - **Images**: PNG, JPG, JPEG, WebP, AVIF, JP2, TIFF, BMP
    - **Videos**: MP4, M4V, MOV, WebM
    - **Audio**: MP3, MPEG, WAV, AAC, AIFF, FLAC
    """

    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.upload_urls = AsyncUploadUrlsClient(base_client=self._base_client)

    async def upload_file(
        self,
        file: typing.Union[str, pathlib.Path, typing.BinaryIO, io.IOBase],
    ) -> str:
        """
        Upload a file to Magic Hour's storage asynchronously.

        This method asynchronously uploads a file to Magic Hour's secure cloud storage
        and returns a file path that can be used as input for other Magic Hour API endpoints.
        The file type is automatically detected from the file extension or MIME type.

        Args:
            file: The file to upload. Can be:
                - **str**: Path to a local file (e.g., "/path/to/image.jpg")
                - **str**: URL of the file to upload, this will be skipped and the URL will be returned as is
                - **str**: if the string begins with "api-assets", the file will be assumed to be a blob path and already uploaded to Magic Hour's storage
                - **pathlib.Path**: Path object to a local file
                - **typing.BinaryIO or io.IOBase**: File-like object (must have a 'name' attribute)

        Returns:
            str: The uploaded file's path in Magic Hour's storage system.
                This path can be used as input for other API endpoints, such for `.assets.image_file_path`.

        Raises:
            FileNotFoundError: If the specified local file doesn't exist.
            ValueError: If the file type is not supported or file-like object is invalid.
            httpx.HTTPStatusError: If the upload request fails (network/server errors).

        Examples:
            Basic async upload:

            ```python
            import asyncio
            from magic_hour import AsyncClient
            from os import getenv


            async def upload_example():
                client = AsyncClient(token=getenv("MAGIC_HOUR_API_TOKEN"))

                # Upload from file path
                file_path = await client.v1.files.upload_file("/path/to/your/image.jpg")
                print(f"Uploaded file: {file_path}")

                # Use the uploaded file in other API calls
                result = await client.v1.ai_image_upscaler.create(
                    assets={"image_file_path": file_path}, style={"upscale_factor": 2}
                )


            asyncio.run(upload_example())
            ```
        """
        if isinstance(file, str) and file.startswith(("http://", "https://")):
            logger.info(f"{file} is a url. Skipping upload and returning the URL.")
            return file
        elif isinstance(file, str) and file.startswith("api-assets"):
            logger.info(
                f"{file} is begins with api-assets, assuming it's a blob path.. Skipping upload and returning the path."
            )
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

        async with httpx.AsyncClient(timeout=None) as client:
            content = _prepare_file_for_upload(
                file_path=file_path, file_to_upload=file_to_upload
            )

            upload_response = await client.put(
                url=upload_info.upload_url, content=content
            )
            upload_response.raise_for_status()

        logger.info(
            f"Uploaded {file_path} to Magic Hour storage at {upload_info.file_path}."
        )
        return upload_info.file_path
