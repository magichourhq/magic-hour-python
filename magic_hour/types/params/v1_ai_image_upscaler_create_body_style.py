import pydantic
import typing
import typing_extensions


class V1AiImageUpscalerCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1AiImageUpscalerCreateBodyStyle
    """

    enhancement: typing_extensions.Required[
        typing_extensions.Literal["Balanced", "Creative", "Resemblance"]
    ]

    prompt: typing_extensions.NotRequired[str]
    """
    A prompt to guide the final image. This value is ignored if `enhancement` is not Creative
    """


class _SerializerV1AiImageUpscalerCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiImageUpscalerCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enhancement: typing_extensions.Literal["Balanced", "Creative", "Resemblance"] = (
        pydantic.Field(
            alias="enhancement",
        )
    )
    prompt: typing.Optional[str] = pydantic.Field(alias="prompt", default=None)
