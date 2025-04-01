import pydantic
import typing
import typing_extensions

from .v1_ai_talking_photo_create_body_assets import (
    V1AiTalkingPhotoCreateBodyAssets,
    _SerializerV1AiTalkingPhotoCreateBodyAssets,
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
    The end time of the input video in seconds
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image
    """

    start_seconds: typing_extensions.Required[float]
    """
    The start time of the input video in seconds
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
