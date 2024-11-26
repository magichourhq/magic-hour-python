"""
Generated by Sideko (sideko.dev)
"""

import typing

from magic_hour.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from magic_hour.types import models


class VideoProjectsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources

    # register sync api methods
    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetV1VideoProjectsIdResponse:
        """
        Get the details of a video project. The `download` field will be `null` unless the video was successfully rendered.

        The video can be one of the following status
        - `draft` - not currently used
        - `queued` - the job is queued and waiting for a GPU
        - `rendering` - the generation is in progress
        - `complete` - the video is successful created
        - `error` - an error occurred during rendering
        - `canceled` - video render is canceled by the user


        GET /v1/video-projects/{id}
        """

        # start -- build request data

        # end -- build request data

        # start -- send sync request
        return self._base_client.request(
            method="GET",
            path=f"/v1/video-projects/{id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetV1VideoProjectsIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request


class AsyncVideoProjectsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources

    # register async api methods
    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetV1VideoProjectsIdResponse:
        """
        Get the details of a video project. The `download` field will be `null` unless the video was successfully rendered.

        The video can be one of the following status
        - `draft` - not currently used
        - `queued` - the job is queued and waiting for a GPU
        - `rendering` - the generation is in progress
        - `complete` - the video is successful created
        - `error` - an error occurred during rendering
        - `canceled` - video render is canceled by the user


        GET /v1/video-projects/{id}
        """

        # start -- build request data

        # end -- build request data

        # start -- send async request
        return await self._base_client.request(
            method="GET",
            path=f"/v1/video-projects/{id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetV1VideoProjectsIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request
