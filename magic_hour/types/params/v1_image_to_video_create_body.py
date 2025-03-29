import pydantic
import typing
import typing_extensions

from .v1_image_to_video_create_body_assets import (
    V1ImageToVideoCreateBodyAssets,
    _SerializerV1ImageToVideoCreateBodyAssets,
)
from .v1_image_to_video_create_body_style import (
    V1ImageToVideoCreateBodyStyle,
    _SerializerV1ImageToVideoCreateBodyStyle,
)


class V1ImageToVideoCreateBody(typing_extensions.TypedDict):
    """
    V1ImageToVideoCreateBody
    """

    assets: typing_extensions.Required[V1ImageToVideoCreateBodyAssets]
    """
    Provide the assets for image-to-video.
    """

    end_seconds: typing_extensions.Required[float]
    """
    The total duration of the output video in seconds.
    """

    height: typing_extensions.Required[int]
    """
    The height of the input video. This value will help determine the final orientation of the output video. The output video resolution may not match the input.
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of video
    """

    style: typing_extensions.Required[V1ImageToVideoCreateBodyStyle]

    width: typing_extensions.Required[int]
    """
    The width of the input video. This value will help determine the final orientation of the output video. The output video resolution may not match the input.
    """


class _SerializerV1ImageToVideoCreateBody(pydantic.BaseModel):
    """
    Serializer for V1ImageToVideoCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1ImageToVideoCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    height: int = pydantic.Field(
        alias="height",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    style: _SerializerV1ImageToVideoCreateBodyStyle = pydantic.Field(
        alias="style",
    )
    width: int = pydantic.Field(
        alias="width",
    )
