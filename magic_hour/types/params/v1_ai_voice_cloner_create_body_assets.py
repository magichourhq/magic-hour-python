import pydantic
import typing_extensions


class V1AiVoiceClonerCreateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for voice cloning.
    """

    audio_file_path: typing_extensions.Required[str]
    """
    The audio used to clone the voice. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.
    
    """


class _SerializerV1AiVoiceClonerCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1AiVoiceClonerCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    audio_file_path: str = pydantic.Field(
        alias="audio_file_path",
    )
