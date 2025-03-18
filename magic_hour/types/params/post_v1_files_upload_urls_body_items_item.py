import pydantic
import typing_extensions


class PostV1FilesUploadUrlsBodyItemsItem(typing_extensions.TypedDict):
    """
    PostV1FilesUploadUrlsBodyItemsItem
    """

    extension: typing_extensions.Required[str]
    """
    the extension of the file to upload. Do not include the dot (.) before the extension.
    """

    type_field: typing_extensions.Required[
        typing_extensions.Literal["audio", "image", "video"]
    ]
    """
    The type of asset to upload
    """


class _SerializerPostV1FilesUploadUrlsBodyItemsItem(pydantic.BaseModel):
    """
    Serializer for PostV1FilesUploadUrlsBodyItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    extension: str = pydantic.Field(
        alias="extension",
    )
    type_field: typing_extensions.Literal["audio", "image", "video"] = pydantic.Field(
        alias="type",
    )
