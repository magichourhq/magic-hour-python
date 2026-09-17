import typing
import typing_extensions

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


class SavedItemsClient:
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
        type_: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "brand_kit", "character", "moodboard", "reference", "voice"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1SavedItemsListResponse:
        """
        List saved items

        Returns active saved items owned by the authenticated account, newest first. Each item includes every saved asset with a durable file_path for reuse in compatible generation APIs and a temporary signed URL for previewing or downloading. Filter by type to find characters, references, voices, moodboards, or brand kits. To fetch the next page, pass the response's next_cursor as cursor.

        GET /v1/saved-items

        Args:
            cursor: Opaque pagination cursor from the previous response's next_cursor.
            limit: Maximum number of saved items to return. Defaults to 20.
            type_: Only return saved items of this type.
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v1.saved_items.list(limit=20, type_="character")
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
        if not isinstance(type_, type_utils.NotGiven):
            encode_query_param(
                _query,
                "type",
                to_encodable(
                    item=type_,
                    dump_with=typing_extensions.Literal[
                        "brand_kit", "character", "moodboard", "reference", "voice"
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/saved-items",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.V1SavedItemsListResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncSavedItemsClient:
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
        type_: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "brand_kit", "character", "moodboard", "reference", "voice"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.V1SavedItemsListResponse:
        """
        List saved items

        Returns active saved items owned by the authenticated account, newest first. Each item includes every saved asset with a durable file_path for reuse in compatible generation APIs and a temporary signed URL for previewing or downloading. Filter by type to find characters, references, voices, moodboards, or brand kits. To fetch the next page, pass the response's next_cursor as cursor.

        GET /v1/saved-items

        Args:
            cursor: Opaque pagination cursor from the previous response's next_cursor.
            limit: Maximum number of saved items to return. Defaults to 20.
            type_: Only return saved items of this type.
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v1.saved_items.list(limit=20, type_="character")
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
        if not isinstance(type_, type_utils.NotGiven):
            encode_query_param(
                _query,
                "type",
                to_encodable(
                    item=type_,
                    dump_with=typing_extensions.Literal[
                        "brand_kit", "character", "moodboard", "reference", "voice"
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/saved-items",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.V1SavedItemsListResponse,
            request_options=request_options or default_request_options(),
        )
