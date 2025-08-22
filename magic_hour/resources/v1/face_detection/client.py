import asyncio
import os
import time
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


class FaceDetectionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def check_result(
        self,
        id: str,
        wait_for_completion: bool,
    ) -> models.V1FaceDetectionGetResponse:
        """
        Check the result of a face detection task with optional waiting.

        This method retrieves the status of a face detection task and optionally waits for completion.

        Args:
            id: Unique ID of the face detection task
            wait_for_completion: Whether to wait for the face detection task to complete

        Returns:
            V1FaceDetectionGetResponse: The face detection response
        """
        api_response = self.get(id=id)
        if not wait_for_completion:
            return api_response

        poll_interval = float(os.getenv("MAGIC_HOUR_POLL_INTERVAL", "0.5"))

        # For face detection, we check the status in the response
        # Face detection tasks complete quickly, so we poll until we get results or an error
        while api_response.status not in ["complete", "error"]:
            api_response = self.get(id=id)
            time.sleep(poll_interval)

        return api_response

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

    async def check_result(
        self,
        id: str,
        wait_for_completion: bool,
    ) -> models.V1FaceDetectionGetResponse:
        """
        Check the result of a face detection task with optional waiting.

        This method retrieves the status of a face detection task and optionally waits for completion.

        Args:
            id: Unique ID of the face detection task
            wait_for_completion: Whether to wait for the face detection task to complete

        Returns:
            V1FaceDetectionGetResponse: The face detection response
        """
        api_response = await self.get(id=id)
        if not wait_for_completion:
            return api_response

        poll_interval = float(os.getenv("MAGIC_HOUR_POLL_INTERVAL", "0.5"))

        # For face detection, we check the status in the response
        # Face detection tasks complete quickly, so we poll until we get results or an error
        while api_response.status not in ["complete", "error"]:
            api_response = await self.get(id=id)
            await asyncio.sleep(poll_interval)

        return api_response

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
