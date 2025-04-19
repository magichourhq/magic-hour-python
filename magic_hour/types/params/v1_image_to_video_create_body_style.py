import pydantic
import typing
import typing_extensions


class V1ImageToVideoCreateBodyStyle(typing_extensions.TypedDict):
    """
    Attributed used to dictate the style of the output
    """

    high_quality: typing_extensions.NotRequired[bool]
    """
    Deprecated: Please use `quality_mode` instead. For backward compatibility, setting `high_quality: true` and `quality_mode: quick` will map to `quality_mode: studio`. Note: `quality_mode: studio` offers the same quality as `high_quality: true`.
    """

    prompt: typing_extensions.NotRequired[str]
    """
    The prompt used for the video.
    """

    quality_mode: typing_extensions.NotRequired[
        typing_extensions.Literal["quick", "studio"]
    ]
    """
    * `quick` - Fastest option for rapid results. Takes ~3 minutes per 5s of video.
    *  `studio` - Polished visuals with longer runtime. Takes ~8.5 minutes per 5s of video.
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
