import pydantic
import typing
import typing_extensions


class V1AiMemeGeneratorCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1AiMemeGeneratorCreateBodyStyle
    """

    search_web: typing_extensions.NotRequired[bool]
    """
    Whether to search the web for meme content.
    """

    template: typing_extensions.Required[
        typing_extensions.Literal[
            "Bike Fall",
            "Change My Mind",
            "Disappointed Guy",
            "Drake Hotline Bling",
            "Galaxy Brain",
            "Gru's Plan",
            "Is This a Pigeon",
            "Panik Kalm Panik",
            "Random",
            "Side Eyeing Chloe",
            "Tuxedo Winnie The Pooh",
            "Two Buttons",
            "Waiting Skeleton",
        ]
    ]
    """
    To use our templates, pass in one of the enum values.
    """

    topic: typing_extensions.Required[str]
    """
    The topic of the meme.
    """


class _SerializerV1AiMemeGeneratorCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiMemeGeneratorCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    search_web: typing.Optional[bool] = pydantic.Field(alias="searchWeb", default=None)
    template: typing_extensions.Literal[
        "Bike Fall",
        "Change My Mind",
        "Disappointed Guy",
        "Drake Hotline Bling",
        "Galaxy Brain",
        "Gru's Plan",
        "Is This a Pigeon",
        "Panik Kalm Panik",
        "Random",
        "Side Eyeing Chloe",
        "Tuxedo Winnie The Pooh",
        "Two Buttons",
        "Waiting Skeleton",
    ] = pydantic.Field(
        alias="template",
    )
    topic: str = pydantic.Field(
        alias="topic",
    )
