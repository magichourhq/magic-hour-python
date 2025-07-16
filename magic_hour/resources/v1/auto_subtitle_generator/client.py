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


class AutoSubtitleGeneratorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.V1AutoSubtitleGeneratorCreateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        style: params.V1AutoSubtitleGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AutoSubtitleGeneratorCreateResponse:
        """
        Auto Subtitle Generator

        Automatically generate subtitles for your video in multiple languages.

        POST /v1/auto-subtitle-generator

        Args:
            name: The name of video
            assets: Provide the assets for auto subtitle generator
            end_seconds: The end time of the input video in seconds
            start_seconds: The start time of the input video in seconds
            style: Style of the subtitle. At least one of `.style.template` or `.style.custom_config` must be provided.
        * If only `.style.template` is provided, default values for the template will be used.
        * If both are provided, the fields in `.style.custom_config` will be used to overwrite the fields in `.style.template`.
        * If only `.style.custom_config` is provided, then all fields in `.style.custom_config` will be used.

        To use custom config only, the following `custom_config` params are required:
        * `.style.custom_config.font`
        * `.style.custom_config.text_color`
        * `.style.custom_config.vertical_position`
        * `.style.custom_config.horizontal_position`

            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.auto_subtitle_generator.create(
            assets={"video_file_path": "api-assets/id/1234.mp4"},
            end_seconds=15.0,
            start_seconds=0.0,
            style={},
            name="Auto Subtitle video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "assets": assets,
                "end_seconds": end_seconds,
                "start_seconds": start_seconds,
                "style": style,
            },
            dump_with=params._SerializerV1AutoSubtitleGeneratorCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/auto-subtitle-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AutoSubtitleGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAutoSubtitleGeneratorClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.V1AutoSubtitleGeneratorCreateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        style: params.V1AutoSubtitleGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AutoSubtitleGeneratorCreateResponse:
        """
        Auto Subtitle Generator

        Automatically generate subtitles for your video in multiple languages.

        POST /v1/auto-subtitle-generator

        Args:
            name: The name of video
            assets: Provide the assets for auto subtitle generator
            end_seconds: The end time of the input video in seconds
            start_seconds: The start time of the input video in seconds
            style: Style of the subtitle. At least one of `.style.template` or `.style.custom_config` must be provided.
        * If only `.style.template` is provided, default values for the template will be used.
        * If both are provided, the fields in `.style.custom_config` will be used to overwrite the fields in `.style.template`.
        * If only `.style.custom_config` is provided, then all fields in `.style.custom_config` will be used.

        To use custom config only, the following `custom_config` params are required:
        * `.style.custom_config.font`
        * `.style.custom_config.text_color`
        * `.style.custom_config.vertical_position`
        * `.style.custom_config.horizontal_position`

            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.auto_subtitle_generator.create(
            assets={"video_file_path": "api-assets/id/1234.mp4"},
            end_seconds=15.0,
            start_seconds=0.0,
            style={},
            name="Auto Subtitle video",
        )
        ```
        """
        _json = to_encodable(
            item={
                "name": name,
                "assets": assets,
                "end_seconds": end_seconds,
                "start_seconds": start_seconds,
                "style": style,
            },
            dump_with=params._SerializerV1AutoSubtitleGeneratorCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/auto-subtitle-generator",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AutoSubtitleGeneratorCreateResponse,
            request_options=request_options or default_request_options(),
        )
