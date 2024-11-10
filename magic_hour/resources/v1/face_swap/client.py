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


class FaceSwapClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: typing.Optional[params.PostV1FaceSwapBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1FaceSwapResponse:
        """
        Create a Face Swap video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerPostV1FaceSwapBody)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/face-swap",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1FaceSwapResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncFaceSwapClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: typing.Optional[params.PostV1FaceSwapBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1FaceSwapResponse:
        """
        Create a Face Swap video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerPostV1FaceSwapBody)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/face-swap",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1FaceSwapResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
