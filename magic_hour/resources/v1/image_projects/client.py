import asyncio
import os
import pydantic
import time
import typing

from magic_hour.helpers.download import download_files_async, download_files_sync
from magic_hour.helpers.logger import get_sdk_logger
from magic_hour.types import models
from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)


logger = get_sdk_logger(__name__)


class V1ImageProjectsGetResponseWithDownloads(models.V1ImageProjectsGetResponse):
    downloaded_paths: typing.Optional[typing.List[str]] = pydantic.Field(
        default=None, alias="downloaded_paths"
    )
    """
    The paths to the downloaded files.

    This field is only populated if `download_outputs` is True and the image project is complete.
    """


class ImageProjectsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def check_result(
        self,
        id: str,
        wait_for_completion: bool,
        download_outputs: bool,
        download_directory: typing.Optional[str] = None,
    ) -> V1ImageProjectsGetResponseWithDownloads:
        """
        Check the result of an image project with optional waiting and downloading.

        This method retrieves the status of an image project and optionally waits for completion
        and downloads the output files.

        Args:
            id: Unique ID of the image project
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided,
                the outputs will be downloaded to the current working directory

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The image project response with optional
                downloaded file paths included
        """
        api_response = self.get(id=id)
        if not wait_for_completion:
            response = V1ImageProjectsGetResponseWithDownloads(
                **api_response.model_dump()
            )
            return response

        poll_interval = float(os.getenv("MAGIC_HOUR_POLL_INTERVAL", "0.5"))

        status = api_response.status

        while status not in ["complete", "error", "canceled"]:
            api_response = self.get(id=id)
            status = api_response.status
            time.sleep(poll_interval)

        if api_response.status != "complete":
            log = logger.error if api_response.status == "error" else logger.info
            log(
                f"Image project {id} has status {api_response.status}: {api_response.error}"
            )
            return V1ImageProjectsGetResponseWithDownloads(**api_response.model_dump())

        if not download_outputs:
            return V1ImageProjectsGetResponseWithDownloads(**api_response.model_dump())

        downloaded_paths = download_files_sync(
            downloads=api_response.downloads,
            download_directory=download_directory,
        )

        return V1ImageProjectsGetResponseWithDownloads(
            **api_response.model_dump(), downloaded_paths=downloaded_paths
        )

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete image

        Permanently delete the rendered image(s). This action is not reversible, please be sure before deleting.

        DELETE /v1/image-projects/{id}

        Args:
            id: Unique ID of the image project. This value is returned by all of the POST APIs that create an image.
            request_options: Additional options to customize the HTTP request

        Returns:
            204

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.image_projects.delete(id="cuid-example")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/v1/image-projects/{id}",
            auth_names=["bearerAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.V1ImageProjectsGetResponse:
        """
        Get image details

        Get the details of a image project. The `downloads` field will be empty unless the image was successfully rendered.

        The image can be one of the following status
        - `draft` - not currently used
        - `queued` - the job is queued and waiting for a GPU
        - `rendering` - the generation is in progress
        - `complete` - the image is successful created
        - `error` - an error occurred during rendering
        - `canceled` - image render is canceled by the user


        GET /v1/image-projects/{id}

        Args:
            id: Unique ID of the image project. This value is returned by all of the POST APIs that create an image.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.image_projects.get(id="cuid-example")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v1/image-projects/{id}",
            auth_names=["bearerAuth"],
            cast_to=models.V1ImageProjectsGetResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncImageProjectsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def check_result(
        self,
        id: str,
        wait_for_completion: bool,
        download_outputs: bool,
        download_directory: typing.Optional[str] = None,
    ) -> V1ImageProjectsGetResponseWithDownloads:
        """
        Check the result of an image project with optional waiting and downloading.

        This method retrieves the status of an image project and optionally waits for completion
        and downloads the output files.

        Args:
            id: Unique ID of the image project
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided,
                the outputs will be downloaded to the current working directory

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The image project response with optional
                downloaded file paths included
        """
        api_response = await self.get(id=id)
        if not wait_for_completion:
            response = V1ImageProjectsGetResponseWithDownloads(
                **api_response.model_dump()
            )
            return response

        poll_interval = float(os.getenv("MAGIC_HOUR_POLL_INTERVAL", "0.5"))

        status = api_response.status

        while status not in ["complete", "error", "canceled"]:
            api_response = await self.get(id=id)
            status = api_response.status
            await asyncio.sleep(poll_interval)

        if api_response.status != "complete":
            log = logger.error if api_response.status == "error" else logger.info
            log(
                f"Image project {id} has status {api_response.status}: {api_response.error}"
            )
            return V1ImageProjectsGetResponseWithDownloads(**api_response.model_dump())

        if not download_outputs:
            return V1ImageProjectsGetResponseWithDownloads(**api_response.model_dump())

        downloaded_paths = await download_files_async(
            downloads=api_response.downloads,
            download_directory=download_directory,
        )

        return V1ImageProjectsGetResponseWithDownloads(
            **api_response.model_dump(), downloaded_paths=downloaded_paths
        )

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete image

        Permanently delete the rendered image(s). This action is not reversible, please be sure before deleting.

        DELETE /v1/image-projects/{id}

        Args:
            id: Unique ID of the image project. This value is returned by all of the POST APIs that create an image.
            request_options: Additional options to customize the HTTP request

        Returns:
            204

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.image_projects.delete(id="cuid-example")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/v1/image-projects/{id}",
            auth_names=["bearerAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.V1ImageProjectsGetResponse:
        """
        Get image details

        Get the details of a image project. The `downloads` field will be empty unless the image was successfully rendered.

        The image can be one of the following status
        - `draft` - not currently used
        - `queued` - the job is queued and waiting for a GPU
        - `rendering` - the generation is in progress
        - `complete` - the image is successful created
        - `error` - an error occurred during rendering
        - `canceled` - image render is canceled by the user


        GET /v1/image-projects/{id}

        Args:
            id: Unique ID of the image project. This value is returned by all of the POST APIs that create an image.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.image_projects.get(id="cuid-example")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v1/image-projects/{id}",
            auth_names=["bearerAuth"],
            cast_to=models.V1ImageProjectsGetResponse,
            request_options=request_options or default_request_options(),
        )
