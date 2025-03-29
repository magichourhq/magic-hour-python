import pydantic
import typing_extensions


class V1FilesUploadUrlsCreateBodyItemsItem(typing_extensions.TypedDict):
    """
    V1FilesUploadUrlsCreateBodyItemsItem
    """

    extension: typing_extensions.Required[str]
    """
    the extension of the file to upload. Do not include the dot (.) before the extension.
    """

    type_: typing_extensions.Required[
        typing_extensions.Literal["audio", "image", "video"]
    ]
    """
    The type of asset to upload
    """


class _SerializerV1FilesUploadUrlsCreateBodyItemsItem(pydantic.BaseModel):
    """
    Serializer for V1FilesUploadUrlsCreateBodyItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    extension: str = pydantic.Field(
        alias="extension",
    )
    type_: typing_extensions.Literal["audio", "image", "video"] = pydantic.Field(
        alias="type",
    )
