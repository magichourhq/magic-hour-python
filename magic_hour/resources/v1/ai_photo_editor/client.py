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


class AiPhotoEditorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources

    # register sync api methods
    def create(
        self,
        *,
        data: typing.Optional[params.PostV1AiPhotoEditorBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1AiPhotoEditorResponse:
        """
        > **NOTE**: this API is still in early development stages, and should be avoided. Please reach out to us if you're interested in this API.

        Edit photo using AI. Each photo costs 10 frames.

        POST /v1/ai-photo-editor
        """

        # start -- build request data
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostV1AiPhotoEditorBody
        )
        # end -- build request data

        # start -- send sync request
        return self._base_client.request(
            method="POST",
            path="/v1/ai-photo-editor",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1AiPhotoEditorResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request


class AsyncAiPhotoEditorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources

    # register async api methods
    async def create(
        self,
        *,
        data: typing.Optional[params.PostV1AiPhotoEditorBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1AiPhotoEditorResponse:
        """
        > **NOTE**: this API is still in early development stages, and should be avoided. Please reach out to us if you're interested in this API.

        Edit photo using AI. Each photo costs 10 frames.

        POST /v1/ai-photo-editor
        """

        # start -- build request data
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostV1AiPhotoEditorBody
        )
        # end -- build request data

        # start -- send async request
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-photo-editor",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1AiPhotoEditorResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request