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
    if download_directory:
        return os.path.join(download_directory, filename)
    return filename


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

            with open(download_path, "wb") as f:
                f.write(download_response.content)

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

            with open(download_path, "wb") as f:
                f.write(download_response.content)

            downloaded_paths.append(download_path)

            logger.info(f"Downloaded file saved as: {download_path}")

    return downloaded_paths
