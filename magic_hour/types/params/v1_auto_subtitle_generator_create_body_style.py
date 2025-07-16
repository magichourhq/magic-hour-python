import pydantic
import typing
import typing_extensions

from .v1_auto_subtitle_generator_create_body_style_custom_config import (
    V1AutoSubtitleGeneratorCreateBodyStyleCustomConfig,
    _SerializerV1AutoSubtitleGeneratorCreateBodyStyleCustomConfig,
)


class V1AutoSubtitleGeneratorCreateBodyStyle(typing_extensions.TypedDict):
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

    custom_config: typing_extensions.NotRequired[
        V1AutoSubtitleGeneratorCreateBodyStyleCustomConfig
    ]
    """
    Custom subtitle configuration.
    """

    template: typing_extensions.NotRequired[
        typing_extensions.Literal["cinematic", "highlight", "karaoke", "minimalist"]
    ]
    """
    Preset subtitle templates. Please visit https://magichour.ai/create/auto-subtitle-generator to see the style of the existing templates.
    """


class _SerializerV1AutoSubtitleGeneratorCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AutoSubtitleGeneratorCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    custom_config: typing.Optional[
        _SerializerV1AutoSubtitleGeneratorCreateBodyStyleCustomConfig
    ] = pydantic.Field(alias="custom_config", default=None)
    template: typing.Optional[
        typing_extensions.Literal["cinematic", "highlight", "karaoke", "minimalist"]
    ] = pydantic.Field(alias="template", default=None)
