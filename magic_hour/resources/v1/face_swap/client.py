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
        assets: params.V1FaceSwapCreateBodyAssets,
        end_seconds: float,
        start_seconds: float,
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
    ) -> models.V1FaceSwapCreateResponse:
        """
        Face Swap video

        Create a Face Swap video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](https://magichour.ai/products/face-swap).


        POST /v1/face-swap

        Args:
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
            assets: Provide the assets for face swap. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
            end_seconds: The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
            start_seconds: The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.face_swap.create(
            assets={
                "face_mappings": [
                    {
                        "new_face": "api-assets/id/1234.png",
                        "original_face": "api-assets/id/0-0.png",
                    }
                ],
                "face_swap_mode": "all-faces",
                "image_file_path": "image/id/1234.png",
                "video_file_path": "api-assets/id/1234.mp4",
                "video_source": "file",
            },
            end_seconds=15.0,
            start_seconds=0.0,
            name="Face Swap video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "height": height,
                "name": name,
                "width": width,
                "assets": assets,
                "end_seconds": end_seconds,
                "start_seconds": start_seconds,
            },
            dump_with=params._SerializerV1FaceSwapCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/face-swap",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1FaceSwapCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncFaceSwapClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.V1FaceSwapCreateBodyAssets,
        end_seconds: float,
        start_seconds: float,
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
    ) -> models.V1FaceSwapCreateResponse:
        """
        Face Swap video

        Create a Face Swap video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](https://magichour.ai/products/face-swap).


        POST /v1/face-swap

        Args:
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
            assets: Provide the assets for face swap. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
            end_seconds: The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
            start_seconds: The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.face_swap.create(
            assets={
                "face_mappings": [
                    {
                        "new_face": "api-assets/id/1234.png",
                        "original_face": "api-assets/id/0-0.png",
                    }
                ],
                "face_swap_mode": "all-faces",
                "image_file_path": "image/id/1234.png",
                "video_file_path": "api-assets/id/1234.mp4",
                "video_source": "file",
            },
            end_seconds=15.0,
            start_seconds=0.0,
            name="Face Swap video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "height": height,
                "name": name,
                "width": width,
                "assets": assets,
                "end_seconds": end_seconds,
                "start_seconds": start_seconds,
            },
            dump_with=params._SerializerV1FaceSwapCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/face-swap",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1FaceSwapCreateResponse,
            request_options=request_options or default_request_options(),
        )
