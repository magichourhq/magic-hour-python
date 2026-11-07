import typing

from magic_hour.types import models
from make_api_request import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)


class VoicesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        cursor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1VoicesListResponse:
        """
        List voices

        List the voices available for text-to-speech. Use a voice's `id` as `style.voice_name` in the AI Voice Generator API. To fetch the next page, pass the response's next_cursor as cursor.

        GET /v1/voices

        Args:
            cursor: Opaque pagination cursor from the previous response's next_cursor.
            limit: Maximum number of voices to return. Defaults to 20.
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.voices.list(limit=20)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(cursor, type_utils.NotGiven):
            encode_query_param(
                _query,
                "cursor",
                to_encodable(item=cursor, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=int),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/voices",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.V1VoicesListResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncVoicesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        cursor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1VoicesListResponse:
        """
        List voices

        List the voices available for text-to-speech. Use a voice's `id` as `style.voice_name` in the AI Voice Generator API. To fetch the next page, pass the response's next_cursor as cursor.

        GET /v1/voices

        Args:
            cursor: Opaque pagination cursor from the previous response's next_cursor.
            limit: Maximum number of voices to return. Defaults to 20.
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.voices.list(limit=20)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(cursor, type_utils.NotGiven):
            encode_query_param(
                _query,
                "cursor",
                to_encodable(item=cursor, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=int),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/voices",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.V1VoicesListResponse,
            request_options=request_options or default_request_options(),
        )
