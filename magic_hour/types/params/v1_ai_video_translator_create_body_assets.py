import pydantic
import typing_extensions


class V1AiVideoTranslatorCreateBodyAssets(typing_extensions.TypedDict):
    """
    Source video for the translation job.
    """

    video_file_path: typing_extensions.Required[str]
    """
    Source video containing the speech to translate. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.
    
    """


class _SerializerV1AiVideoTranslatorCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1AiVideoTranslatorCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    video_file_path: str = pydantic.Field(
        alias="video_file_path",
    )
