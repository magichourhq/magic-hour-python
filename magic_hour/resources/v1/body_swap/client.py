import typing
import typing_extensions

from magic_hour.types import models, params
from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)


class BodySwapClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.V1BodySwapCreateBodyAssets,
        resolution: typing_extensions.Literal["1k", "2k", "4k", "640px"],
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1BodySwapCreateResponse:
        """
        Body Swap

        Swap a person into a scene image using Nano Banana 2. Credits depend on `resolution` (from 100 credits at 640px upward).

        POST /v1/body-swap

        Args:
            name: Give your image a custom name for easy identification.
            assets: Person image and scene image for body swap
            resolution: Output resolution. Determines credits charged for the run.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.body_swap.create(
            assets={
                "person_file_path": "api-assets/id/1234.png",
                "scene_file_path": "api-assets/id/5678.png",
            },
            resolution="1k",
            name="My Body Swap image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets, "resolution": resolution},
            dump_with=params._SerializerV1BodySwapCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/body-swap",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1BodySwapCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncBodySwapClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.V1BodySwapCreateBodyAssets,
        resolution: typing_extensions.Literal["1k", "2k", "4k", "640px"],
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1BodySwapCreateResponse:
        """
        Body Swap

        Swap a person into a scene image using Nano Banana 2. Credits depend on `resolution` (from 100 credits at 640px upward).

        POST /v1/body-swap

        Args:
            name: Give your image a custom name for easy identification.
            assets: Person image and scene image for body swap
            resolution: Output resolution. Determines credits charged for the run.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.body_swap.create(
            assets={
                "person_file_path": "api-assets/id/1234.png",
                "scene_file_path": "api-assets/id/5678.png",
            },
            resolution="1k",
            name="My Body Swap image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets, "resolution": resolution},
            dump_with=params._SerializerV1BodySwapCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/body-swap",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1BodySwapCreateResponse,
            request_options=request_options or default_request_options(),
        )
