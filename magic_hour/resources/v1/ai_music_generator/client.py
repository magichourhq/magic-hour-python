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


class AiMusicGeneratorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        duration: int,
        style: params.V1AiMusicGeneratorCreateBodyStyle,
        additional_properties: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiMusicGeneratorCreateResponse:
        """
        AI Music Generator

        Generate music from a description, with optional custom lyrics or instrumental-only output. Costs 1 credits per requested second. Returns a project ID; poll GET /v1/audio-projects/{id} for status and downloads.

        POST /v1/ai-music-generator

        Args:
            additional_properties: typing.Dict[str, typing.Any]
            name: Give your audio a custom name for easy identification.
            duration: Requested track duration in seconds, from 15 to 300. Determines credits charged.
            style: V1AiMusicGeneratorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_music_generator.create(
            duration=120,
            style={
                "instrumental": False,
                "lyrics": "City lights are fading...",
                "prompt": "Dreamy synthwave with warm bass and soft vocals",
            },
            name="My Music Generator audio",
        )
        ```
        """
        _json = to_encodable(
            item={
                **(additional_properties or {}),
                "name": name,
                "duration": duration,
                "style": style,
            },
            dump_with=params._SerializerV1AiMusicGeneratorCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-music-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiMusicGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiMusicGeneratorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        duration: int,
        style: params.V1AiMusicGeneratorCreateBodyStyle,
        additional_properties: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiMusicGeneratorCreateResponse:
        """
        AI Music Generator

        Generate music from a description, with optional custom lyrics or instrumental-only output. Costs 1 credits per requested second. Returns a project ID; poll GET /v1/audio-projects/{id} for status and downloads.

        POST /v1/ai-music-generator

        Args:
            additional_properties: typing.Dict[str, typing.Any]
            name: Give your audio a custom name for easy identification.
            duration: Requested track duration in seconds, from 15 to 300. Determines credits charged.
            style: V1AiMusicGeneratorCreateBodyStyle
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_music_generator.create(
            duration=120,
            style={
                "instrumental": False,
                "lyrics": "City lights are fading...",
                "prompt": "Dreamy synthwave with warm bass and soft vocals",
            },
            name="My Music Generator audio",
        )
        ```
        """
        _json = to_encodable(
            item={
                **(additional_properties or {}),
                "name": name,
                "duration": duration,
                "style": style,
            },
            dump_with=params._SerializerV1AiMusicGeneratorCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-music-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiMusicGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )
