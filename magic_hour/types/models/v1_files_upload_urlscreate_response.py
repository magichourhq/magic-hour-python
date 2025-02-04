import typing
import pydantic

from .v1_files_upload_urlscreate_response_items_item import (
    V1FilesUploadUrlscreateResponseItemsItem,
)


class V1FilesUploadUrlscreateResponse(pydantic.BaseModel):
    """
    Success
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    items: typing.List[V1FilesUploadUrlscreateResponseItemsItem] = pydantic.Field(
        alias="items",
    )
