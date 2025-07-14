import pydantic
import typing
import typing_extensions


class V1TextToVideoCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1TextToVideoCreateBodyStyle
    """

    prompt: typing_extensions.Required[str]
    """
    The prompt used for the video.
    """

    quality_mode: typing_extensions.NotRequired[
        typing_extensions.Literal["quick", "studio"]
    ]
    """
    DEPRECATED: Please use `resolution` field instead. For backward compatibility:
    * `quick` maps to 720p resolution
    * `studio` maps to 1080p resolution
    
    This field will be removed in a future version. Use the `resolution` field to directly to specify the resolution.
    """


class _SerializerV1TextToVideoCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1TextToVideoCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prompt: str = pydantic.Field(
        alias="prompt",
    )
    quality_mode: typing.Optional[typing_extensions.Literal["quick", "studio"]] = (
        pydantic.Field(alias="quality_mode", default=None)
    )
