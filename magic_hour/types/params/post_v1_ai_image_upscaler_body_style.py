import pydantic
import typing
import typing_extensions


class PostV1AiImageUpscalerBodyStyle(typing_extensions.TypedDict):
    """
    PostV1AiImageUpscalerBodyStyle
    """

    enhancement: typing_extensions.Required[
        typing_extensions.Literal["Balanced", "Creative", "Resemblance"]
    ]

    prompt: typing_extensions.NotRequired[str]
    """
    A prompt to guide the final image. This value is ignored if `enhancement` is not Creative
    """


class _SerializerPostV1AiImageUpscalerBodyStyle(pydantic.BaseModel):
    """
    Serializer for PostV1AiImageUpscalerBodyStyle handling case conversions
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
