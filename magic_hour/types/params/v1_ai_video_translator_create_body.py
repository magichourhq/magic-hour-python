import pydantic
import typing
import typing_extensions

from .v1_ai_video_translator_create_body_assets import (
    V1AiVideoTranslatorCreateBodyAssets,
    _SerializerV1AiVideoTranslatorCreateBodyAssets,
)


class V1AiVideoTranslatorCreateBody(typing_extensions.TypedDict):
    """
    V1AiVideoTranslatorCreateBody
    """

    assets: typing_extensions.Required[V1AiVideoTranslatorCreateBodyAssets]
    """
    Source video for the translation job.
    """

    end_seconds: typing_extensions.Required[float]
    """
    End time of your clip (seconds). Must be greater than start_seconds. The clip must be 1-30 seconds long.
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your video a custom name for easy identification.
    """

    resolution: typing_extensions.NotRequired[
        typing_extensions.Literal["1080p", "480p", "720p"]
    ]
    """
    Output video resolution. Defaults to 480p. 720p and 1080p require a paid plan.
    """

    start_seconds: typing_extensions.NotRequired[float]
    """
    Start time of your clip (seconds). Must be ≥ 0.
    """

    target_language: typing_extensions.Required[
        typing_extensions.Literal[
            "Afrikaans",
            "Arabic",
            "Bengali",
            "Bulgarian",
            "Catalan",
            "Chinese (Simplified)",
            "Chinese (Traditional)",
            "Croatian",
            "Czech",
            "Danish",
            "Dutch",
            "English",
            "Estonian",
            "Finnish",
            "French",
            "German",
            "Greek",
            "Gujarati",
            "Hebrew",
            "Hindi",
            "Hungarian",
            "Indonesian",
            "Italian",
            "Japanese",
            "Kannada",
            "Kazakh",
            "Korean",
            "Latvian",
            "Lithuanian",
            "Malay",
            "Malayalam",
            "Marathi",
            "Norwegian",
            "Persian",
            "Polish",
            "Portuguese",
            "Punjabi",
            "Romanian",
            "Russian",
            "Serbian",
            "Slovak",
            "Slovenian",
            "Spanish",
            "Swahili",
            "Swedish",
            "Tamil",
            "Telugu",
            "Thai",
            "Turkish",
            "Ukrainian",
            "Urdu",
            "Vietnamese",
            "Welsh",
        ]
    ]
    """
    Language to translate the video's speech into.
    """


class _SerializerV1AiVideoTranslatorCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiVideoTranslatorCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1AiVideoTranslatorCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    resolution: typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]] = (
        pydantic.Field(alias="resolution", default=None)
    )
    start_seconds: typing.Optional[float] = pydantic.Field(
        alias="start_seconds", default=None
    )
    target_language: typing_extensions.Literal[
        "Afrikaans",
        "Arabic",
        "Bengali",
        "Bulgarian",
        "Catalan",
        "Chinese (Simplified)",
        "Chinese (Traditional)",
        "Croatian",
        "Czech",
        "Danish",
        "Dutch",
        "English",
        "Estonian",
        "Finnish",
        "French",
        "German",
        "Greek",
        "Gujarati",
        "Hebrew",
        "Hindi",
        "Hungarian",
        "Indonesian",
        "Italian",
        "Japanese",
        "Kannada",
        "Kazakh",
        "Korean",
        "Latvian",
        "Lithuanian",
        "Malay",
        "Malayalam",
        "Marathi",
        "Norwegian",
        "Persian",
        "Polish",
        "Portuguese",
        "Punjabi",
        "Romanian",
        "Russian",
        "Serbian",
        "Slovak",
        "Slovenian",
        "Spanish",
        "Swahili",
        "Swedish",
        "Tamil",
        "Telugu",
        "Thai",
        "Turkish",
        "Ukrainian",
        "Urdu",
        "Vietnamese",
        "Welsh",
    ] = pydantic.Field(
        alias="target_language",
    )
