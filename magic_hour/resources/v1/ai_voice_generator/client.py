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


class AiVoiceGeneratorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        style: params.V1AiVoiceGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiVoiceGeneratorCreateResponse:
        """
        AI Voice Generator

        Generate speech from text. Each character costs 0.05 credits. The cost is rounded up to the nearest whole number.

        POST /v1/ai-voice-generator

        Args:
            name: The name of audio. This value is mainly used for your own identification of the audio.
            style: The content used to generate speech.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_voice_generator.create(
            style={"prompt": "Hello, how are you?", "voice_name": "Elon Musk"},
            name="Voice Generator audio",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "style": style},
            dump_with=params._SerializerV1AiVoiceGeneratorCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-voice-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiVoiceGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiVoiceGeneratorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        style: params.V1AiVoiceGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiVoiceGeneratorCreateResponse:
        """
        AI Voice Generator

        Generate speech from text. Each character costs 0.05 credits. The cost is rounded up to the nearest whole number.

        POST /v1/ai-voice-generator

        Args:
            name: The name of audio. This value is mainly used for your own identification of the audio.
            style: The content used to generate speech.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_voice_generator.create(
            style={"prompt": "Hello, how are you?", "voice_name": "Elon Musk"},
            name="Voice Generator audio",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "style": style},
            dump_with=params._SerializerV1AiVoiceGeneratorCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-voice-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiVoiceGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )
