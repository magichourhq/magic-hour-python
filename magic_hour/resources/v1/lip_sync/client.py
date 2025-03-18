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


class LipSyncClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.PostV1LipSyncBodyAssets,
        end_seconds: float,
        height: int,
        start_seconds: float,
        width: int,
        max_fps_limit: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1LipSyncResponse:
        """
        Lip Sync

        Create a Lip Sync video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](/products/lip-sync).


        POST /v1/lip-sync

        Args:
            max_fps_limit: Defines the maximum FPS (frames per second) for the output video. If the input video's FPS is lower than this limit, the output video will retain the input FPS. This is useful for reducing unnecessary frame usage in scenarios where high FPS is not required.
            name: The name of video
            assets: Provide the assets for lip-sync. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
            end_seconds: The end time of the input video in seconds
            height: The height of the final output video. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            start_seconds: The start time of the input video in seconds
            width: The width of the final output video. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.lip_sync.create(
            assets={
                "audio_file_path": "api-assets/id/1234.mp3",
                "video_source": "file",
            },
            end_seconds=15.0,
            height=960,
            start_seconds=0.0,
            width=512,
            max_fps_limit=12.0,
            name="Lip Sync video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "max_fps_limit": max_fps_limit,
                "name": name,
                "assets": assets,
                "end_seconds": end_seconds,
                "height": height,
                "start_seconds": start_seconds,
                "width": width,
            },
            dump_with=params._SerializerPostV1LipSyncBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/lip-sync",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1LipSyncResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncLipSyncClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.PostV1LipSyncBodyAssets,
        end_seconds: float,
        height: int,
        start_seconds: float,
        width: int,
        max_fps_limit: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1LipSyncResponse:
        """
        Lip Sync

        Create a Lip Sync video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](/products/lip-sync).


        POST /v1/lip-sync

        Args:
            max_fps_limit: Defines the maximum FPS (frames per second) for the output video. If the input video's FPS is lower than this limit, the output video will retain the input FPS. This is useful for reducing unnecessary frame usage in scenarios where high FPS is not required.
            name: The name of video
            assets: Provide the assets for lip-sync. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
            end_seconds: The end time of the input video in seconds
            height: The height of the final output video. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            start_seconds: The start time of the input video in seconds
            width: The width of the final output video. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.lip_sync.create(
            assets={
                "audio_file_path": "api-assets/id/1234.mp3",
                "video_source": "file",
            },
            end_seconds=15.0,
            height=960,
            start_seconds=0.0,
            width=512,
            max_fps_limit=12.0,
            name="Lip Sync video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "max_fps_limit": max_fps_limit,
                "name": name,
                "assets": assets,
                "end_seconds": end_seconds,
                "height": height,
                "start_seconds": start_seconds,
                "width": width,
            },
            dump_with=params._SerializerPostV1LipSyncBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/lip-sync",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1LipSyncResponse,
            request_options=request_options or default_request_options(),
        )
