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
import time
import sys


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


class _ProgressTracker:
    """Helper class to track upload progress and show progress bar for large uploads."""

    def __init__(self, total_size: int, filename: str = "file"):
        self.total_size = total_size
        self.filename = filename
        self.uploaded = 0
        self.start_time = time.time()
        self.show_progress = False
        self.last_update = 0

    def update(self, chunk_size: int):
        """Update progress and show progress bar if upload is taking longer than 5 seconds."""
        self.uploaded += chunk_size
        current_time = time.time()

        # Start showing progress after 5 seconds
        if not self.show_progress and (current_time - self.start_time) >= 5:
            self.show_progress = True
            print(f"\nUploading {self.filename}...")

        # Update progress bar every 0.5 seconds when showing progress
        if self.show_progress and (current_time - self.last_update) >= 0.5:
            self._show_progress_bar()
            self.last_update = current_time

    def _show_progress_bar(self):
        """Display a progress bar."""
        if self.total_size == 0:
            return

        percent = min(100, (self.uploaded / self.total_size) * 100)
        elapsed = time.time() - self.start_time

        # Calculate upload speed
        speed_mbps = (self.uploaded / (1024 * 1024)) / elapsed if elapsed > 0 else 0

        # Progress bar
        bar_length = 30
        filled_length = int(bar_length * percent // 100)
        bar = "█" * filled_length + "-" * (bar_length - filled_length)

        # Size display
        uploaded_mb = self.uploaded / (1024 * 1024)
        total_mb = self.total_size / (1024 * 1024)

        sys.stdout.write(
            f"\r[{bar}] {percent:.1f}% ({uploaded_mb:.1f}MB/{total_mb:.1f}MB) {speed_mbps:.1f}MB/s"
        )
        sys.stdout.flush()

    def finish(self):
        """Complete the progress tracking."""
        if self.show_progress:
            self._show_progress_bar()
            elapsed = time.time() - self.start_time
            print(f"\nUpload completed in {elapsed:.1f}s")


def _upload_with_progress(
    client: httpx.Client, url: str, content: bytes, filename: str = "file"
):
    """Upload with progress tracking for large files."""
    content_length = len(content)
    tracker = _ProgressTracker(content_length, filename)

    # Create a generator that yields chunks and tracks progress
    def content_generator():
        chunk_size = 8192  # 8KB chunks
        for i in range(0, len(content), chunk_size):
            chunk = content[i : i + chunk_size]
            tracker.update(len(chunk))
            yield chunk

    try:
        response = client.put(url, content=content_generator())
        tracker.finish()
        return response
    except Exception as e:
        if tracker.show_progress:
            print("\nUpload failed!")
        raise e


async def _upload_with_progress_async(
    client: httpx.AsyncClient, url: str, content: bytes, filename: str = "file"
):
    """Upload with progress tracking for large files (async version)."""
    content_length = len(content)
    tracker = _ProgressTracker(content_length, filename)

    # Create an async generator that yields chunks and tracks progress
    async def content_generator():
        chunk_size = 8192  # 8KB chunks
        for i in range(0, len(content), chunk_size):
            chunk = content[i : i + chunk_size]
            tracker.update(len(chunk))
            yield chunk

    try:
        response = await client.put(url, content=content_generator())
        tracker.finish()
        return response
    except Exception as e:
        if tracker.show_progress:
            print("\nUpload failed!")
        raise e


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

        with httpx.Client(timeout=None) as client:
            content = _prepare_file_for_upload(
                file_path=file_path, file_to_upload=file_to_upload
            )

            # Extract filename for progress display
            filename = "file"
            if file_path:
                filename = os.path.basename(file_path)
            elif file_to_upload:
                try:
                    file_name = getattr(file_to_upload, "name", None)
                    if file_name and isinstance(file_name, str):
                        filename = os.path.basename(file_name)
                except (AttributeError, TypeError):
                    pass

            response = _upload_with_progress(
                client, upload_info.upload_url, content, filename
            )
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

        async with httpx.AsyncClient(timeout=None) as client:
            content = _prepare_file_for_upload(
                file_path=file_path, file_to_upload=file_to_upload
            )

            # Extract filename for progress display
            filename = "file"
            if file_path:
                filename = os.path.basename(file_path)
            elif file_to_upload:
                try:
                    file_name = getattr(file_to_upload, "name", None)
                    if file_name and isinstance(file_name, str):
                        filename = os.path.basename(file_name)
                except (AttributeError, TypeError):
                    pass

            response = await _upload_with_progress_async(
                client, upload_info.upload_url, content, filename
            )
            response.raise_for_status()

        return upload_info.file_path
