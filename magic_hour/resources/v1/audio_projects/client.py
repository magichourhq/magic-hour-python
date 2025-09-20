import typing

from magic_hour.types import models
from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)


class AudioProjectsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

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
