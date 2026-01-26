import pydantic
import typing
import typing_extensions


class V1AiTalkingPhotoCreateBodyStyle(typing_extensions.TypedDict):
    """
    Attributes used to dictate the style of the output
    """

    generation_mode: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "expressive", "pro", "prompted", "realistic", "stable", "standard"
        ]
    ]
    """
    Controls overall motion style.
    * `realistic` - Maintains likeness well, high quality, and reliable.
    * `prompted` - Slightly lower likeness; allows option to prompt scene.
    
    **Deprecated values (maintained for backward compatibility):**
    * `pro` - Deprecated: use `realistic`
    * `standard` - Deprecated: use `prompted`
    * `stable` - Deprecated: use `realistic`
    * `expressive` - Deprecated: use `prompted`
    """

    intensity: typing_extensions.NotRequired[float]
    """
    Note: this value is only applicable when generation_mode is `expressive`. The value can include up to 2 decimal places.
    * Lower values yield more stability but can suppress mouth movement.
    * Higher values increase motion and expressiveness, with a higher risk of distortion.
    """

    prompt: typing_extensions.NotRequired[str]
    """
    A text prompt to guide the generation. Only applicable when generation_mode is `prompted`.
    This field is ignored for other modes.
    """


class _SerializerV1AiTalkingPhotoCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiTalkingPhotoCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    generation_mode: typing.Optional[
        typing_extensions.Literal[
            "expressive", "pro", "prompted", "realistic", "stable", "standard"
        ]
    ] = pydantic.Field(alias="generation_mode", default=None)
    intensity: typing.Optional[float] = pydantic.Field(alias="intensity", default=None)
    prompt: typing.Optional[str] = pydantic.Field(alias="prompt", default=None)
