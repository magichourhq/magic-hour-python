import pydantic
import typing

from .post_v1_files_upload_urls_response_items_item import (
    PostV1FilesUploadUrlsResponseItemsItem,
)


class PostV1FilesUploadUrlsResponse(pydantic.BaseModel):
    """
    Success
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    items: typing.List[PostV1FilesUploadUrlsResponseItemsItem] = pydantic.Field(
        alias="items",
    )
