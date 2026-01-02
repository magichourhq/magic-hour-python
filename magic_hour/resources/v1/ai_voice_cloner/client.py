import typing

from magic_hour.types import models, params
from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)


class AiVoiceClonerClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.V1AiVoiceClonerCreateBodyAssets,
        style: params.V1AiVoiceClonerCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiVoiceClonerCreateResponse:
        """
        AI Voice Cloner

        Clone a voice from an audio sample and generate speech.
        * Each character costs 0.05 credits.
        * The cost is rounded up to the nearest whole number

        POST /v1/ai-voice-cloner

        Args:
            name: The name of audio. This value is mainly used for your own identification of the audio.
            assets: Provide the assets for voice cloning.
            style: V1AiVoiceClonerCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_voice_cloner.create(
            assets={"audio_file_path": "api-assets/id/1234.mp3"},
            style={"prompt": "Hello, this is my cloned voice."},
            name="Voice Cloner audio",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets, "style": style},
            dump_with=params._SerializerV1AiVoiceClonerCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-voice-cloner",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiVoiceClonerCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiVoiceClonerClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.V1AiVoiceClonerCreateBodyAssets,
        style: params.V1AiVoiceClonerCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiVoiceClonerCreateResponse:
        """
        AI Voice Cloner

        Clone a voice from an audio sample and generate speech.
        * Each character costs 0.05 credits.
        * The cost is rounded up to the nearest whole number

        POST /v1/ai-voice-cloner

        Args:
            name: The name of audio. This value is mainly used for your own identification of the audio.
            assets: Provide the assets for voice cloning.
            style: V1AiVoiceClonerCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_voice_cloner.create(
            assets={"audio_file_path": "api-assets/id/1234.mp3"},
            style={"prompt": "Hello, this is my cloned voice."},
            name="Voice Cloner audio",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets, "style": style},
            dump_with=params._SerializerV1AiVoiceClonerCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-voice-cloner",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiVoiceClonerCreateResponse,
            request_options=request_options or default_request_options(),
        )
