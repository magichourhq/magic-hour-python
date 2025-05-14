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


class PhotoColorizerClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

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
            name: The name of image
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
            name: The name of image
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
