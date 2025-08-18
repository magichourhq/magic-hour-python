import pydantic
import typing
import typing_extensions

from .v1_files_upload_urls_create_body_items_item import (
    V1FilesUploadUrlsCreateBodyItemsItem,
    _SerializerV1FilesUploadUrlsCreateBodyItemsItem,
)


class V1FilesUploadUrlsCreateBody(typing_extensions.TypedDict):
    """
    V1FilesUploadUrlsCreateBody
    """

    items: typing_extensions.Required[typing.List[V1FilesUploadUrlsCreateBodyItemsItem]]
    """
    The list of assets to upload. The response array will match the order of items in the request body.
    """


class _SerializerV1FilesUploadUrlsCreateBody(pydantic.BaseModel):
    """
    Serializer for V1FilesUploadUrlsCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    items: typing.List[_SerializerV1FilesUploadUrlsCreateBodyItemsItem] = (
        pydantic.Field(
            alias="items",
        )
    )
