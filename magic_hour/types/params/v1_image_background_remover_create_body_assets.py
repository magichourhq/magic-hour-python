import pydantic
import typing_extensions


class V1ImageBackgroundRemoverCreateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for background removal
    """

    image_file_path: typing_extensions.Required[str]
    """
    The image used to generate the image. This value can be either the `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls), or the url of the file.
    """


class _SerializerV1ImageBackgroundRemoverCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1ImageBackgroundRemoverCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    image_file_path: str = pydantic.Field(
        alias="image_file_path",
    )
