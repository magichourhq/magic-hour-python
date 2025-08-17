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

        Get more information about this mode at our [product page](https://magichour.ai/products/video-to-video).


        POST /v1/video-to-video

        Args:
            fps_resolution: Determines whether the resulting video will have the same frame per second as the original video, or half.
        * `FULL` - the result video will have the same FPS as the input video
        * `HALF` - the result video will have half the FPS as the input video
            height: `height` is deprecated and no longer influences the output video's resolution.

        Output resolution is determined by the **minimum** of:
        - The resolution of the input video
        - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.

        This field is retained only for backward compatibility and will be removed in a future release.
            name: The name of video. This value is mainly used for your own identification of the video.
            width: `width` is deprecated and no longer influences the output video's resolution.

        Output resolution is determined by the **minimum** of:
        - The resolution of the input video
        - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.

        This field is retained only for backward compatibility and will be removed in a future release.
            assets: Provide the assets for video-to-video. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
            end_seconds: The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
            start_seconds: The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
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
                "model": "default",
                "prompt": "string",
                "prompt_type": "default",
                "version": "default",
            },
            fps_resolution="HALF",
            name="Video To Video video",
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

        Get more information about this mode at our [product page](https://magichour.ai/products/video-to-video).


        POST /v1/video-to-video

        Args:
            fps_resolution: Determines whether the resulting video will have the same frame per second as the original video, or half.
        * `FULL` - the result video will have the same FPS as the input video
        * `HALF` - the result video will have half the FPS as the input video
            height: `height` is deprecated and no longer influences the output video's resolution.

        Output resolution is determined by the **minimum** of:
        - The resolution of the input video
        - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.

        This field is retained only for backward compatibility and will be removed in a future release.
            name: The name of video. This value is mainly used for your own identification of the video.
            width: `width` is deprecated and no longer influences the output video's resolution.

        Output resolution is determined by the **minimum** of:
        - The resolution of the input video
        - The maximum resolution allowed by your subscription tier. See our [pricing page](https://magichour.ai/pricing) for more details.

        This field is retained only for backward compatibility and will be removed in a future release.
            assets: Provide the assets for video-to-video. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
            end_seconds: The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
            start_seconds: The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
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
                "model": "default",
                "prompt": "string",
                "prompt_type": "default",
                "version": "default",
            },
            fps_resolution="HALF",
            name="Video To Video video",
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
