import pydantic
import typing_extensions


class PostV1AiImageUpscalerBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for upscaling
    """

    image_file_path: typing_extensions.Required[str]
    """
    The image to upscale. This value can be either the `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls), or the url of the file.
    """


class _SerializerPostV1AiImageUpscalerBodyAssets(pydantic.BaseModel):
    """
    Serializer for PostV1AiImageUpscalerBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    image_file_path: str = pydantic.Field(
        alias="image_file_path",
    )
