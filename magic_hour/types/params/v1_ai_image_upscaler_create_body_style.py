import pydantic
import typing
import typing_extensions


class V1AiImageUpscalerCreateBodyStyle(typing_extensions.TypedDict):
    """
    Style settings for the upscale. Use `mode` (`"preserve"`, `"balanced"`, or `"creative"`). Defaults to `"balanced"`.
    """

    enhancement: typing_extensions.NotRequired[
        typing_extensions.Literal["Balanced", "Creative", "Resemblance"]
    ]
    """
    Deprecated: use `mode` instead. `"Resemblance"` maps to `"preserve"`. `"Balanced"` and `"Creative"` map to the same-named modes.
    """

    mode: typing_extensions.NotRequired[
        typing_extensions.Literal["balanced", "creative", "preserve", "pro"]
    ]
    """
    The upscaling mode. `"preserve"` uses the fast pro pipeline (1× credit multiplier). `"balanced"` and `"creative"` use the creative pipeline (2× credit multiplier). `"pro"` is deprecated and maps to `"preserve"`. Defaults to `"balanced"`.
    """

    prompt: typing_extensions.NotRequired[str]
    """
    A prompt to guide the final image. Only used when mode is `creative`.
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
    mode: typing.Optional[
        typing_extensions.Literal["balanced", "creative", "preserve", "pro"]
    ] = pydantic.Field(alias="mode", default=None)
    prompt: typing.Optional[str] = pydantic.Field(alias="prompt", default=None)
