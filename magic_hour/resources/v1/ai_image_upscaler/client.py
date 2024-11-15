"""
Generated by Sideko (sideko.dev)
"""

import typing

from magic_hour.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)
from magic_hour.types import models, params


class AiImageUpscalerClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: typing.Optional[params.PostV1AiImageUpscalerBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1AiImageUpscalerResponse:
        """
        Upscale your image using AI. Each 2x upscale costs 50 frames, and 4x upscale costs 200 frames.
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostV1AiImageUpscalerBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/ai-image-upscaler",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1AiImageUpscalerResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAiImageUpscalerClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: typing.Optional[params.PostV1AiImageUpscalerBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1AiImageUpscalerResponse:
        """
        Upscale your image using AI. Each 2x upscale costs 50 frames, and 4x upscale costs 200 frames.
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostV1AiImageUpscalerBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-image-upscaler",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1AiImageUpscalerResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
