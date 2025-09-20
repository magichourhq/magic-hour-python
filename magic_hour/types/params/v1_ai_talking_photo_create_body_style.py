import pydantic
import typing
import typing_extensions


class V1AiTalkingPhotoCreateBodyStyle(typing_extensions.TypedDict):
    """
    Attributes used to dictate the style of the output
    """

    generation_mode: typing_extensions.NotRequired[
        typing_extensions.Literal["expressive", "pro", "stable", "standard"]
    ]
    """
    Controls overall motion style.
    * `pro` -  Higher fidelity, realistic detail, accurate lip sync, and faster generation.
    * `standard` -  More expressive motion, but lower visual fidelity.
    
    * `expressive` - More motion and facial expressiveness; may introduce visual artifacts. (Deprecated: passing this value will be treated as `standard`)
    * `stable` -  Reduced motion for cleaner output; may result in minimal animation. (Deprecated: passing this value will be treated as `pro`)
    """

    intensity: typing_extensions.NotRequired[float]
    """
    Note: this value is only applicable when generation_mode is `expressive`. The value can include up to 2 decimal places.
    * Lower values yield more stability but can suppress mouth movement.
    * Higher values increase motion and expressiveness, with a higher risk of distortion.
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
        typing_extensions.Literal["expressive", "pro", "stable", "standard"]
    ] = pydantic.Field(alias="generation_mode", default=None)
    intensity: typing.Optional[float] = pydantic.Field(alias="intensity", default=None)
