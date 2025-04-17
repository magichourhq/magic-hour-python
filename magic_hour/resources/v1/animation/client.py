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


class AnimationClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.V1AnimationCreateBodyAssets,
        end_seconds: float,
        fps: float,
        height: int,
        style: params.V1AnimationCreateBodyStyle,
        width: int,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AnimationCreateResponse:
        """
        Animation

        Create a Animation video. The estimated frame cost is calculated based on the `fps` and `end_seconds` input.

        POST /v1/animation

        Args:
            name: The name of video
            assets: Provide the assets for animation.
            end_seconds: The end time of the input video in seconds
            fps: The desire output video frame rate
            height: The height of the final output video. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            style: Defines the style of the output video
            width: The width of the final output video. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.animation.create(
            assets={
                "audio_file_path": "api-assets/id/1234.mp3",
                "audio_source": "file",
                "image_file_path": "api-assets/id/1234.png",
            },
            end_seconds=15.0,
            fps=12.0,
            height=960,
            style={
                "art_style": "Painterly Illustration",
                "camera_effect": "Accelerate",
                "prompt": "Cyberpunk city",
                "prompt_type": "ai_choose",
                "transition_speed": 5,
            },
            width=512,
            name="Animation video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "assets": assets,
                "end_seconds": end_seconds,
                "fps": fps,
                "height": height,
                "style": style,
                "width": width,
            },
            dump_with=params._SerializerV1AnimationCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/animation",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AnimationCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAnimationClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.V1AnimationCreateBodyAssets,
        end_seconds: float,
        fps: float,
        height: int,
        style: params.V1AnimationCreateBodyStyle,
        width: int,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AnimationCreateResponse:
        """
        Animation

        Create a Animation video. The estimated frame cost is calculated based on the `fps` and `end_seconds` input.

        POST /v1/animation

        Args:
            name: The name of video
            assets: Provide the assets for animation.
            end_seconds: The end time of the input video in seconds
            fps: The desire output video frame rate
            height: The height of the final output video. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            style: Defines the style of the output video
            width: The width of the final output video. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.animation.create(
            assets={
                "audio_file_path": "api-assets/id/1234.mp3",
                "audio_source": "file",
                "image_file_path": "api-assets/id/1234.png",
            },
            end_seconds=15.0,
            fps=12.0,
            height=960,
            style={
                "art_style": "Painterly Illustration",
                "camera_effect": "Accelerate",
                "prompt": "Cyberpunk city",
                "prompt_type": "ai_choose",
                "transition_speed": 5,
            },
            width=512,
            name="Animation video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "assets": assets,
                "end_seconds": end_seconds,
                "fps": fps,
                "height": height,
                "style": style,
                "width": width,
            },
            dump_with=params._SerializerV1AnimationCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/animation",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AnimationCreateResponse,
            request_options=request_options or default_request_options(),
        )
