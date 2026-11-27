from magic_hour.resources.v1.estimate.image import AsyncImageClient, ImageClient
from make_api_request import AsyncBaseClient, SyncBaseClient


class EstimateClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.image = ImageClient(base_client=self._base_client)


class AsyncEstimateClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.image = AsyncImageClient(base_client=self._base_client)
