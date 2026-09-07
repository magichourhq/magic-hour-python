import typing

from magic_hour.types import models
from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)


class AccountClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.V1AccountListResponse:
        """
        Get account details

        Get the current credit balance and subscription details of the account that owns the API key.

        GET /v1/account

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.account.list()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/v1/account",
            auth_names=["bearerAuth"],
            cast_to=models.V1AccountListResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAccountClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.V1AccountListResponse:
        """
        Get account details

        Get the current credit balance and subscription details of the account that owns the API key.

        GET /v1/account

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.account.list()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/v1/account",
            auth_names=["bearerAuth"],
            cast_to=models.V1AccountListResponse,
            request_options=request_options or default_request_options(),
        )
