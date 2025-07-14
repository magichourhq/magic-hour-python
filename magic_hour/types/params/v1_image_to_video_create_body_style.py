import pydantic
import typing
import typing_extensions


class V1ImageToVideoCreateBodyStyle(typing_extensions.TypedDict):
    """
    Attributed used to dictate the style of the output
    """

    high_quality: typing_extensions.NotRequired[bool]
    """
    Deprecated: Please use `resolution` instead. For backward compatibility, 
    * `false` maps to 720p resolution
    * `true` maps to 1080p resolution
    
    This field will be removed in a future version. Use the `resolution` field to directly specify the resolution.
    """

    prompt: typing_extensions.NotRequired[str]
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


class _SerializerV1ImageToVideoCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1ImageToVideoCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    high_quality: typing.Optional[bool] = pydantic.Field(
        alias="high_quality", default=None
    )
    prompt: typing.Optional[str] = pydantic.Field(alias="prompt", default=None)
    quality_mode: typing.Optional[typing_extensions.Literal["quick", "studio"]] = (
        pydantic.Field(alias="quality_mode", default=None)
    )
