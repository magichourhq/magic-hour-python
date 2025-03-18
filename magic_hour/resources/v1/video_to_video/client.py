import typing
import typing_extensions

from magic_hour.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from magic_hour.types import models, params


class VideoToVideoClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.PostV1VideoToVideoBodyAssets,
        end_seconds: float,
        height: int,
        start_seconds: float,
        style: params.PostV1VideoToVideoBodyStyle,
        width: int,
        fps_resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["FULL", "HALF"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1VideoToVideoResponse:
        """
        Video-to-Video

        Create a Video To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](/products/video-to-video).


        POST /v1/video-to-video

        Args:
            fps_resolution: Determines whether the resulting video will have the same frame per second as the original video, or half.
        * `FULL` - the result video will have the same FPS as the input video
        * `HALF` - the result video will have half the FPS as the input video
            name: The name of video
            assets: Provide the assets for video-to-video. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
            end_seconds: The end time of the input video in seconds
            height: The height of the final output video. Must be divisible by 64. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            start_seconds: The start time of the input video in seconds
            style: PostV1VideoToVideoBodyStyle
            width: The width of the final output video. Must be divisible by 64. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.video_to_video.create(
            assets={"video_source": "file"},
            end_seconds=15.0,
            height=960,
            start_seconds=0.0,
            style={
                "art_style": "3D Render",
                "model": "Absolute Reality",
                "prompt": "string",
                "prompt_type": "append_default",
                "version": "default",
            },
            width=512,
            fps_resolution="HALF",
            name="Video To Video video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "fps_resolution": fps_resolution,
                "name": name,
                "assets": assets,
                "end_seconds": end_seconds,
                "height": height,
                "start_seconds": start_seconds,
                "style": style,
                "width": width,
            },
            dump_with=params._SerializerPostV1VideoToVideoBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/video-to-video",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1VideoToVideoResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncVideoToVideoClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.PostV1VideoToVideoBodyAssets,
        end_seconds: float,
        height: int,
        start_seconds: float,
        style: params.PostV1VideoToVideoBodyStyle,
        width: int,
        fps_resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["FULL", "HALF"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1VideoToVideoResponse:
        """
        Video-to-Video

        Create a Video To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](/products/video-to-video).


        POST /v1/video-to-video

        Args:
            fps_resolution: Determines whether the resulting video will have the same frame per second as the original video, or half.
        * `FULL` - the result video will have the same FPS as the input video
        * `HALF` - the result video will have half the FPS as the input video
            name: The name of video
            assets: Provide the assets for video-to-video. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
            end_seconds: The end time of the input video in seconds
            height: The height of the final output video. Must be divisible by 64. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            start_seconds: The start time of the input video in seconds
            style: PostV1VideoToVideoBodyStyle
            width: The width of the final output video. Must be divisible by 64. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.video_to_video.create(
            assets={"video_source": "file"},
            end_seconds=15.0,
            height=960,
            start_seconds=0.0,
            style={
                "art_style": "3D Render",
                "model": "Absolute Reality",
                "prompt": "string",
                "prompt_type": "append_default",
                "version": "default",
            },
            width=512,
            fps_resolution="HALF",
            name="Video To Video video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "fps_resolution": fps_resolution,
                "name": name,
                "assets": assets,
                "end_seconds": end_seconds,
                "height": height,
                "start_seconds": start_seconds,
                "style": style,
                "width": width,
            },
            dump_with=params._SerializerPostV1VideoToVideoBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/video-to-video",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1VideoToVideoResponse,
            request_options=request_options or default_request_options(),
        )
