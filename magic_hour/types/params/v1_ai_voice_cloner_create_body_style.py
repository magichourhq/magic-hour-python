import pydantic
import typing
import typing_extensions


class V1AiVoiceClonerCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1AiVoiceClonerCreateBodyStyle
    """

    language: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "afrikaans",
            "albanian",
            "amharic",
            "arabic",
            "armenian",
            "assamese",
            "auto",
            "azerbaijani",
            "basque",
            "belarusian",
            "bengali",
            "bulgarian",
            "burmese",
            "cantonese",
            "catalan",
            "cebuano",
            "chinese",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "estonian",
            "finnish",
            "french",
            "galician",
            "georgian",
            "german",
            "greek",
            "gujarati",
            "haitian creole",
            "hebrew",
            "hindi",
            "hungarian",
            "icelandic",
            "indonesian",
            "italian",
            "japanese",
            "javanese",
            "kannada",
            "kazakh",
            "konkani",
            "korean",
            "lao",
            "latvian",
            "lithuanian",
            "luxembourgish",
            "macedonian",
            "maithili",
            "malagasy",
            "malay",
            "malayalam",
            "marathi",
            "mongolian",
            "nepali",
            "norwegian",
            "odia",
            "pashto",
            "persian",
            "polish",
            "portuguese",
            "punjabi",
            "romanian",
            "russian",
            "serbian",
            "sindhi",
            "sinhala",
            "slovak",
            "slovenian",
            "spanish",
            "swahili",
            "swedish",
            "tagalog",
            "tamil",
            "telugu",
            "thai",
            "turkish",
            "ukrainian",
            "urdu",
            "uzbek",
            "vietnamese",
            "welsh",
        ]
    ]
    """
    Spoken language. Use a canonical lowercase language name, or auto to detect the language from the text. Defaults to auto.
    """

    prompt: typing_extensions.Required[str]
    """
    Text used to generate speech from the cloned voice. The character limit is 5000 characters.
    """

    speed: typing_extensions.NotRequired[float]
    """
    Speech speed multiplier, from 0.75 to 1.30 inclusive. Defaults to 1 (normal speed).
    """


class _SerializerV1AiVoiceClonerCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiVoiceClonerCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    language: typing.Optional[
        typing_extensions.Literal[
            "afrikaans",
            "albanian",
            "amharic",
            "arabic",
            "armenian",
            "assamese",
            "auto",
            "azerbaijani",
            "basque",
            "belarusian",
            "bengali",
            "bulgarian",
            "burmese",
            "cantonese",
            "catalan",
            "cebuano",
            "chinese",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "estonian",
            "finnish",
            "french",
            "galician",
            "georgian",
            "german",
            "greek",
            "gujarati",
            "haitian creole",
            "hebrew",
            "hindi",
            "hungarian",
            "icelandic",
            "indonesian",
            "italian",
            "japanese",
            "javanese",
            "kannada",
            "kazakh",
            "konkani",
            "korean",
            "lao",
            "latvian",
            "lithuanian",
            "luxembourgish",
            "macedonian",
            "maithili",
            "malagasy",
            "malay",
            "malayalam",
            "marathi",
            "mongolian",
            "nepali",
            "norwegian",
            "odia",
            "pashto",
            "persian",
            "polish",
            "portuguese",
            "punjabi",
            "romanian",
            "russian",
            "serbian",
            "sindhi",
            "sinhala",
            "slovak",
            "slovenian",
            "spanish",
            "swahili",
            "swedish",
            "tagalog",
            "tamil",
            "telugu",
            "thai",
            "turkish",
            "ukrainian",
            "urdu",
            "uzbek",
            "vietnamese",
            "welsh",
        ]
    ] = pydantic.Field(alias="language", default=None)
    prompt: str = pydantic.Field(
        alias="prompt",
    )
    speed: typing.Optional[float] = pydantic.Field(alias="speed", default=None)
