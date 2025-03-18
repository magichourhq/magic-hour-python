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


class TextToVideoClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        end_seconds: float,
        orientation: typing_extensions.Literal["landscape", "portrait", "square"],
        style: params.PostV1TextToVideoBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1TextToVideoResponse:
        """
        Text-to-Video

        Create a Text To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](/products/text-to-video).


        POST /v1/text-to-video

        Args:
            name: The name of video
            end_seconds: The total duration of the output video in seconds.
            orientation: Determines the orientation of the output video
            style: PostV1TextToVideoBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.text_to_video.create(
            end_seconds=5.0,
            orientation="landscape",
            style={"prompt": "string"},
            name="Text To Video video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "end_seconds": end_seconds,
                "orientation": orientation,
                "style": style,
            },
            dump_with=params._SerializerPostV1TextToVideoBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/text-to-video",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1TextToVideoResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncTextToVideoClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        end_seconds: float,
        orientation: typing_extensions.Literal["landscape", "portrait", "square"],
        style: params.PostV1TextToVideoBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1TextToVideoResponse:
        """
        Text-to-Video

        Create a Text To Video video. The estimated frame cost is calculated using 30 FPS. This amount is deducted from your account balance when a video is queued. Once the video is complete, the cost will be updated based on the actual number of frames rendered.

        Get more information about this mode at our [product page](/products/text-to-video).


        POST /v1/text-to-video

        Args:
            name: The name of video
            end_seconds: The total duration of the output video in seconds.
            orientation: Determines the orientation of the output video
            style: PostV1TextToVideoBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.text_to_video.create(
            end_seconds=5.0,
            orientation="landscape",
            style={"prompt": "string"},
            name="Text To Video video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "end_seconds": end_seconds,
                "orientation": orientation,
                "style": style,
            },
            dump_with=params._SerializerPostV1TextToVideoBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/text-to-video",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1TextToVideoResponse,
            request_options=request_options or default_request_options(),
        )
