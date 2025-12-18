import pydantic
import typing_extensions


class V1FilesUploadUrlsCreateBodyItemsItem(typing_extensions.TypedDict):
    """
    V1FilesUploadUrlsCreateBodyItemsItem
    """

    extension: typing_extensions.Required[str]
    """
    The extension of the file to upload. Do not include the dot (.) before the extension. Possible extensions are mp4,m4v,mov,webm,mp3,wav,aac,flac,webm,png,jpg,jpeg,heic,webp,avif,jp2,tiff,bmp,gif,webp,webm
    """

    type_: typing_extensions.Required[
        typing_extensions.Literal["audio", "image", "video"]
    ]
    """
    The type of asset to upload. Possible types are video, audio, image
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
