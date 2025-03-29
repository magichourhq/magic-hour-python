import pydantic
import typing
import typing_extensions

from .v1_text_to_video_create_body_style import (
    V1TextToVideoCreateBodyStyle,
    _SerializerV1TextToVideoCreateBodyStyle,
)


class V1TextToVideoCreateBody(typing_extensions.TypedDict):
    """
    V1TextToVideoCreateBody
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

    style: typing_extensions.Required[V1TextToVideoCreateBodyStyle]


class _SerializerV1TextToVideoCreateBody(pydantic.BaseModel):
    """
    Serializer for V1TextToVideoCreateBody handling case conversions
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
    style: _SerializerV1TextToVideoCreateBodyStyle = pydantic.Field(
        alias="style",
    )
