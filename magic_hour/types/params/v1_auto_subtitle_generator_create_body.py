import pydantic
import typing
import typing_extensions

from .v1_auto_subtitle_generator_create_body_assets import (
    V1AutoSubtitleGeneratorCreateBodyAssets,
    _SerializerV1AutoSubtitleGeneratorCreateBodyAssets,
)
from .v1_auto_subtitle_generator_create_body_style import (
    V1AutoSubtitleGeneratorCreateBodyStyle,
    _SerializerV1AutoSubtitleGeneratorCreateBodyStyle,
)


class V1AutoSubtitleGeneratorCreateBody(typing_extensions.TypedDict):
    """
    V1AutoSubtitleGeneratorCreateBody
    """

    assets: typing_extensions.Required[V1AutoSubtitleGeneratorCreateBodyAssets]
    """
    Provide the assets for auto subtitle generator
    """

    end_seconds: typing_extensions.Required[float]
    """
    The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of video. This value is mainly used for your own identification of the video.
    """

    start_seconds: typing_extensions.Required[float]
    """
    The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
    """

    style: typing_extensions.Required[V1AutoSubtitleGeneratorCreateBodyStyle]
    """
    Style of the subtitle. At least one of `.style.template` or `.style.custom_config` must be provided. 
    * If only `.style.template` is provided, default values for the template will be used.
    * If both are provided, the fields in `.style.custom_config` will be used to overwrite the fields in `.style.template`.
    * If only `.style.custom_config` is provided, then all fields in `.style.custom_config` will be used.
    
    To use custom config only, the following `custom_config` params are required:
    * `.style.custom_config.font`
    * `.style.custom_config.text_color`
    * `.style.custom_config.vertical_position`
    * `.style.custom_config.horizontal_position`
    
    """


class _SerializerV1AutoSubtitleGeneratorCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AutoSubtitleGeneratorCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1AutoSubtitleGeneratorCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    start_seconds: float = pydantic.Field(
        alias="start_seconds",
    )
    style: _SerializerV1AutoSubtitleGeneratorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
