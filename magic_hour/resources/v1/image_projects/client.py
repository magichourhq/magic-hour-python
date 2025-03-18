import typing

from magic_hour.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from magic_hour.types import models


class ImageProjectsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete image

        Permanently delete the rendered image. This action is not reversible, please be sure before deleting.

        DELETE /v1/image-projects/{id}

        Args:
            id: The id of the image project
            request_options: Additional options to customize the HTTP request

        Returns:
            204

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.image_projects.delete(id="cm6pvghix03bvyz0zwash6noj")
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
    ) -> models.GetV1ImageProjectsIdResponse:
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
            id: The id of the image project
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.image_projects.get(id="cm6pvghix03bvyz0zwash6noj")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v1/image-projects/{id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetV1ImageProjectsIdResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncImageProjectsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete image

        Permanently delete the rendered image. This action is not reversible, please be sure before deleting.

        DELETE /v1/image-projects/{id}

        Args:
            id: The id of the image project
            request_options: Additional options to customize the HTTP request

        Returns:
            204

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.image_projects.delete(id="cm6pvghix03bvyz0zwash6noj")
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
    ) -> models.GetV1ImageProjectsIdResponse:
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
            id: The id of the image project
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.image_projects.get(id="cm6pvghix03bvyz0zwash6noj")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v1/image-projects/{id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetV1ImageProjectsIdResponse,
            request_options=request_options or default_request_options(),
        )
