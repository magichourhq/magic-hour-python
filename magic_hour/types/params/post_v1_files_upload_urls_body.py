import pydantic
import typing
import typing_extensions

from .post_v1_files_upload_urls_body_items_item import (
    PostV1FilesUploadUrlsBodyItemsItem,
    _SerializerPostV1FilesUploadUrlsBodyItemsItem,
)


class PostV1FilesUploadUrlsBody(typing_extensions.TypedDict):
    """
    PostV1FilesUploadUrlsBody
    """

    items: typing_extensions.Required[typing.List[PostV1FilesUploadUrlsBodyItemsItem]]


class _SerializerPostV1FilesUploadUrlsBody(pydantic.BaseModel):
    """
    Serializer for PostV1FilesUploadUrlsBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    items: typing.List[_SerializerPostV1FilesUploadUrlsBodyItemsItem] = pydantic.Field(
        alias="items",
    )
