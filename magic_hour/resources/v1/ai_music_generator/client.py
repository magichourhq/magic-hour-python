import typing

from magic_hour.helpers.logger import get_sdk_logger
from magic_hour.resources.v1.audio_projects.client import (
    AsyncAudioProjectsClient,
    AudioProjectsClient,
    V1AudioProjectsGetResponseWithDownloads,
)
from magic_hour.types import models, params
from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)


logger = get_sdk_logger(__name__)


class AiMusicGeneratorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
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
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1AudioProjectsGetResponseWithDownloads:
        """
        Generate music with automatic polling and downloads.

        Accepts the same parameters as create(), plus wait_for_completion,
        download_outputs, and download_directory. These default to waiting
        for completion and downloading outputs to the current directory.

        Returns:
            The audio project with downloaded_paths when downloads are enabled.

        Examples:
        ```py
        response = client.v1.ai_music_generator.generate(
            duration=120,
            style={"prompt": "Dreamy synthwave with warm bass"},
        )
        ```
        """
        create_response = self.create(
            duration=duration,
            style=style,
            additional_properties=additional_properties,
            name=name,
            request_options=request_options,
        )
        logger.info(f"Created ai_music_generator project {create_response.id}")

        projects_client = AudioProjectsClient(base_client=self._base_client)
        return projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

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

    async def generate(
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
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1AudioProjectsGetResponseWithDownloads:
        """
        Generate music with automatic polling and downloads.

        Accepts the same parameters as create(), plus wait_for_completion,
        download_outputs, and download_directory. These default to waiting
        for completion and downloading outputs to the current directory.

        Returns:
            The audio project with downloaded_paths when downloads are enabled.

        Examples:
        ```py
        response = await client.v1.ai_music_generator.generate(
            duration=120,
            style={"prompt": "Dreamy synthwave with warm bass"},
        )
        ```
        """
        create_response = await self.create(
            duration=duration,
            style=style,
            additional_properties=additional_properties,
            name=name,
            request_options=request_options,
        )
        logger.info(f"Created ai_music_generator project {create_response.id}")

        projects_client = AsyncAudioProjectsClient(base_client=self._base_client)
        return await projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

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
