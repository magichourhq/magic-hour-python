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


class ImageProjectsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources

    # register sync api methods
    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetV1ImageProjectsIdResponse:
        """
        Get the details of a image project. The `download` field will be `null` unless the image was successfully rendered.

        The image can be one of the following status
        - `draft` - not currently used
        - `queued` - the job is queued and waiting for a GPU
        - `rendering` - the generation is in progress
        - `complete` - the image is successful created
        - `error` - an error occurred during rendering
        - `canceled` - image render is canceled by the user


        GET /v1/image-projects/{id}
        """

        # start -- build request data

        # end -- build request data

        # start -- send sync request
        return self._base_client.request(
            method="GET",
            path=f"/v1/image-projects/{id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetV1ImageProjectsIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request


class AsyncImageProjectsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources

    # register async api methods
    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetV1ImageProjectsIdResponse:
        """
        Get the details of a image project. The `download` field will be `null` unless the image was successfully rendered.

        The image can be one of the following status
        - `draft` - not currently used
        - `queued` - the job is queued and waiting for a GPU
        - `rendering` - the generation is in progress
        - `complete` - the image is successful created
        - `error` - an error occurred during rendering
        - `canceled` - image render is canceled by the user


        GET /v1/image-projects/{id}
        """

        # start -- build request data

        # end -- build request data

        # start -- send async request
        return await self._base_client.request(
            method="GET",
            path=f"/v1/image-projects/{id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetV1ImageProjectsIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request
