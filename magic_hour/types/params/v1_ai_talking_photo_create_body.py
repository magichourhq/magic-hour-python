import pydantic
import typing
import typing_extensions

from .v1_ai_talking_photo_create_body_assets import (
    V1AiTalkingPhotoCreateBodyAssets,
    _SerializerV1AiTalkingPhotoCreateBodyAssets,
)
from .v1_ai_talking_photo_create_body_style import (
    V1AiTalkingPhotoCreateBodyStyle,
    _SerializerV1AiTalkingPhotoCreateBodyStyle,
)


class V1AiTalkingPhotoCreateBody(typing_extensions.TypedDict):
    """
    Provide the assets for creating a talking photo
    """

    assets: typing_extensions.Required[V1AiTalkingPhotoCreateBodyAssets]
    """
    Provide the assets for creating a talking photo
    """

    end_seconds: typing_extensions.Required[float]
    """
    The end time of the input audio in seconds. The maximum duration allowed is 60 seconds.
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image. This value is mainly used for your own identification of the image.
    """

    start_seconds: typing_extensions.Required[float]
    """
    The start time of the input audio in seconds. The maximum duration allowed is 60 seconds.
    """

    style: typing_extensions.NotRequired[V1AiTalkingPhotoCreateBodyStyle]
    """
    Attributes used to dictate the style of the output
    """


class _SerializerV1AiTalkingPhotoCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiTalkingPhotoCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1AiTalkingPhotoCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    start_seconds: float = pydantic.Field(
        alias="start_seconds",
    )
    style: typing.Optional[_SerializerV1AiTalkingPhotoCreateBodyStyle] = pydantic.Field(
        alias="style", default=None
    )
