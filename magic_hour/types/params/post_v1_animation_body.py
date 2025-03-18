import pydantic
import typing
import typing_extensions

from .post_v1_animation_body_assets import (
    PostV1AnimationBodyAssets,
    _SerializerPostV1AnimationBodyAssets,
)
from .post_v1_animation_body_style import (
    PostV1AnimationBodyStyle,
    _SerializerPostV1AnimationBodyStyle,
)


class PostV1AnimationBody(typing_extensions.TypedDict):
    """
    PostV1AnimationBody
    """

    assets: typing_extensions.Required[PostV1AnimationBodyAssets]
    """
    Provide the assets for animation.
    """

    end_seconds: typing_extensions.Required[float]
    """
    The end time of the input video in seconds
    """

    fps: typing_extensions.Required[float]
    """
    The desire output video frame rate
    """

    height: typing_extensions.Required[int]
    """
    The height of the final output video. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of video
    """

    style: typing_extensions.Required[PostV1AnimationBodyStyle]
    """
    Defines the style of the output video
    """

    width: typing_extensions.Required[int]
    """
    The width of the final output video. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
    """


class _SerializerPostV1AnimationBody(pydantic.BaseModel):
    """
    Serializer for PostV1AnimationBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerPostV1AnimationBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    fps: float = pydantic.Field(
        alias="fps",
    )
    height: int = pydantic.Field(
        alias="height",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    style: _SerializerPostV1AnimationBodyStyle = pydantic.Field(
        alias="style",
    )
    width: int = pydantic.Field(
        alias="width",
    )
