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


class CharacterReplaceClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.V1CharacterReplaceCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate character replace video (alias for create with additional functionality).

        Create a Character Replace video. Credits are only charged for the frames that actually render.

        Args:
            data: V1CharacterReplaceCreateBody
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Character Replace API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = client.v1.character_replace.generate(
            data={
                "assets": {
                    "image_file_path": "path/to/image.png",
                    "video_file_path": "path/to/video.mp4",
                },
                "end_seconds": 15.0,
                "name": "My Character Replace video",
                "resolution": "720p",
                "start_seconds": 0.0,
                "style": {"mode": "replace", "selection_mode": "auto"},
            },
            wait_for_completion=True,
            download_outputs=True,
            download_directory=".",
        )
        ```
        """

        if data and "assets" in data:
            file_client = FilesClient(base_client=self._base_client)
            assets = data["assets"]

            image_file_path = assets["image_file_path"]
            video_file_path = assets["video_file_path"]
            assets["image_file_path"] = file_client.upload_file(file=image_file_path)
            assets["video_file_path"] = file_client.upload_file(file=video_file_path)

        create_response = self.create(
            data=data,
            request_options=request_options,
        )
        logger.info(f"Character Replace response: {create_response}")

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
        data: typing.Union[
            typing.Optional[params.V1CharacterReplaceCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1CharacterReplaceCreateResponse:
        """
        Character Replace

        **What this API does**

        Create the same Character Replace you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding character replace into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a character replace job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

        For detailed examples, see the [product page](https://magichour.ai/products/character-replace).

        POST /v1/character-replace

        Args:
            data: V1CharacterReplaceCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.character_replace.create()
        ```
        """
        _json = (
            to_encodable(
                item=data, dump_with=params._SerializerV1CharacterReplaceCreateBody
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/character-replace",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1CharacterReplaceCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncCharacterReplaceClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.V1CharacterReplaceCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Generate character replace video (alias for create with additional functionality).

        Create a Character Replace video. Credits are only charged for the frames that actually render.

        Args:
            data: V1CharacterReplaceCreateBody
            wait_for_completion: Whether to wait for the video project to complete
            download_outputs: Whether to download the outputs
            download_directory: The directory to download the outputs to. If not provided, the outputs will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1VideoProjectsGetResponseWithDownloads: The response from the Character Replace API with the downloaded paths if `download_outputs` is True.

        Examples:
        ```py
        response = await client.v1.character_replace.generate(
            data={
                "assets": {
                    "image_file_path": "path/to/image.png",
                    "video_file_path": "path/to/video.mp4",
                },
                "end_seconds": 15.0,
                "name": "My Character Replace video",
                "resolution": "720p",
                "start_seconds": 0.0,
                "style": {"mode": "replace", "selection_mode": "auto"},
            },
            wait_for_completion=True,
            download_outputs=True,
            download_directory=".",
        )
        ```
        """

        if data and "assets" in data:
            file_client = AsyncFilesClient(base_client=self._base_client)
            assets = data["assets"]

            image_file_path = assets["image_file_path"]
            video_file_path = assets["video_file_path"]
            assets["image_file_path"] = await file_client.upload_file(
                file=image_file_path
            )
            assets["video_file_path"] = await file_client.upload_file(
                file=video_file_path
            )

        create_response = await self.create(
            data=data,
            request_options=request_options,
        )
        logger.info(f"Character Replace response: {create_response}")

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
        data: typing.Union[
            typing.Optional[params.V1CharacterReplaceCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1CharacterReplaceCreateResponse:
        """
        Character Replace

        **What this API does**

        Create the same Character Replace you can make in the browser, but programmatically, so you can automate it, run it at scale, or connect it to your own app or workflow.

        **Good for**
        - Automation and batch processing
        - Adding character replace into apps, pipelines, or tools

        **How it works (3 steps)**
        1) Upload your inputs (video, image, or audio) with [Generate Upload URLs](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls) and copy the `file_path`.
        2) Send a request to create a character replace job with the basic fields.
        3) Check the job status until it's `complete`, then download the result from `downloads`.

        **Key options**
        - Inputs: usually a file, sometimes a YouTube link, depending on project type
        - Resolution: free users are limited to 576px; higher plans unlock HD and larger sizes
        - Extra fields: e.g. `face_swap_mode`, `start_seconds`/`end_seconds`, or a text prompt

        **Cost**
        Credits are only charged for the frames that actually render. You'll see an estimate when the job is queued, and the final total after it's done.

        For detailed examples, see the [product page](https://magichour.ai/products/character-replace).

        POST /v1/character-replace

        Args:
            data: V1CharacterReplaceCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.character_replace.create()
        ```
        """
        _json = (
            to_encodable(
                item=data, dump_with=params._SerializerV1CharacterReplaceCreateBody
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/character-replace",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1CharacterReplaceCreateResponse,
            request_options=request_options or default_request_options(),
        )
