import pydantic
import typing

from .v1_saved_items_list_response_items_item import V1SavedItemsListResponseItemsItem


class V1SavedItemsListResponse(pydantic.BaseModel):
    """
    V1SavedItemsListResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    items: typing.List[V1SavedItemsListResponseItemsItem] = pydantic.Field(
        alias="items",
    )
    next_cursor: typing.Optional[str] = pydantic.Field(
        alias="next_cursor",
    )
    """
    Cursor for the next page, or null when there are no more saved items.
    """
