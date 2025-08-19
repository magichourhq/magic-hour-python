import os
import time
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

    def poll_until_complete(self, id: str) -> models.V1ImageProjectsGetResponse:
        """
        Poll until the image project is complete.
        """

        poll_interval = float(os.getenv("MAGIC_HOUR_POLL_INTERVAL", "0.5"))

        response = self.get(id=id)
        status = response.status

        while status not in ["complete", "error", "canceled"]:
            response = self.get(id=id)
            status = response.status
            time.sleep(poll_interval)

        return response


class AsyncImageProjectsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

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
