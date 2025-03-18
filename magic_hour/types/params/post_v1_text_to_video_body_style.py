import pydantic
import typing_extensions


class PostV1TextToVideoBodyStyle(typing_extensions.TypedDict):
    """
    PostV1TextToVideoBodyStyle
    """

    prompt: typing_extensions.Required[str]
    """
    The prompt used for the video.
    """


class _SerializerPostV1TextToVideoBodyStyle(pydantic.BaseModel):
    """
    Serializer for PostV1TextToVideoBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prompt: str = pydantic.Field(
        alias="prompt",
    )
