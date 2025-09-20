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


class V1AudioProjectsGetResponseWithDownloads(models.V1AudioProjectsGetResponse):
    downloaded_paths: typing.Optional[typing.List[str]] = pydantic.Field(
        default=None, alias="downloaded_paths"
    )
    """
    The paths to the downloaded files.

    This field is only populated if `download_outputs` is True and the audio project is complete.
    """


class AudioProjectsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def check_result(
        self,
        id: str,
        wait_for_completion: bool,
        download_outputs: bool,
        download_directory: typing.Optional[str] = None,
    ) -> V1AudioProjectsGetResponseWithDownloads:
        """
        Check the result of an audio project with optional waiting and downloading.

        This method retrieves the status of an audio project and optionally waits for completion
        and downloads the output files.

        Args:
            id: Unique ID of the audio project
            wait_for_completion: Whether to wait for the audio project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided,
                the outputs will be downloaded to the current working directory

        Returns:
            V1AudioProjectsGetResponseWithDownloads: The audio project response with optional
                downloaded file paths included
        """
        api_response = self.get(id=id)
        if not wait_for_completion:
            response = V1AudioProjectsGetResponseWithDownloads(
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
                f"Audio project {id} has status {api_response.status}: {api_response.error}"
            )
            return V1AudioProjectsGetResponseWithDownloads(**api_response.model_dump())

        if not download_outputs:
            return V1AudioProjectsGetResponseWithDownloads(**api_response.model_dump())

        downloaded_paths = download_files_sync(
            downloads=api_response.downloads,
            download_directory=download_directory,
        )

        return V1AudioProjectsGetResponseWithDownloads(
            **api_response.model_dump(), downloaded_paths=downloaded_paths
        )

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete audio

        Permanently delete the rendered audio file(s). This action is not reversible, please be sure before deleting.

        DELETE /v1/audio-projects/{id}

        Args:
            id: Unique ID of the audio project. This value is returned by all of the POST APIs that create an audio.
            request_options: Additional options to customize the HTTP request

        Returns:
            204

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.audio_projects.delete(id="cuid-example")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/v1/audio-projects/{id}",
            auth_names=["bearerAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.V1AudioProjectsGetResponse:
        """
        Get audio details

        Get the details of a audio project. The `downloads` field will be empty unless the audio was successfully rendered.

        The audio can be one of the following status
        - `draft` - not currently used
        - `queued` - the job is queued and waiting for a GPU
        - `rendering` - the generation is in progress
        - `complete` - the audio is successful created
        - `error` - an error occurred during rendering
        - `canceled` - audio render is canceled by the user


        GET /v1/audio-projects/{id}

        Args:
            id: Unique ID of the audio project. This value is returned by all of the POST APIs that create an audio.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.audio_projects.get(id="cuid-example")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v1/audio-projects/{id}",
            auth_names=["bearerAuth"],
            cast_to=models.V1AudioProjectsGetResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAudioProjectsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def check_result(
        self,
        id: str,
        wait_for_completion: bool,
        download_outputs: bool,
        download_directory: typing.Optional[str] = None,
    ) -> V1AudioProjectsGetResponseWithDownloads:
        """
        Check the result of an audio project with optional waiting and downloading.

        This method retrieves the status of an audio project and optionally waits for completion
        and downloads the output files.

        Args:
            id: Unique ID of the audio project
            wait_for_completion: Whether to wait for the audio project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided,
                the outputs will be downloaded to the current working directory

        Returns:
            V1AudioProjectsGetResponseWithDownloads: The audio project response with optional
                downloaded file paths included
        """
        api_response = await self.get(id=id)
        if not wait_for_completion:
            response = V1AudioProjectsGetResponseWithDownloads(
                **api_response.model_dump()
            )
            return response

        poll_interval = float(os.getenv("MAGIC_HOUR_POLL_INTERVAL", "0.5"))

        status = api_response.status

        while status not in ["complete", "error", "canceled"]:
            api_response = await self.get(id=id)
            status = api_response.status
            time.sleep(poll_interval)

        if api_response.status != "complete":
            log = logger.error if api_response.status == "error" else logger.info
            log(
                f"Audio project {id} has status {api_response.status}: {api_response.error}"
            )
            return V1AudioProjectsGetResponseWithDownloads(**api_response.model_dump())

        if not download_outputs:
            return V1AudioProjectsGetResponseWithDownloads(**api_response.model_dump())

        downloaded_paths = await download_files_async(
            downloads=api_response.downloads,
            download_directory=download_directory,
        )

        return V1AudioProjectsGetResponseWithDownloads(
            **api_response.model_dump(), downloaded_paths=downloaded_paths
        )

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete audio

        Permanently delete the rendered audio file(s). This action is not reversible, please be sure before deleting.

        DELETE /v1/audio-projects/{id}

        Args:
            id: Unique ID of the audio project. This value is returned by all of the POST APIs that create an audio.
            request_options: Additional options to customize the HTTP request

        Returns:
            204

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.audio_projects.delete(id="cuid-example")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/v1/audio-projects/{id}",
            auth_names=["bearerAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.V1AudioProjectsGetResponse:
        """
        Get audio details

        Get the details of a audio project. The `downloads` field will be empty unless the audio was successfully rendered.

        The audio can be one of the following status
        - `draft` - not currently used
        - `queued` - the job is queued and waiting for a GPU
        - `rendering` - the generation is in progress
        - `complete` - the audio is successful created
        - `error` - an error occurred during rendering
        - `canceled` - audio render is canceled by the user


        GET /v1/audio-projects/{id}

        Args:
            id: Unique ID of the audio project. This value is returned by all of the POST APIs that create an audio.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.audio_projects.get(id="cuid-example")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v1/audio-projects/{id}",
            auth_names=["bearerAuth"],
            cast_to=models.V1AudioProjectsGetResponse,
            request_options=request_options or default_request_options(),
        )
