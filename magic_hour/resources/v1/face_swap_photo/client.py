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


class FaceSwapPhotoClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        assets: params.PostV1FaceSwapPhotoBodyAssets,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1FaceSwapPhotoResponse:
        """
        Face Swap Photo

        Create a face swap photo. Each photo costs 5 frames. The height/width of the output image depends on your subscription. Please refer to our [pricing](/pricing) page for more details

        POST /v1/face-swap-photo

        Args:
            name: The name of image
            assets: Provide the assets for face swap photo
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.face_swap_photo.create(
            assets={
                "source_file_path": "api-assets/id/1234.png",
                "target_file_path": "api-assets/id/1234.png",
            },
            name="Face Swap image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets},
            dump_with=params._SerializerPostV1FaceSwapPhotoBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/face-swap-photo",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1FaceSwapPhotoResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncFaceSwapPhotoClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        assets: params.PostV1FaceSwapPhotoBodyAssets,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1FaceSwapPhotoResponse:
        """
        Face Swap Photo

        Create a face swap photo. Each photo costs 5 frames. The height/width of the output image depends on your subscription. Please refer to our [pricing](/pricing) page for more details

        POST /v1/face-swap-photo

        Args:
            name: The name of image
            assets: Provide the assets for face swap photo
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.face_swap_photo.create(
            assets={
                "source_file_path": "api-assets/id/1234.png",
                "target_file_path": "api-assets/id/1234.png",
            },
            name="Face Swap image",
        )
        ```
        """
        _json = to_encodable(
            item={"name": name, "assets": assets},
            dump_with=params._SerializerPostV1FaceSwapPhotoBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/face-swap-photo",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1FaceSwapPhotoResponse,
            request_options=request_options or default_request_options(),
        )
