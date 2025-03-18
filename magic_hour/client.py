import httpx
import typing

from magic_hour.core import AsyncBaseClient, AuthBearer, SyncBaseClient
from magic_hour.environment import Environment
from magic_hour.resources.v1 import AsyncV1Client, V1Client


class Client:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        environment: Environment = Environment.ENVIRONMENT,
        token: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.Client(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth("bearerAuth", AuthBearer(val=token))
        self.v1 = V1Client(base_client=self._base_client)


class AsyncClient:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        environment: Environment = Environment.ENVIRONMENT,
        token: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.AsyncClient(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth("bearerAuth", AuthBearer(val=token))
        self.v1 = AsyncV1Client(base_client=self._base_client)


def _get_base_url(
    *, base_url: typing.Optional[str] = None, environment: Environment
) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Must include a base_url or environment arguments")
