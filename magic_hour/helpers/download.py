import os
from pathlib import Path
from typing import Union, List
from urllib.parse import urlparse
import httpx
from magic_hour.types import models
import logging

logger = logging.getLogger(__name__)


def _compute_download_path(
    url: str, download_directory: Union[str, None] = None
) -> str:
    url_path = urlparse(url).path
    filename = Path(url_path).name
    if not filename or filename == "..":
        raise ValueError("Download URL must include a filename")
    if download_directory:
        return os.path.join(download_directory, filename)
    return filename


def _save_download(content: bytes, download_path: str) -> str:
    path = Path(download_path)
    candidate = download_path
    suffix = 0
    while True:
        try:
            file = open(candidate, "xb")
        except FileExistsError:
            suffix += 1
            candidate = str(path.with_name(f"{path.stem}_{suffix}{path.suffix}"))
            continue
        identity = None
        try:
            identity = os.fstat(file.fileno())
            file.write(content)
            file.close()
        except BaseException:
            # Preserve the write/close error even if closing or cleanup also fails.
            try:
                file.close()
            except OSError:
                pass
            if identity is not None:
                try:
                    # lstat avoids following a replacement symlink's target.
                    if os.path.samestat(identity, os.lstat(candidate)):
                        os.unlink(candidate)
                except OSError:
                    pass
            raise
        return candidate


def download_files_sync(
    downloads: Union[
        List[models.V1ImageProjectsGetResponseDownloadsItem],
        List[models.V1VideoProjectsGetResponseDownloadsItem],
        List[models.V1AudioProjectsGetResponseDownloadsItem],
    ],
    download_directory: Union[str, None] = None,
) -> List[str]:
    downloaded_paths: List[str] = []

    for download in downloads:
        with httpx.Client() as http_client:
            download_response = http_client.get(download.url)
            download_response.raise_for_status()

            download_path = _compute_download_path(
                download.url, download_directory=download_directory
            )

            download_path = _save_download(download_response.content, download_path)

            downloaded_paths.append(download_path)

            logger.info(f"Downloaded file saved as: {download_path}")

    return downloaded_paths


async def download_files_async(
    downloads: Union[
        List[models.V1ImageProjectsGetResponseDownloadsItem],
        List[models.V1VideoProjectsGetResponseDownloadsItem],
        List[models.V1AudioProjectsGetResponseDownloadsItem],
    ],
    download_directory: Union[str, None] = None,
) -> List[str]:
    downloaded_paths: List[str] = []

    for download in downloads:
        async with httpx.AsyncClient() as http_client:
            download_response = await http_client.get(download.url)
            download_response.raise_for_status()

            download_path = _compute_download_path(
                download.url, download_directory=download_directory
            )

            download_path = _save_download(download_response.content, download_path)

            downloaded_paths.append(download_path)

            logger.info(f"Downloaded file saved as: {download_path}")

    return downloaded_paths
