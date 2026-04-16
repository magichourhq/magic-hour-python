import typing
import typing_extensions

from magic_hour.helpers.logger import get_sdk_logger
from magic_hour.resources.v1.files.client import AsyncFilesClient, FilesClient
from magic_hour.resources.v1.image_projects.client import (
    AsyncImageProjectsClient,
    ImageProjectsClient,
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


class BodySwapClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1BodySwapCreateBodyAssets,
        resolution: typing_extensions.Literal["1k", "2k", "4k", "640px"],
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate body swap image (alias for create with additional functionality).

        Swap a person into a scene image using Nano Banana 2. Credits depend on `resolution` (from 100 credits at 640px upward).

        Args:
            name: Give your image a custom name for easy identification.
            assets: Person image and scene image for body swap
            resolution: Output resolution. Determines credits charged for the run.
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the Body Swap API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        client.v1.body_swap.generate(
            assets={
                "person_file_path": "path/to/person.png",
                "scene_file_path": "path/to/scene.png",
            },
            resolution="1k",
            name="My Body Swap image",
            wait_for_completion=True,
            download_outputs=True,
            download_directory=".",
        )
        ```
        """

        file_client = FilesClient(base_client=self._base_client)

        person_file_path = assets["person_file_path"]
        scene_file_path = assets["scene_file_path"]
        assets["person_file_path"] = file_client.upload_file(file=person_file_path)
        assets["scene_file_path"] = file_client.upload_file(file=scene_file_path)

        create_response = self.create(
            assets=assets,
            resolution=resolution,
            name=name,
            request_options=request_options,
        )
        logger.info(f"Body Swap response: {create_response}")

        image_projects_client = ImageProjectsClient(base_client=self._base_client)
        response = image_projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

        return response

    def create(
        self,
        *,
        assets: params.V1BodySwapCreateBodyAssets,
        resolution: typing_extensions.Literal["1k", "2k", "4k", "640px"],
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1BodySwapCreateResponse:
        """
        Body Swap

        Swap a person into a scene image using Nano Banana 2. Credits depend on `resolution` (from 100 credits at 640px upward).

        POST /v1/body-swap

        Args:
            name: Give your image a custom name for easy identification.
            assets: Person image and scene image for body swap
            resolution: Output resolution. Determines credits charged for the run.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.body_swap.create(
            assets={
                "person_file_path": "api-assets/id/1234.png",
                "scene_file_path": "api-assets/id/5678.png",
            },
            resolution="1k",
            name="My Body Swap image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets, "resolution": resolution},
            dump_with=params._SerializerV1BodySwapCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/body-swap",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1BodySwapCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncBodySwapClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        assets: params.V1BodySwapCreateBodyAssets,
        resolution: typing_extensions.Literal["1k", "2k", "4k", "640px"],
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate body swap image (alias for create with additional functionality).

        Swap a person into a scene image using Nano Banana 2. Credits depend on `resolution` (from 100 credits at 640px upward).

        Args:
            name: Give your image a custom name for easy identification.
            assets: Person image and scene image for body swap
            resolution: Output resolution. Determines credits charged for the run.
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the Body Swap API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        await client.v1.body_swap.generate(
            assets={
                "person_file_path": "path/to/person.png",
                "scene_file_path": "path/to/scene.png",
            },
            resolution="1k",
            name="My Body Swap image",
            wait_for_completion=True,
            download_outputs=True,
            download_directory=".",
        )
        ```
        """

        file_client = AsyncFilesClient(base_client=self._base_client)

        person_file_path = assets["person_file_path"]
        scene_file_path = assets["scene_file_path"]
        assets["person_file_path"] = await file_client.upload_file(
            file=person_file_path
        )
        assets["scene_file_path"] = await file_client.upload_file(
            file=scene_file_path
        )

        create_response = await self.create(
            assets=assets,
            resolution=resolution,
            name=name,
            request_options=request_options,
        )
        logger.info(f"Body Swap response: {create_response}")

        image_projects_client = AsyncImageProjectsClient(base_client=self._base_client)
        response = await image_projects_client.check_result(
            id=create_response.id,
            wait_for_completion=wait_for_completion,
            download_outputs=download_outputs,
            download_directory=download_directory,
        )

        return response

    async def create(
        self,
        *,
        assets: params.V1BodySwapCreateBodyAssets,
        resolution: typing_extensions.Literal["1k", "2k", "4k", "640px"],
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1BodySwapCreateResponse:
        """
        Body Swap

        Swap a person into a scene image using Nano Banana 2. Credits depend on `resolution` (from 100 credits at 640px upward).

        POST /v1/body-swap

        Args:
            name: Give your image a custom name for easy identification.
            assets: Person image and scene image for body swap
            resolution: Output resolution. Determines credits charged for the run.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.body_swap.create(
            assets={
                "person_file_path": "api-assets/id/1234.png",
                "scene_file_path": "api-assets/id/5678.png",
            },
            resolution="1k",
            name="My Body Swap image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets, "resolution": resolution},
            dump_with=params._SerializerV1BodySwapCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/body-swap",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1BodySwapCreateResponse,
            request_options=request_options or default_request_options(),
        )
