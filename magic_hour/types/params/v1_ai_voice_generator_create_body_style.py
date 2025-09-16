import pydantic
import typing_extensions


class V1AiVoiceGeneratorCreateBodyStyle(typing_extensions.TypedDict):
    """
    The content used to generate speech.
    """

    prompt: typing_extensions.Required[str]
    """
    Text used to generate speech. Starter tier users can use up to 200 characters, while Creator, Pro, or Business users can use up to 1000.
    """

    voice_name: typing_extensions.Required[
        typing_extensions.Literal[
            "Barack Obama",
            "Donald Trump",
            "Elon Musk",
            "Joe Biden",
            "Joe Rogan",
            "Kanye West",
            "Kim Kardashian",
            "Mark Zuckerberg",
            "Morgan Freeman",
            "Taylor Swift",
        ]
    ]
    """
    The voice to use for the speech. Available voices: Elon Musk, Mark Zuckerberg, Joe Rogan, Barack Obama, Morgan Freeman, Kanye West, Donald Trump, Joe Biden, Kim Kardashian, Taylor Swift
    """


class _SerializerV1AiVoiceGeneratorCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiVoiceGeneratorCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prompt: str = pydantic.Field(
        alias="prompt",
    )
    voice_name: typing_extensions.Literal[
        "Barack Obama",
        "Donald Trump",
        "Elon Musk",
        "Joe Biden",
        "Joe Rogan",
        "Kanye West",
        "Kim Kardashian",
        "Mark Zuckerberg",
        "Morgan Freeman",
        "Taylor Swift",
    ] = pydantic.Field(
        alias="voice_name",
    )
