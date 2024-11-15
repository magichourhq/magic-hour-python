"""
Generated by Sideko (sideko.dev)
"""

import typing_extensions
import pydantic


class PostV1FilesUploadUrlsBodyItemsItem(typing_extensions.TypedDict):
    """ """

    extension: typing_extensions.Required[str]
    type_field: typing_extensions.Required[
        typing_extensions.Literal["audio", "image", "video"]
    ]


class _SerializerPostV1FilesUploadUrlsBodyItemsItem(pydantic.BaseModel):
    """
    Serializer for PostV1FilesUploadUrlsBodyItemsItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    extension: str = pydantic.Field(alias="extension")
    type_field: typing_extensions.Literal["audio", "image", "video"] = pydantic.Field(
        alias="type"
    )
