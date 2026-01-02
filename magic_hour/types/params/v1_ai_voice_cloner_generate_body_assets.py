import pydantic
import typing_extensions


class V1AiVoiceClonerGenerateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for voice cloning.
    """

    audio_file_path: typing_extensions.Required[str]
    """
    The audio used to clone the voice. This can be a local file path or URL.
    """


class _SerializerV1AiVoiceClonerGenerateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1AiVoiceClonerGenerateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    audio_file_path: str = pydantic.Field(
        alias="audio_file_path",
    )
