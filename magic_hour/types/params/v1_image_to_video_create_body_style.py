import pydantic
import typing
import typing_extensions


class V1ImageToVideoCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1ImageToVideoCreateBodyStyle
    """

    high_quality: typing_extensions.NotRequired[bool]
    """
    High Quality mode enhances detail, sharpness, and realism, making it ideal for portraits, animals, and intricate landscapes.
    """

    prompt: typing_extensions.Required[typing.Optional[str]]
    """
    The prompt used for the video.
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
    prompt: typing.Optional[str] = pydantic.Field(
        alias="prompt",
    )
