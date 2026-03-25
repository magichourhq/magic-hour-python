import typing

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


class HeadSwapClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1HeadSwapGenerateBodyAssets,
        max_resolution: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate head swap (alias for create with additional functionality).

        Swap a head onto a body image. Each image costs 10 credits. Output resolution depends on your subscription; you may set `max_resolution` lower than your plan maximum if desired.

        Args:
            max_resolution: Constrains the larger dimension (height or width) of the output. Omit to use the maximum allowed for your plan (capped at 2048px). Values above your plan maximum are clamped down to your plan's maximum.
            name: Give your image a custom name for easy identification.
            assets: Provide the body and head images for head swap
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the Head Swap API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        client.v1.head_swap.generate(
            assets={
                "body_file_path": "/path/to/body.png",
                "head_file_path": "/path/to/head.png",
            },
            max_resolution=1024,
            name="My Head Swap image",
            wait_for_completion=True,
            download_outputs=True,
            download_directory=".",
        )
        ```
        """

        file_client = FilesClient(base_client=self._base_client)

        body_file_path = assets["body_file_path"]
        assets["body_file_path"] = file_client.upload_file(file=body_file_path)

        head_file_path = assets["head_file_path"]
        assets["head_file_path"] = file_client.upload_file(file=head_file_path)

        create_response = self.create(
            assets=assets,
            max_resolution=max_resolution,
            name=name,
            request_options=request_options,
        )
        logger.info(f"Head Swap response: {create_response}")

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
        assets: params.V1HeadSwapCreateBodyAssets,
        max_resolution: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1HeadSwapCreateResponse:
        """
        Head Swap

        Swap a head onto a body image. Each image costs 10 credits. Output resolution depends on your subscription; you may set `max_resolution` lower than your plan maximum if desired.

        POST /v1/head-swap

        Args:
            max_resolution: Constrains the larger dimension (height or width) of the output. Omit to use the maximum allowed for your plan (capped at 2048px). Values above your plan maximum are clamped down to your plan's maximum.
            name: Give your image a custom name for easy identification.
            assets: Provide the body and head images for head swap
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.head_swap.create(
            assets={
                "body_file_path": "api-assets/id/1234.png",
                "head_file_path": "api-assets/id/5678.png",
            },
            max_resolution=1024,
            name="My Head Swap image",
        )
        ```
        """
        _json = to_encodable(
            item={"max_resolution": max_resolution, "name": name, "assets": assets},
            dump_with=params._SerializerV1HeadSwapCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/head-swap",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1HeadSwapCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncHeadSwapClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        assets: params.V1HeadSwapGenerateBodyAssets,
        max_resolution: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate head swap (alias for create with additional functionality).

        Swap a head onto a body image. Each image costs 10 credits. Output resolution depends on your subscription; you may set `max_resolution` lower than your plan maximum if desired.

        Args:
            max_resolution: Constrains the larger dimension (height or width) of the output. Omit to use the maximum allowed for your plan (capped at 2048px). Values above your plan maximum are clamped down to your plan's maximum.
            name: Give your image a custom name for easy identification.
            assets: Provide the body and head images for head swap
            wait_for_completion: Whether to wait for the image project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1ImageProjectsGetResponseWithDownloads: The response from the Head Swap API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        await client.v1.head_swap.generate(
            assets={
                "body_file_path": "/path/to/body.png",
                "head_file_path": "/path/to/head.png",
            },
            max_resolution=1024,
            name="My Head Swap image",
            wait_for_completion=True,
            download_outputs=True,
            download_directory=".",
        )
        ```
        """

        file_client = AsyncFilesClient(base_client=self._base_client)

        body_file_path = assets["body_file_path"]
        assets["body_file_path"] = await file_client.upload_file(file=body_file_path)

        head_file_path = assets["head_file_path"]
        assets["head_file_path"] = await file_client.upload_file(file=head_file_path)

        create_response = await self.create(
            assets=assets,
            max_resolution=max_resolution,
            name=name,
            request_options=request_options,
        )
        logger.info(f"Head Swap response: {create_response}")

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
        assets: params.V1HeadSwapCreateBodyAssets,
        max_resolution: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1HeadSwapCreateResponse:
        """
        Head Swap

        Swap a head onto a body image. Each image costs 10 credits. Output resolution depends on your subscription; you may set `max_resolution` lower than your plan maximum if desired.

        POST /v1/head-swap

        Args:
            max_resolution: Constrains the larger dimension (height or width) of the output. Omit to use the maximum allowed for your plan (capped at 2048px). Values above your plan maximum are clamped down to your plan's maximum.
            name: Give your image a custom name for easy identification.
            assets: Provide the body and head images for head swap
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.head_swap.create(
            assets={
                "body_file_path": "api-assets/id/1234.png",
                "head_file_path": "api-assets/id/5678.png",
            },
            max_resolution=1024,
            name="My Head Swap image",
        )
        ```
        """
        _json = to_encodable(
            item={"max_resolution": max_resolution, "name": name, "assets": assets},
            dump_with=params._SerializerV1HeadSwapCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/head-swap",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1HeadSwapCreateResponse,
            request_options=request_options or default_request_options(),
        )
