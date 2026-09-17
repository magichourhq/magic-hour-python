import pydantic
import typing
import typing_extensions

from .v1_saved_items_list_response_items_item_assets_item import (
    V1SavedItemsListResponseItemsItemAssetsItem,
)


class V1SavedItemsListResponseItemsItem(pydantic.BaseModel):
    """
    V1SavedItemsListResponseItemsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    assets: typing.List[V1SavedItemsListResponseItemsItemAssetsItem] = pydantic.Field(
        alias="assets",
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique ID of the saved item.
    """
    name: typing.Optional[str] = pydantic.Field(
        alias="name",
    )
    """
    User-provided name of the saved item.
    """
    type_: typing_extensions.Literal[
        "brand_kit", "character", "moodboard", "reference", "voice"
    ] = pydantic.Field(
        alias="type",
    )
    """
    Saved item type.
    """
