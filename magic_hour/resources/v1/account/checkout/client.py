import typing
import typing_extensions

from magic_hour.types import models, params
from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)


class CheckoutClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        type_: typing_extensions.Literal["credit_pack"],
        credit_shortfall: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pack_count: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AccountCheckoutCreateResponse:
        """
        Create checkout

        Create a Stripe Checkout link for the account that owns the API key. Nothing is charged until the checkout is completed in a browser.

        POST /v1/account/checkout

        Args:
            credit_shortfall: Credits a blocked request is missing, e.g. `credit_shortfall` from a 402 response. The checkout starts with enough packs to cover it. Defaults to one pack.
            pack_count: Number of credit packs the checkout starts with. Takes priority over `credit_shortfall`.
            type_: What to buy. `credit_pack` is a one-time credit purchase.
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.account.checkout.create(
            type_="credit_pack", credit_shortfall=150.0, pack_count=3
        )
        ```
        """
        _json = to_encodable(
            item={
                "credit_shortfall": credit_shortfall,
                "pack_count": pack_count,
                "type_": type_,
            },
            dump_with=params._SerializerV1AccountCheckoutCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/account/checkout",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AccountCheckoutCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncCheckoutClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        type_: typing_extensions.Literal["credit_pack"],
        credit_shortfall: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pack_count: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1AccountCheckoutCreateResponse:
        """
        Create checkout

        Create a Stripe Checkout link for the account that owns the API key. Nothing is charged until the checkout is completed in a browser.

        POST /v1/account/checkout

        Args:
            credit_shortfall: Credits a blocked request is missing, e.g. `credit_shortfall` from a 402 response. The checkout starts with enough packs to cover it. Defaults to one pack.
            pack_count: Number of credit packs the checkout starts with. Takes priority over `credit_shortfall`.
            type_: What to buy. `credit_pack` is a one-time credit purchase.
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.account.checkout.create(
            type_="credit_pack", credit_shortfall=150.0, pack_count=3
        )
        ```
        """
        _json = to_encodable(
            item={
                "credit_shortfall": credit_shortfall,
                "pack_count": pack_count,
                "type_": type_,
            },
            dump_with=params._SerializerV1AccountCheckoutCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/account/checkout",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.V1AccountCheckoutCreateResponse,
            request_options=request_options or default_request_options(),
        )
