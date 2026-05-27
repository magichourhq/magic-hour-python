import pydantic
import typing
import typing_extensions


class V1AudioToVideoCreateBodyStyle(typing_extensions.TypedDict):
    """
    Attributes used to dictate the style of the output
    """

    prompt: typing_extensions.NotRequired[str]
    """
    Prompt to guide the visual style of the video.
    """


class _SerializerV1AudioToVideoCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AudioToVideoCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prompt: typing.Optional[str] = pydantic.Field(alias="prompt", default=None)
