import pydantic
import typing
import typing_extensions

from .v1_animation_create_body_assets import (
    V1AnimationCreateBodyAssets,
    _SerializerV1AnimationCreateBodyAssets,
)
from .v1_animation_create_body_style import (
    V1AnimationCreateBodyStyle,
    _SerializerV1AnimationCreateBodyStyle,
)


class V1AnimationCreateBody(typing_extensions.TypedDict):
    """
    V1AnimationCreateBody
    """

    assets: typing_extensions.Required[V1AnimationCreateBodyAssets]
    """
    Provide the assets for animation.
    """

    end_seconds: typing_extensions.Required[float]
    """
    This value determines the duration of the output video.
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
    The name of video. This value is mainly used for your own identification of the video.
    """

    style: typing_extensions.Required[V1AnimationCreateBodyStyle]
    """
    Defines the style of the output video
    """

    width: typing_extensions.Required[int]
    """
    The width of the final output video. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
    """


class _SerializerV1AnimationCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AnimationCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1AnimationCreateBodyAssets = pydantic.Field(
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
    style: _SerializerV1AnimationCreateBodyStyle = pydantic.Field(
        alias="style",
    )
    width: int = pydantic.Field(
        alias="width",
    )
