import typing_extensions
import pydantic


class PostV1AiHeadshotGeneratorBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for headshot photo
    """

    image_file_path: typing_extensions.Required[str]
    """
    The image used to generate the headshot. This image must contain one detectable face. This value can be either the `file_path` field from the response of the [upload urls API](/docs/api/tag/files/post/v1/files/upload-urls), or the url of the file.
    """


class _SerializerPostV1AiHeadshotGeneratorBodyAssets(pydantic.BaseModel):
    """
    Serializer for PostV1AiHeadshotGeneratorBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    image_file_path: str = pydantic.Field(
        alias="image_file_path",
    )
