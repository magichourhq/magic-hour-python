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
    * `quick` - Fastest option for rapid results. Takes ~3 minutes per 5s of video.
    *  `studio` - Polished visuals with longer runtime. Takes ~8.5 minutes per 5s of video.
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
