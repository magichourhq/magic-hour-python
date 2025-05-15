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


class AiTalkingPhotoClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.V1AiTalkingPhotoCreateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1AiTalkingPhotoCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiTalkingPhotoCreateResponse:
        """
        AI Talking Photo

        Create a talking photo from an image and audio or text input.

        POST /v1/ai-talking-photo

        Args:
            name: The name of image
            style: Attributes used to dictate the style of the output
            assets: Provide the assets for creating a talking photo
            end_seconds: The end time of the input audio in seconds. The maximum duration allowed is 30 seconds.
            start_seconds: The start time of the input audio in seconds. The maximum duration allowed is 30 seconds.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_talking_photo.create(
            assets={
                "audio_file_path": "api-assets/id/1234.mp3",
                "image_file_path": "api-assets/id/1234.png",
            },
            end_seconds=15.0,
            start_seconds=0.0,
            name="Talking Photo image",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "style": style,
                "assets": assets,
                "end_seconds": end_seconds,
                "start_seconds": start_seconds,
            },
            dump_with=params._SerializerV1AiTalkingPhotoCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-talking-photo",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiTalkingPhotoCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiTalkingPhotoClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.V1AiTalkingPhotoCreateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        style: typing.Union[
            typing.Optional[params.V1AiTalkingPhotoCreateBodyStyle], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiTalkingPhotoCreateResponse:
        """
        AI Talking Photo

        Create a talking photo from an image and audio or text input.

        POST /v1/ai-talking-photo

        Args:
            name: The name of image
            style: Attributes used to dictate the style of the output
            assets: Provide the assets for creating a talking photo
            end_seconds: The end time of the input audio in seconds. The maximum duration allowed is 30 seconds.
            start_seconds: The start time of the input audio in seconds. The maximum duration allowed is 30 seconds.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_talking_photo.create(
            assets={
                "audio_file_path": "api-assets/id/1234.mp3",
                "image_file_path": "api-assets/id/1234.png",
            },
            end_seconds=15.0,
            start_seconds=0.0,
            name="Talking Photo image",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "style": style,
                "assets": assets,
                "end_seconds": end_seconds,
                "start_seconds": start_seconds,
            },
            dump_with=params._SerializerV1AiTalkingPhotoCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-talking-photo",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiTalkingPhotoCreateResponse,
            request_options=request_options or default_request_options(),
        )
