import asyncio
import os
import pydantic
import time
import typing

from magic_hour.helpers.download import download_files_async, download_files_sync
from magic_hour.helpers.logger import get_sdk_logger
from magic_hour.resources.v1.files import AsyncFilesClient, FilesClient
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


class V1FaceDetectionGetResponseWithDownloads(models.V1FaceDetectionGetResponse):
    downloaded_paths: typing.Optional[typing.List[str]] = pydantic.Field(
        default=None, alias="downloaded_paths"
    )
    """
    The paths to the downloaded face images.

    This field is only populated if `download_outputs` is True and the face detection is complete.
    """


class FaceDetectionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate(
        self,
        *,
        assets: params.V1FaceDetectionCreateBodyAssets,
        confidence_score: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1FaceDetectionGetResponseWithDownloads:
        """
        Generate face detection results with optional waiting and downloading.

        This method creates a face detection task and optionally waits for completion
        and downloads the detected face images.

        Args:
            assets: Provide the assets for face detection
            confidence_score: Confidence threshold for filtering detected faces
            wait_for_completion: Whether to wait for the face detection task to complete
            download_outputs: Whether to download the detected face images
            download_directory: The directory to download the face images to. If not provided,
                the images will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1FaceDetectionGetResponseWithDownloads: The face detection response with optional
                downloaded face image paths included
        """
        # Handle file upload if needed
        file_client = FilesClient(base_client=self._base_client)
        target_file_path = assets["target_file_path"]
        assets["target_file_path"] = file_client.upload_file(file=target_file_path)

        create_response = self.create(
            assets=assets,
            confidence_score=confidence_score,
            request_options=request_options,
        )

        task_id = create_response.id

        api_response = self.get(id=task_id)
        if not wait_for_completion:
            return V1FaceDetectionGetResponseWithDownloads(**api_response.model_dump())

        poll_interval = float(os.getenv("MAGIC_HOUR_POLL_INTERVAL", "0.5"))

        while api_response.status not in ["complete", "error"]:
            api_response = self.get(id=task_id)
            time.sleep(poll_interval)

        if api_response.status != "complete":
            log = logger.error if api_response.status == "error" else logger.info
            log(f"Face detection {task_id} has status {api_response.status}")
            return V1FaceDetectionGetResponseWithDownloads(**api_response.model_dump())

        if not download_outputs or not api_response.faces:
            return V1FaceDetectionGetResponseWithDownloads(**api_response.model_dump())

        face_downloads = [
            models.V1ImageProjectsGetResponseDownloadsItem(
                url=face.url,
                expires_at="ignore",
            )
            for face in api_response.faces
        ]
        downloaded_paths = download_files_sync(
            downloads=face_downloads,
            download_directory=download_directory,
        )

        return V1FaceDetectionGetResponseWithDownloads(
            **api_response.model_dump(), downloaded_paths=downloaded_paths
        )

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.V1FaceDetectionGetResponse:
        """
        Get face detection details

        Get the details of a face detection task.

        Use this API to get the list of faces detected in the image or video to use in the [face swap photo](/api-reference/face-swap-photo/face-swap-photo) or [face swap video](/api-reference/face-swap/face-swap-video) API calls for multi-face swaps.

        GET /v1/face-detection/{id}

        Args:
            id: The id of the task. This value is returned by the [face detection API](/api-reference/files/face-detection#response-id).
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.face_detection.get(id="uuid-example")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v1/face-detection/{id}",
            auth_names=["bearerAuth"],
            cast_to=models.V1FaceDetectionGetResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        assets: params.V1FaceDetectionCreateBodyAssets,
        confidence_score: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1FaceDetectionCreateResponse:
        """
        Face Detection

        Detect faces in an image or video.

        Use this API to get the list of faces detected in the image or video to use in the [face swap photo](/api-reference/face-swap-photo/face-swap-photo) or [face swap video](/api-reference/face-swap/face-swap-video) API calls for multi-face swaps.

        Note: Face detection is free to use for the near future. Pricing may change in the future.

        POST /v1/face-detection

        Args:
            confidence_score: Confidence threshold for filtering detected faces.
        * Higher values (e.g., 0.9) include only faces detected with high certainty, reducing false positives.
        * Lower values (e.g., 0.3) include more faces, but may increase the chance of incorrect detections.
            assets: Provide the assets for face detection
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.face_detection.create(
            assets={"target_file_path": "api-assets/id/1234.png"}, confidence_score=0.5
        )
        ```
        """
        _json = to_encodable(
            item={"confidence_score": confidence_score, "assets": assets},
            dump_with=params._SerializerV1FaceDetectionCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/face-detection",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1FaceDetectionCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncFaceDetectionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate(
        self,
        *,
        assets: params.V1FaceDetectionCreateBodyAssets,
        confidence_score: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        wait_for_completion: bool = True,
        download_outputs: bool = True,
        download_directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1FaceDetectionGetResponseWithDownloads:
        """
        Generate face detection results with optional waiting and downloading.

        This method creates a face detection task and optionally waits for completion
        and downloads the detected face images.

        Args:
            assets: Provide the assets for face detection
            confidence_score: Confidence threshold for filtering detected faces
            wait_for_completion: Whether to wait for the face detection task to complete
            download_outputs: Whether to download the detected face images
            download_directory: The directory to download the face images to. If not provided,
                the images will be downloaded to the current working directory
            request_options: Additional options to customize the HTTP request

        Returns:
            V1FaceDetectionGetResponseWithDownloads: The face detection response with optional
                downloaded face image paths included
        """
        # Handle file upload if needed
        file_client = AsyncFilesClient(base_client=self._base_client)
        target_file_path = assets["target_file_path"]
        assets["target_file_path"] = await file_client.upload_file(
            file=target_file_path
        )

        create_response = await self.create(
            assets=assets,
            confidence_score=confidence_score,
            request_options=request_options,
        )

        task_id = create_response.id

        api_response = await self.get(id=task_id)
        if not wait_for_completion:
            return V1FaceDetectionGetResponseWithDownloads(**api_response.model_dump())

        poll_interval = float(os.getenv("MAGIC_HOUR_POLL_INTERVAL", "0.5"))

        while api_response.status not in ["complete", "error"]:
            api_response = await self.get(id=task_id)
            await asyncio.sleep(poll_interval)

        if api_response.status != "complete":
            log = logger.error if api_response.status == "error" else logger.info
            log(f"Face detection {task_id} has status {api_response.status}")
            return V1FaceDetectionGetResponseWithDownloads(**api_response.model_dump())

        if not download_outputs or not api_response.faces:
            return V1FaceDetectionGetResponseWithDownloads(**api_response.model_dump())

        face_downloads = [
            models.V1ImageProjectsGetResponseDownloadsItem(
                url=face.url,
                expires_at="ignore",
            )
            for face in api_response.faces
        ]
        downloaded_paths = await download_files_async(
            downloads=face_downloads,
            download_directory=download_directory,
        )

        return V1FaceDetectionGetResponseWithDownloads(
            **api_response.model_dump(), downloaded_paths=downloaded_paths
        )

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.V1FaceDetectionGetResponse:
        """
        Get face detection details

        Get the details of a face detection task.

        Use this API to get the list of faces detected in the image or video to use in the [face swap photo](/api-reference/face-swap-photo/face-swap-photo) or [face swap video](/api-reference/face-swap/face-swap-video) API calls for multi-face swaps.

        GET /v1/face-detection/{id}

        Args:
            id: The id of the task. This value is returned by the [face detection API](/api-reference/files/face-detection#response-id).
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.face_detection.get(id="uuid-example")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v1/face-detection/{id}",
            auth_names=["bearerAuth"],
            cast_to=models.V1FaceDetectionGetResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        assets: params.V1FaceDetectionCreateBodyAssets,
        confidence_score: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1FaceDetectionCreateResponse:
        """
        Face Detection

        Detect faces in an image or video.

        Use this API to get the list of faces detected in the image or video to use in the [face swap photo](/api-reference/face-swap-photo/face-swap-photo) or [face swap video](/api-reference/face-swap/face-swap-video) API calls for multi-face swaps.

        Note: Face detection is free to use for the near future. Pricing may change in the future.

        POST /v1/face-detection

        Args:
            confidence_score: Confidence threshold for filtering detected faces.
        * Higher values (e.g., 0.9) include only faces detected with high certainty, reducing false positives.
        * Lower values (e.g., 0.3) include more faces, but may increase the chance of incorrect detections.
            assets: Provide the assets for face detection
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.face_detection.create(
            assets={"target_file_path": "api-assets/id/1234.png"}, confidence_score=0.5
        )
        ```
        """
        _json = to_encodable(
            item={"confidence_score": confidence_score, "assets": assets},
            dump_with=params._SerializerV1FaceDetectionCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/face-detection",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1FaceDetectionCreateResponse,
            request_options=request_options or default_request_options(),
        )
