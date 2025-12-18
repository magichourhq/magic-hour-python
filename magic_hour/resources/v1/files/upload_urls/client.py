import typing

from magic_hour.types import models, params
from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)


class UploadUrlsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        items: typing.List[params.V1FilesUploadUrlsCreateBodyItemsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1FilesUploadUrlsCreateResponse:
        """
        Generate asset upload urls
        
        Generates a list of pre-signed upload URLs for the assets required. This API is only necessary if you want to upload to Magic Hour's storage. Refer to the [Input Files Guide](/integration/input-files) for more details.
        
        The response array will match the order of items in the request body.
        
        **Valid file extensions per asset type**:
        - video: mp4, m4v, mov, webm
        - audio: mp3, wav, aac, flac, webm
        - image: png, jpg, jpeg, heic, webp, avif, jp2, tiff, bmp
        - gif: gif, webp, webm
        
        > Note: `gif` is only supported for face swap API `video_file_path` field.
        
        Once you receive an upload URL, send a `PUT` request to upload the file directly.
        
        Example:
        
        ```
        curl -X PUT --data '@/path/to/file/video.mp4' \
          https://videos.magichour.ai/api-assets/id/video.mp4?<auth params from the API response>
        ```
        
        
        POST /v1/files/upload-urls
        
        Args:
            items: The list of assets to upload. The response array will match the order of items in the request body.
            request_options: Additional options to customize the HTTP request
        
        Returns:
            Success   
        
        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.
        
        Examples:
        ```py
        client.v1.files.upload_urls.create(items=[{"extension": "mp4", "type_": "video"}, {"extension": "mp3", "type_": "audio"}])
        ```
        """
        _json = to_encodable(
            item={"items": items},
            dump_with=params._SerializerV1FilesUploadUrlsCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/files/upload-urls",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1FilesUploadUrlsCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncUploadUrlsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        items: typing.List[params.V1FilesUploadUrlsCreateBodyItemsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1FilesUploadUrlsCreateResponse:
        """
        Generate asset upload urls
        
        Generates a list of pre-signed upload URLs for the assets required. This API is only necessary if you want to upload to Magic Hour's storage. Refer to the [Input Files Guide](/integration/input-files) for more details.
        
        The response array will match the order of items in the request body.
        
        **Valid file extensions per asset type**:
        - video: mp4, m4v, mov, webm
        - audio: mp3, wav, aac, flac, webm
        - image: png, jpg, jpeg, heic, webp, avif, jp2, tiff, bmp
        - gif: gif, webp, webm
        
        > Note: `gif` is only supported for face swap API `video_file_path` field.
        
        Once you receive an upload URL, send a `PUT` request to upload the file directly.
        
        Example:
        
        ```
        curl -X PUT --data '@/path/to/file/video.mp4' \
          https://videos.magichour.ai/api-assets/id/video.mp4?<auth params from the API response>
        ```
        
        
        POST /v1/files/upload-urls
        
        Args:
            items: The list of assets to upload. The response array will match the order of items in the request body.
            request_options: Additional options to customize the HTTP request
        
        Returns:
            Success   
        
        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.
        
        Examples:
        ```py
        await client.v1.files.upload_urls.create(items=[{"extension": "mp4", "type_": "video"}, {"extension": "mp3", "type_": "audio"}])
        ```
        """
        _json = to_encodable(
            item={"items": items},
            dump_with=params._SerializerV1FilesUploadUrlsCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/files/upload-urls",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1FilesUploadUrlsCreateResponse,
            request_options=request_options or default_request_options(),
        )
