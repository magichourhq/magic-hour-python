import pydantic
import typing
import typing_extensions

from .post_v1_text_to_video_body_style import (
    PostV1TextToVideoBodyStyle,
    _SerializerPostV1TextToVideoBodyStyle,
)


class PostV1TextToVideoBody(typing_extensions.TypedDict):
    """
    PostV1TextToVideoBody
    """

    end_seconds: typing_extensions.Required[float]
    """
    The total duration of the output video in seconds.
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of video
    """

    orientation: typing_extensions.Required[
        typing_extensions.Literal["landscape", "portrait", "square"]
    ]
    """
    Determines the orientation of the output video
    """

    style: typing_extensions.Required[PostV1TextToVideoBodyStyle]


class _SerializerPostV1TextToVideoBody(pydantic.BaseModel):
    """
    Serializer for PostV1TextToVideoBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    orientation: typing_extensions.Literal["landscape", "portrait", "square"] = (
        pydantic.Field(
            alias="orientation",
        )
    )
    style: _SerializerPostV1TextToVideoBodyStyle = pydantic.Field(
        alias="style",
    )
