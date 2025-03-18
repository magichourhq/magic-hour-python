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


class FaceSwapClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.PostV1FaceSwapBodyAssets,
        end_seconds: float,
        height: int,
        start_seconds: float,
        width: int,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1FaceSwapResponse:
        """
        Face Swap video

        Create a Face Swap video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](/products/face-swap).


        POST /v1/face-swap

        Args:
            name: The name of video
            assets: Provide the assets for face swap. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
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
        client.v1.face_swap.create(
            assets={"image_file_path": "image/id/1234.png", "video_source": "file"},
            end_seconds=15.0,
            height=960,
            start_seconds=0.0,
            width=512,
            name="Face Swap video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "assets": assets,
                "end_seconds": end_seconds,
                "height": height,
                "start_seconds": start_seconds,
                "width": width,
            },
            dump_with=params._SerializerPostV1FaceSwapBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/face-swap",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1FaceSwapResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncFaceSwapClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.PostV1FaceSwapBodyAssets,
        end_seconds: float,
        height: int,
        start_seconds: float,
        width: int,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1FaceSwapResponse:
        """
        Face Swap video

        Create a Face Swap video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](/products/face-swap).


        POST /v1/face-swap

        Args:
            name: The name of video
            assets: Provide the assets for face swap. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
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
        await client.v1.face_swap.create(
            assets={"image_file_path": "image/id/1234.png", "video_source": "file"},
            end_seconds=15.0,
            height=960,
            start_seconds=0.0,
            width=512,
            name="Face Swap video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "assets": assets,
                "end_seconds": end_seconds,
                "height": height,
                "start_seconds": start_seconds,
                "width": width,
            },
            dump_with=params._SerializerPostV1FaceSwapBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/face-swap",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1FaceSwapResponse,
            request_options=request_options or default_request_options(),
        )
