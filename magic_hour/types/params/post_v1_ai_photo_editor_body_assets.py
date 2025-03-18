import pydantic
import typing_extensions


class PostV1AiPhotoEditorBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for photo editor
    """

    image_file_path: typing_extensions.Required[str]
    """
    The image used to generate the output. This value can be either the `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls), or the url of the file.
    """


class _SerializerPostV1AiPhotoEditorBodyAssets(pydantic.BaseModel):
    """
    Serializer for PostV1AiPhotoEditorBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    image_file_path: str = pydantic.Field(
        alias="image_file_path",
    )
