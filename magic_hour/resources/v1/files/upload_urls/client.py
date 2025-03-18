import typing

from magic_hour.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)
from magic_hour.types import models, params


class UploadUrlsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        items: typing.List[params.PostV1FilesUploadUrlsBodyItemsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1FilesUploadUrlsResponse:
        """
        Generate asset upload urls
        
        Create a list of urls used to upload the assets needed to generate a video. Each video type has their own requirements on what assets are required. Please refer to the specific mode API for more details. The response array will be in the same order as the request body.
        
        Below is the list of valid extensions for each asset type:
        
        - video: mp4, m4v, mov, webm
        - audio: mp3, mpeg, wav, aac, aiff, flac
        - image: png, jpg, jpeg, webp, avif, jp2, tiff, bmp
        
        Note: `.gif` is supported for face swap API `video_file_path` field.
        
        After receiving the upload url, you can upload the file by sending a PUT request with the header `'Content-Type: application/octet-stream'`.
        
        For example using curl
        
        ```
        curl -X PUT -H 'Content-Type: application/octet-stream' \
          --data '@/path/to/file/video.mp4' \
          https://videos.magichour.ai/api-assets/id/video.mp4?auth-value=1234567890
        ```
        
        
        POST /v1/files/upload-urls
        
        Args:
            items: typing.List[PostV1FilesUploadUrlsBodyItemsItem]
            request_options: Additional options to customize the HTTP request
        
        Returns:
            Success   
        
        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.
        
        Examples:
        ```py
        client.v1.files.upload_urls.create(items=[{"extension": "mp4", "type_field": "video"}, {"extension": "mp3", "type_field": "audio"}])
        ```
        """
        _json = to_encodable(
            item={"items": items}, dump_with=params._SerializerPostV1FilesUploadUrlsBody
        )
        return self._base_client.request(
            method="POST",
            path="/v1/files/upload-urls",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1FilesUploadUrlsResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncUploadUrlsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        items: typing.List[params.PostV1FilesUploadUrlsBodyItemsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostV1FilesUploadUrlsResponse:
        """
        Generate asset upload urls
        
        Create a list of urls used to upload the assets needed to generate a video. Each video type has their own requirements on what assets are required. Please refer to the specific mode API for more details. The response array will be in the same order as the request body.
        
        Below is the list of valid extensions for each asset type:
        
        - video: mp4, m4v, mov, webm
        - audio: mp3, mpeg, wav, aac, aiff, flac
        - image: png, jpg, jpeg, webp, avif, jp2, tiff, bmp
        
        Note: `.gif` is supported for face swap API `video_file_path` field.
        
        After receiving the upload url, you can upload the file by sending a PUT request with the header `'Content-Type: application/octet-stream'`.
        
        For example using curl
        
        ```
        curl -X PUT -H 'Content-Type: application/octet-stream' \
          --data '@/path/to/file/video.mp4' \
          https://videos.magichour.ai/api-assets/id/video.mp4?auth-value=1234567890
        ```
        
        
        POST /v1/files/upload-urls
        
        Args:
            items: typing.List[PostV1FilesUploadUrlsBodyItemsItem]
            request_options: Additional options to customize the HTTP request
        
        Returns:
            Success   
        
        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.
        
        Examples:
        ```py
        await client.v1.files.upload_urls.create(items=[{"extension": "mp4", "type_field": "video"}, {"extension": "mp3", "type_field": "audio"}])
        ```
        """
        _json = to_encodable(
            item={"items": items}, dump_with=params._SerializerPostV1FilesUploadUrlsBody
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/files/upload-urls",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.PostV1FilesUploadUrlsResponse,
            request_options=request_options or default_request_options(),
        )
