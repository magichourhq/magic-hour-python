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


class ImageToVideoClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.V1ImageToVideoCreateBodyAssets,
        end_seconds: float,
        height: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1ImageToVideoCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        width: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1ImageToVideoCreateResponse:
        """
        Image-to-Video

        Create a Image To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](https://magichour.ai/products/image-to-video).


        POST /v1/image-to-video

        Args:
            height: This field does not affect the output video's resolution. The video's orientation will match that of the input image.

        It is retained solely for backward compatibility and will be deprecated in the future.
            name: The name of video
            resolution: Controls the output video resolution. Defaults to `720p` if not specified.

        **Options:**
        - `480p` - Supports only 5 or 10 second videos. Output: 24fps. Cost: 120 credits per 5 seconds.
        - `720p` - Supports videos between 5-60 seconds. Output: 30fps. Cost: 300 credits per 5 seconds.
        - `1080p` - Supports videos between 5-60 seconds. Output: 30fps. Cost: 600 credits per 5 seconds. **Requires** `pro` or `business` tier.
            style: Attributed used to dictate the style of the output
            width: This field does not affect the output video's resolution. The video's orientation will match that of the input image.

        It is retained solely for backward compatibility and will be deprecated in the future.
            assets: Provide the assets for image-to-video.
            end_seconds: The total duration of the output video in seconds.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.image_to_video.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            end_seconds=5.0,
            height=960,
            name="Image To Video video",
            width=512,
        )
        ```
        """
        _json = to_encodable(
            item={
                "height": height,
                "name": name,
                "resolution": resolution,
                "style": style,
                "width": width,
                "assets": assets,
                "end_seconds": end_seconds,
            },
            dump_with=params._SerializerV1ImageToVideoCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/image-to-video",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1ImageToVideoCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncImageToVideoClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.V1ImageToVideoCreateBodyAssets,
        end_seconds: float,
        height: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1ImageToVideoCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        width: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1ImageToVideoCreateResponse:
        """
        Image-to-Video

        Create a Image To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](https://magichour.ai/products/image-to-video).


        POST /v1/image-to-video

        Args:
            height: This field does not affect the output video's resolution. The video's orientation will match that of the input image.

        It is retained solely for backward compatibility and will be deprecated in the future.
            name: The name of video
            resolution: Controls the output video resolution. Defaults to `720p` if not specified.

        **Options:**
        - `480p` - Supports only 5 or 10 second videos. Output: 24fps. Cost: 120 credits per 5 seconds.
        - `720p` - Supports videos between 5-60 seconds. Output: 30fps. Cost: 300 credits per 5 seconds.
        - `1080p` - Supports videos between 5-60 seconds. Output: 30fps. Cost: 600 credits per 5 seconds. **Requires** `pro` or `business` tier.
            style: Attributed used to dictate the style of the output
            width: This field does not affect the output video's resolution. The video's orientation will match that of the input image.

        It is retained solely for backward compatibility and will be deprecated in the future.
            assets: Provide the assets for image-to-video.
            end_seconds: The total duration of the output video in seconds.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.image_to_video.create(
            assets={"image_file_path": "api-assets/id/1234.png"},
            end_seconds=5.0,
            height=960,
            name="Image To Video video",
            width=512,
        )
        ```
        """
        _json = to_encodable(
            item={
                "height": height,
                "name": name,
                "resolution": resolution,
                "style": style,
                "width": width,
                "assets": assets,
                "end_seconds": end_seconds,
            },
            dump_with=params._SerializerV1ImageToVideoCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/image-to-video",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1ImageToVideoCreateResponse,
            request_options=request_options or default_request_options(),
        )
