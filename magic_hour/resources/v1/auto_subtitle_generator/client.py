import typing

from magic_hour.helpers.logger import get_sdk_logger
from magic_hour.resources.v1.files.client import AsyncFilesClient, FilesClient
from magic_hour.resources.v1.video_projects.client import (
    AsyncVideoProjectsClient,
    VideoProjectsClient,
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


class AutoSubtitleGeneratorClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1AutoSubtitleGeneratorCreateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        style: params.V1AutoSubtitleGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate subtitled video (alias for create with additional functionality).

        Automatically generate subtitles for your video in multiple languages.

        Args:
            name: The name of video. This value is mainly used for your own identification of the video.
            assets: Provide the assets for auto subtitle generator
            end_seconds: The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
            start_seconds: The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
            style: Style of the subtitle. At least one of `.style.template` or `.style.custom_config` must be provided.
        * If only `.style.template` is provided, default values for the template will be used.
        * If both are provided, the fields in `.style.custom_config` will be used to overwrite the fields in `.style.template`.
        * If only `.style.custom_config` is provided, then all fields in `.style.custom_config` will be used.

        To use custom config only, the following `custom_config` params are required:
        * `.style.custom_config.font`
        * `.style.custom_config.text_color`
        * `.style.custom_config.vertical_position`
        * `.style.custom_config.horizontal_position`

            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Auto Subtitle Generator API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.auto_subtitle_generator.generate(
            assets={"video_file_path": "path/to/video.mp4"},
            end_seconds=15.0,
            start_seconds=0.0,
            style={},
            name="Subtitled Video",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = FilesClient(base_client=self._base_client)

        video_file_path = assets["video_file_path"]
        assets["video_file_path"] = file_client.upload_file(file=video_file_path)

        create_response = self.create(
            assets=assets,
            end_seconds=end_seconds,
            start_seconds=start_seconds,
            style=style,
            name=name,
            request_options=request_options,
        )
        logger.info(f"Auto Subtitle Generator response: {create_response}")

        video_projects_client = VideoProjectsClient(base_client=self._base_client)
        response = video_projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

        return response

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
            name: The name of video. This value is mainly used for your own identification of the video.
            assets: Provide the assets for auto subtitle generator
            end_seconds: The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
            start_seconds: The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
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

    async def generate(
        self,
        *,
        assets: params.V1AutoSubtitleGeneratorCreateBodyAssets,
        end_seconds: float,
        start_seconds: float,
        style: params.V1AutoSubtitleGeneratorCreateBodyStyle,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate subtitled video (alias for create with additional functionality).

        Automatically generate subtitles for your video in multiple languages.

        Args:
            name: The name of video. This value is mainly used for your own identification of the video.
            assets: Provide the assets for auto subtitle generator
            end_seconds: The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
            start_seconds: The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
            style: Style of the subtitle. At least one of `.style.template` or `.style.custom_config` must be provided.
        * If only `.style.template` is provided, default values for the template will be used.
        * If both are provided, the fields in `.style.custom_config` will be used to overwrite the fields in `.style.template`.
        * If only `.style.custom_config` is provided, then all fields in `.style.custom_config` will be used.

        To use custom config only, the following `custom_config` params are required:
        * `.style.custom_config.font`
        * `.style.custom_config.text_color`
        * `.style.custom_config.vertical_position`
        * `.style.custom_config.horizontal_position`

            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Auto Subtitle Generator API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.auto_subtitle_generator.generate(
            assets={"video_file_path": "path/to/video.mp4"},
            end_seconds=15.0,
            start_seconds=0.0,
            style={},
            name="Subtitled Video",
            wait_for_completion=True,
            download_outputs=True,
            download_directory="outputs/",
        )
        ```
        """

        file_client = AsyncFilesClient(base_client=self._base_client)

        video_file_path = assets["video_file_path"]
        assets["video_file_path"] = await file_client.upload_file(file=video_file_path)

        create_response = await self.create(
            assets=assets,
            end_seconds=end_seconds,
            start_seconds=start_seconds,
            style=style,
            name=name,
            request_options=request_options,
        )
        logger.info(f"Auto Subtitle Generator response: {create_response}")

        video_projects_client = AsyncVideoProjectsClient(base_client=self._base_client)
        response = await video_projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

        return response

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
            name: The name of video. This value is mainly used for your own identification of the video.
            assets: Provide the assets for auto subtitle generator
            end_seconds: The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
            start_seconds: The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
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
