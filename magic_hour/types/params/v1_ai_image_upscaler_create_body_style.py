import pydantic
import typing
import typing_extensions


class V1AiImageUpscalerCreateBodyStyle(typing_extensions.TypedDict):
    """
    Style settings for the upscale. Use `mode` to select between `"pro"` (faster, no enhancement required) and `"creative"` (defaults to `"Balanced"` enhancement). Defaults to `"creative"`.
    """

    enhancement: typing_extensions.NotRequired[
        typing_extensions.Literal["Balanced", "Creative", "Resemblance"]
    ]

    mode: typing_extensions.NotRequired[typing_extensions.Literal["creative", "pro"]]
    """
    The upscaling mode. `"pro"` is faster and does not require `enhancement`. `"creative"` requires `enhancement`. Defaults to `"creative"`.
    """

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

    enhancement: typing.Optional[
        typing_extensions.Literal["Balanced", "Creative", "Resemblance"]
    ] = pydantic.Field(alias="enhancement", default=None)
    mode: typing.Optional[typing_extensions.Literal["creative", "pro"]] = (
        pydantic.Field(alias="mode", default=None)
    )
    prompt: typing.Optional[str] = pydantic.Field(alias="prompt", default=None)
