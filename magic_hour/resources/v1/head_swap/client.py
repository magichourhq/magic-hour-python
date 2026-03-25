import typing

from magic_hour.types import models, params
from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)


class HeadSwapClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.V1HeadSwapCreateBodyAssets,
        max_resolution: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1HeadSwapCreateResponse:
        """
        Head Swap

        Swap a head onto a body image. Each image costs 10 credits. Output resolution depends on your subscription; you may set `max_resolution` lower than your plan maximum if desired.

        POST /v1/head-swap

        Args:
            max_resolution: Constrains the larger dimension (height or width) of the output. Omit to use the maximum allowed for your plan (capped at 2048px). Values above your plan maximum are clamped down to your plan's maximum.
            name: Give your image a custom name for easy identification.
            assets: Provide the body and head images for head swap
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.head_swap.create(
            assets={
                "body_file_path": "api-assets/id/1234.png",
                "head_file_path": "api-assets/id/5678.png",
            },
            max_resolution=1024,
            name="My Head Swap image",
        )
        ```
        """
        _json = to_encodable(
            item={"max_resolution": max_resolution, "name": name, "assets": assets},
            dump_with=params._SerializerV1HeadSwapCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/head-swap",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1HeadSwapCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncHeadSwapClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.V1HeadSwapCreateBodyAssets,
        max_resolution: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1HeadSwapCreateResponse:
        """
        Head Swap

        Swap a head onto a body image. Each image costs 10 credits. Output resolution depends on your subscription; you may set `max_resolution` lower than your plan maximum if desired.

        POST /v1/head-swap

        Args:
            max_resolution: Constrains the larger dimension (height or width) of the output. Omit to use the maximum allowed for your plan (capped at 2048px). Values above your plan maximum are clamped down to your plan's maximum.
            name: Give your image a custom name for easy identification.
            assets: Provide the body and head images for head swap
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.head_swap.create(
            assets={
                "body_file_path": "api-assets/id/1234.png",
                "head_file_path": "api-assets/id/5678.png",
            },
            max_resolution=1024,
            name="My Head Swap image",
        )
        ```
        """
        _json = to_encodable(
            item={"max_resolution": max_resolution, "name": name, "assets": assets},
            dump_with=params._SerializerV1HeadSwapCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/head-swap",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1HeadSwapCreateResponse,
            request_options=request_options or default_request_options(),
        )
