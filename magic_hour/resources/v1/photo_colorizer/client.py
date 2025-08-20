import os
from pathlib import Path
import typing
import logging
import pydantic
import typing_extensions
from urllib.parse import urlparse
import httpx

from magic_hour.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from magic_hour.resources.v1.files.client import FilesClient
from magic_hour.resources.v1.image_projects.client import ImageProjectsClient
from magic_hour.types import models, params

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class V1PhotoColorizerGenerateBodyAssets(typing_extensions.TypedDict):
    image_file_path: typing_extensions.Required[str]
    """
    The image used to generate the colorized image. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """


def extract_filename_from_url(url: str) -> str:
    """
    Extract filename from URL, handling query parameters and URL encoding.

    Args:
        url: The URL to extract filename from
        default_filename: Fallback filename if extraction fails

    Returns:
        The extracted filename or default_filename

    Examples:
        >>> extract_filename_from_url("https://example.com/path/image.png?param=value")
        'image.png'
        >>> extract_filename_from_url("https://videos.magichour.ai/cmei3iv6t0e508f0zqzz9vbom/output.png?X-Goog-Algorithm=...")
        'output.png'
    """
    try:
        parsed_url = urlparse(url)
        path = parsed_url.path

        file = Path(path)
        return file.name
    except Exception:
        raise ValueError(f"Could not extract filename from {url}")


class ExtendedV1ImageProjectsGetResponse(models.V1ImageProjectsGetResponse):
    downloaded_paths: typing.Optional[typing.List[str]] = pydantic.Field(
        default=None, alias="downloaded_paths"
    )
    """
    The paths to the downloaded files.

    This field is only populated if `download_outputs` is True.
    """


class PhotoColorizerClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: V1PhotoColorizerGenerateBodyAssets,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_directory: typing.Optional[str] = None,
        download_outputs: bool = True,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtendedV1ImageProjectsGetResponse:
        """
        Generate colorized photo (alias for create with additional functionality).

        Colorize image. Each image costs 5 credits.

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for photo colorization
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            ExtendedV1ImageProjectsGetResponse: The response from the Photo Colorizer API with the downloaded paths if `download_outputs` is True.
        """

        file_client = FilesClient(base_client=self._base_client)

        image_file_path = assets.get("image_file_path")

        if image_file_path.startswith(("http://", "https://")):
            logger.info(f"{image_file_path} is a url. Skipping upload.")
            image_blob_path = image_file_path
        elif image_file_path.startswith("api-assets"):
            logger.info(
                f"{image_file_path} is begins with api-assets, assuming it's a blob path.. Skipping upload."
            )
            image_blob_path = image_file_path
        else:
            image_blob_path = file_client.upload_file(file=image_file_path)
            logger.info(
                f"Uploaded {image_file_path} to Magic Hour storage at {image_blob_path}."
            )

        assets["image_file_path"] = image_blob_path

        create_response = self.create(
            assets=assets, name=name, request_options=request_options
        )
        logger.info(f"Photo Colorizer response: {create_response}")

        image_projects_client = ImageProjectsClient(base_client=self._base_client)
        api_response = image_projects_client.get(id=create_response.id)

        if not wait_for_completion:
            response = ExtendedV1ImageProjectsGetResponse(**api_response.model_dump())
            return response

        api_response = image_projects_client.poll_until_complete(id=create_response.id)

        if api_response.status != "complete":
            logger.error(
                f"Photo Colorizer has status {api_response.status}: {api_response.error}"
            )
            return ExtendedV1ImageProjectsGetResponse(**api_response.model_dump())

        if not download_outputs:
            return ExtendedV1ImageProjectsGetResponse(**api_response.model_dump())

        downloaded_paths: list[str] = []
        for download in api_response.downloads:
            logger.info(f"Downloading {download.url} to local storage...")

            with httpx.Client() as http_client:
                download_response = http_client.get(download.url)
                download_response.raise_for_status()

                # Extract filename from URL or use a default
                filename = extract_filename_from_url(download.url)

                if download_directory:
                    download_path = os.path.join(download_directory, filename)
                else:
                    download_path = filename

                with open(download_path, "wb") as f:
                    f.write(download_response.content)

                downloaded_paths.append(download_path)

                logger.info(f"Downloaded file saved as: {download_path}")

        return ExtendedV1ImageProjectsGetResponse(
            **api_response.model_dump(), downloaded_paths=downloaded_paths
        )

    def create(
        self,
        *,
        assets: params.V1PhotoColorizerCreateBodyAssets,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1PhotoColorizerCreateResponse:
        """
        Photo Colorizer

        Colorize image. Each image costs 5 credits.

        POST /v1/photo-colorizer

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for photo colorization
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.photo_colorizer.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            name="Photo Colorizer image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets},
            dump_with=params._SerializerV1PhotoColorizerCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/photo-colorizer",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1PhotoColorizerCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncPhotoColorizerClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.V1PhotoColorizerCreateBodyAssets,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1PhotoColorizerCreateResponse:
        """
        Photo Colorizer

        Colorize image. Each image costs 5 credits.

        POST /v1/photo-colorizer

        Args:
            name: The name of image. This value is mainly used for your own identification of the image.
            assets: Provide the assets for photo colorization
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.photo_colorizer.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            name="Photo Colorizer image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets},
            dump_with=params._SerializerV1PhotoColorizerCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/photo-colorizer",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1PhotoColorizerCreateResponse,
            request_options=request_options or default_request_options(),
        )
