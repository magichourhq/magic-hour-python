import typing
import typing_extensions

from magic_hour.helpers.logger import get_sdk_logger
from magic_hour.resources.v1.files.client import AsyncFilesClient, FilesClient
from magic_hour.resources.v1.video_projects.client import (
    AsyncVideoProjectsClient,
    V1VideoProjectsGetResponseWithDownloads,
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


class AiUgcAdClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1AiUgcAdGenerateBodyAssets,
        end_seconds: float,
        script: str,
        additional_properties: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        model: typing.Union[
            typing.Optional[
                typing_extensions.Literal["kling-3.0", "ltx-2.5", "veo3.1"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1VideoProjectsGetResponseWithDownloads:
        """
        Generate a UGC ad with automatic image upload, polling, and downloads.

        Accepts the same parameters as create(). The image may be a local path,
        URL, or an existing api-assets path. The prepared image is animated
        using the supplied script, model, resolution, and duration.

        Args:
            assets: Prepared image to animate.
            end_seconds: Video duration in seconds, subject to the model's limits.
            script: The words the actor should speak.
            additional_properties: Additional properties to include in the request.
            model: Generation model. Defaults depend on your plan.
            resolution: Output resolution. Defaults depend on your plan.
            wait_for_completion: Whether to wait for the video project to complete.
            download_outputs: Whether to download completed outputs.
            download_directory: Output directory, or the current directory if omitted.
            request_options: Additional options to customize the create request.

        Returns:
            The video project with downloaded paths when downloads are enabled.

        Examples:
        ```py
        response = client.v1.ai_ugc_ad.generate(
            assets={"image_file_path": "path/to/image.jpg"},
            end_seconds=4.0,
            script="Meet your new everyday essential.",
        )
        ```
        """
        file_client = FilesClient(base_client=self._base_client)
        uploaded_image = file_client.upload_file(file=assets["image_file_path"])
        create_response = self.create(
            assets={**assets, "image_file_path": uploaded_image},
            end_seconds=end_seconds,
            script=script,
            additional_properties=additional_properties,
            model=model,
            resolution=resolution,
            request_options=request_options,
        )
        logger.info(f"AI UGC Ad response: {create_response}")

        video_projects_client = VideoProjectsClient(base_client=self._base_client)
        return video_projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

    def create(
        self,
        *,
        assets: params.V1AiUgcAdCreateBodyAssets,
        end_seconds: float,
        script: str,
        additional_properties: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        model: typing.Union[
            typing.Optional[
                typing_extensions.Literal["kling-3.0", "ltx-2.5", "veo3.1"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiUgcAdCreateResponse:
        """
        AI UGC Ad Generator

        Create a spoken UGC video from a prepared image and script. Returns a project ID; poll GET /v1/video-projects/{id} for status and downloads. To compose an image, generate the image separately with the Image Editor API and supply its download URL.

        POST /v1/ai-ugc-ad

        Args:
            additional_properties: typing.Dict[str, typing.Any]
            model: Defaults to kling-3.0 on paid plans and ltx-2.5 on free plans.
            resolution: Defaults to 720p on paid plans and 480p on free plans. Unsupported model/resolution combinations and resolutions unavailable for your plan are rejected.
            assets: V1AiUgcAdCreateBodyAssets
            end_seconds: Video duration in seconds. Supported values by model:
        * kling-3.0: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 seconds.
        * ltx-2.5: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60 seconds.
        * veo3.1: 4, 6, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99, 106, 113, 120, 127, 134, 141 seconds.
        Free plans are limited to 5 seconds unless a credit pack has been purchased.
            script: The words the actor should speak. Character limits apply after trimming:
        * kling-3.0: 2500 characters.
        * ltx-2.5: 1804 characters.
        * veo3.1: 2500 characters.
        LTX's dialogue wrapper counts toward its model prompt limit.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.ai_ugc_ad.create(
            assets={"image_file_path": "api-assets/id/image.jpg"},
            end_seconds=4.0,
            script="Meet your new everyday essential.",
        )
        ```
        """
        _json = to_encodable(
            item={
                **(additional_properties or {}),
                "model": model,
                "resolution": resolution,
                "assets": assets,
                "end_seconds": end_seconds,
                "script": script,
            },
            dump_with=params._SerializerV1AiUgcAdCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ai-ugc-ad",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiUgcAdCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAiUgcAdClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        assets: params.V1AiUgcAdGenerateBodyAssets,
        end_seconds: float,
        script: str,
        additional_properties: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        model: typing.Union[
            typing.Optional[
                typing_extensions.Literal["kling-3.0", "ltx-2.5", "veo3.1"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1VideoProjectsGetResponseWithDownloads:
        """
        Generate a UGC ad with automatic image upload, polling, and downloads.

        Accepts the same parameters as create(). The image may be a local path,
        URL, or an existing api-assets path. The prepared image is animated
        using the supplied script, model, resolution, and duration.

        Args:
            assets: Prepared image to animate.
            end_seconds: Video duration in seconds, subject to the model's limits.
            script: The words the actor should speak.
            additional_properties: Additional properties to include in the request.
            model: Generation model. Defaults depend on your plan.
            resolution: Output resolution. Defaults depend on your plan.
            wait_for_completion: Whether to wait for the video project to complete.
            download_outputs: Whether to download completed outputs.
            download_directory: Output directory, or the current directory if omitted.
            request_options: Additional options to customize the create request.

        Returns:
            The video project with downloaded paths when downloads are enabled.

        Examples:
        ```py
        response = await client.v1.ai_ugc_ad.generate(
            assets={"image_file_path": "path/to/image.jpg"},
            end_seconds=4.0,
            script="Meet your new everyday essential.",
        )
        ```
        """
        file_client = AsyncFilesClient(base_client=self._base_client)
        uploaded_image = await file_client.upload_file(file=assets["image_file_path"])
        create_response = await self.create(
            assets={**assets, "image_file_path": uploaded_image},
            end_seconds=end_seconds,
            script=script,
            additional_properties=additional_properties,
            model=model,
            resolution=resolution,
            request_options=request_options,
        )
        logger.info(f"AI UGC Ad response: {create_response}")

        video_projects_client = AsyncVideoProjectsClient(base_client=self._base_client)
        return await video_projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

    async def create(
        self,
        *,
        assets: params.V1AiUgcAdCreateBodyAssets,
        end_seconds: float,
        script: str,
        additional_properties: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        model: typing.Union[
            typing.Optional[
                typing_extensions.Literal["kling-3.0", "ltx-2.5", "veo3.1"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AiUgcAdCreateResponse:
        """
        AI UGC Ad Generator

        Create a spoken UGC video from a prepared image and script. Returns a project ID; poll GET /v1/video-projects/{id} for status and downloads. To compose an image, generate the image separately with the Image Editor API and supply its download URL.

        POST /v1/ai-ugc-ad

        Args:
            additional_properties: typing.Dict[str, typing.Any]
            model: Defaults to kling-3.0 on paid plans and ltx-2.5 on free plans.
            resolution: Defaults to 720p on paid plans and 480p on free plans. Unsupported model/resolution combinations and resolutions unavailable for your plan are rejected.
            assets: V1AiUgcAdCreateBodyAssets
            end_seconds: Video duration in seconds. Supported values by model:
        * kling-3.0: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 seconds.
        * ltx-2.5: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60 seconds.
        * veo3.1: 4, 6, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99, 106, 113, 120, 127, 134, 141 seconds.
        Free plans are limited to 5 seconds unless a credit pack has been purchased.
            script: The words the actor should speak. Character limits apply after trimming:
        * kling-3.0: 2500 characters.
        * ltx-2.5: 1804 characters.
        * veo3.1: 2500 characters.
        LTX's dialogue wrapper counts toward its model prompt limit.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.ai_ugc_ad.create(
            assets={"image_file_path": "api-assets/id/image.jpg"},
            end_seconds=4.0,
            script="Meet your new everyday essential.",
        )
        ```
        """
        _json = to_encodable(
            item={
                **(additional_properties or {}),
                "model": model,
                "resolution": resolution,
                "assets": assets,
                "end_seconds": end_seconds,
                "script": script,
            },
            dump_with=params._SerializerV1AiUgcAdCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ai-ugc-ad",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AiUgcAdCreateResponse,
            request_options=request_options or default_request_options(),
        )
