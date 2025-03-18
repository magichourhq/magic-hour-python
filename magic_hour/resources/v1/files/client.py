from magic_hour.core import AsyncBaseClient, SyncBaseClient
from magic_hour.resources.v1.files.upload_urls import (
    AsyncUploadUrlsClient,
    UploadUrlsClient,
)


class FilesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.upload_urls = UploadUrlsClient(base_client=self._base_client)


class AsyncFilesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.upload_urls = AsyncUploadUrlsClient(base_client=self._base_client)
