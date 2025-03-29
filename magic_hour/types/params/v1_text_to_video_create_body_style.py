import pydantic
import typing_extensions


class V1TextToVideoCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1TextToVideoCreateBodyStyle
    """

    prompt: typing_extensions.Required[str]
    """
    The prompt used for the video.
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
