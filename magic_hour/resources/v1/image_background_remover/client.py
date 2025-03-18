import typing

from magic_hour.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from magic_hour.types import models, params


class ImageBackgroundRemoverClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.PostV1ImageBackgroundRemoverBodyAssets,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1ImageBackgroundRemoverResponse:
        """
        Image Background Remover

        Remove background from image. Each image costs 5 frames.

        POST /v1/image-background-remover

        Args:
            name: The name of image
            assets: Provide the assets for background removal
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.image_background_remover.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            name="Background Remover image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets},
            dump_with=params._SerializerPostV1ImageBackgroundRemoverBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/image-background-remover",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1ImageBackgroundRemoverResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncImageBackgroundRemoverClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.PostV1ImageBackgroundRemoverBodyAssets,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1ImageBackgroundRemoverResponse:
        """
        Image Background Remover

        Remove background from image. Each image costs 5 frames.

        POST /v1/image-background-remover

        Args:
            name: The name of image
            assets: Provide the assets for background removal
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.image_background_remover.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            name="Background Remover image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets},
            dump_with=params._SerializerPostV1ImageBackgroundRemoverBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/image-background-remover",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1ImageBackgroundRemoverResponse,
            request_options=request_options or default_request_options(),
        )
