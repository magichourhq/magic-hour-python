import pydantic
import typing

from .v1_files_upload_urls_create_response_items_item import (
    V1FilesUploadUrlsCreateResponseItemsItem,
)


class V1FilesUploadUrlsCreateResponse(pydantic.BaseModel):
    """
    Success
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    items: typing.List[V1FilesUploadUrlsCreateResponseItemsItem] = pydantic.Field(
        alias="items",
    )
