import pydantic
import typing_extensions


class V1AiTalkingPhotoCreateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for creating a talking photo
    """

    audio_file_path: typing_extensions.Required[str]
    """
    The audio file to sync with the image. This value can be either the `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls), or the url of the file.
    """

    image_file_path: typing_extensions.Required[str]
    """
    The source image to animate. This value can be either the `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls), or the url of the file.
    """


class _SerializerV1AiTalkingPhotoCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1AiTalkingPhotoCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    audio_file_path: str = pydantic.Field(
        alias="audio_file_path",
    )
    image_file_path: str = pydantic.Field(
        alias="image_file_path",
    )
