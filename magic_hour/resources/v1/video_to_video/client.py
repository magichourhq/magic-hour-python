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
        assets: params.V1VideoToVideoCreateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        style: params.V1VideoToVideoCreateBodyStyle,
        fps_resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["FULL", "HALF"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        height: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        width: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1VideoToVideoCreateResponse:
        """
        Video-to-Video

        Create a Video To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](/products/video-to-video).


        POST /v1/video-to-video

        Args:
            fps_resolution: Determines whether the resulting video will have the same frame per second as the original video, or half.
        * `FULL` - the result video will have the same FPS as the input video
        * `HALF` - the result video will have half the FPS as the input video
            height: Used to determine the dimensions of the output video.

        * If height is provided, width will also be required. The larger value between width and height will be used to determine the maximum output resolution while maintaining the original aspect ratio.
        * If both height and width are omitted, the video will be resized according to your subscription's maximum resolution, while preserving aspect ratio.

        Note: if the video's original resolution is less than the maximum, the video will not be resized.

        See our [pricing page](https://magichour.ai/pricing) for more details.
            name: The name of video
            width: Used to determine the dimensions of the output video.

        * If width is provided, height will also be required. The larger value between width and height will be used to determine the maximum output resolution while maintaining the original aspect ratio.
        * If both height and width are omitted, the video will be resized according to your subscription's maximum resolution, while preserving aspect ratio.

        Note: if the video's original resolution is less than the maximum, the video will not be resized.

        See our [pricing page](https://magichour.ai/pricing) for more details.
            assets: Provide the assets for video-to-video. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
            end_seconds: The end time of the input video in seconds
            start_seconds: The start time of the input video in seconds
            style: V1VideoToVideoCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.video_to_video.create(
            assets={
                "video_file_path": "api-assets/id/1234.mp4",
                "video_source": "file",
            },
            end_seconds=15.0,
            start_seconds=0.0,
            style={
                "art_style": "3D Render",
                "model": "Absolute Reality",
                "prompt": "string",
                "prompt_type": "append_default",
                "version": "default",
            },
            fps_resolution="HALF",
            height=960,
            name="Video To Video video",
            width=512,
        )
        ```
        """
        _json = to_encodable(
            item={
                "fps_resolution": fps_resolution,
                "height": height,
                "name": name,
                "width": width,
                "assets": assets,
                "end_seconds": end_seconds,
                "start_seconds": start_seconds,
                "style": style,
            },
            dump_with=params._SerializerV1VideoToVideoCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/video-to-video",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1VideoToVideoCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncVideoToVideoClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.V1VideoToVideoCreateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        style: params.V1VideoToVideoCreateBodyStyle,
        fps_resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["FULL", "HALF"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        height: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        width: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1VideoToVideoCreateResponse:
        """
        Video-to-Video

        Create a Video To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](/products/video-to-video).


        POST /v1/video-to-video

        Args:
            fps_resolution: Determines whether the resulting video will have the same frame per second as the original video, or half.
        * `FULL` - the result video will have the same FPS as the input video
        * `HALF` - the result video will have half the FPS as the input video
            height: Used to determine the dimensions of the output video.

        * If height is provided, width will also be required. The larger value between width and height will be used to determine the maximum output resolution while maintaining the original aspect ratio.
        * If both height and width are omitted, the video will be resized according to your subscription's maximum resolution, while preserving aspect ratio.

        Note: if the video's original resolution is less than the maximum, the video will not be resized.

        See our [pricing page](https://magichour.ai/pricing) for more details.
            name: The name of video
            width: Used to determine the dimensions of the output video.

        * If width is provided, height will also be required. The larger value between width and height will be used to determine the maximum output resolution while maintaining the original aspect ratio.
        * If both height and width are omitted, the video will be resized according to your subscription's maximum resolution, while preserving aspect ratio.

        Note: if the video's original resolution is less than the maximum, the video will not be resized.

        See our [pricing page](https://magichour.ai/pricing) for more details.
            assets: Provide the assets for video-to-video. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
            end_seconds: The end time of the input video in seconds
            start_seconds: The start time of the input video in seconds
            style: V1VideoToVideoCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.video_to_video.create(
            assets={
                "video_file_path": "api-assets/id/1234.mp4",
                "video_source": "file",
            },
            end_seconds=15.0,
            start_seconds=0.0,
            style={
                "art_style": "3D Render",
                "model": "Absolute Reality",
                "prompt": "string",
                "prompt_type": "append_default",
                "version": "default",
            },
            fps_resolution="HALF",
            height=960,
            name="Video To Video video",
            width=512,
        )
        ```
        """
        _json = to_encodable(
            item={
                "fps_resolution": fps_resolution,
                "height": height,
                "name": name,
                "width": width,
                "assets": assets,
                "end_seconds": end_seconds,
                "start_seconds": start_seconds,
                "style": style,
            },
            dump_with=params._SerializerV1VideoToVideoCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/video-to-video",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1VideoToVideoCreateResponse,
            request_options=request_options or default_request_options(),
        )
