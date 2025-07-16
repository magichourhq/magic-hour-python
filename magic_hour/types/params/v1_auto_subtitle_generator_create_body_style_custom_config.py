import pydantic
import typing
import typing_extensions


class V1AutoSubtitleGeneratorCreateBodyStyleCustomConfig(typing_extensions.TypedDict):
    """
    Custom subtitle configuration.
    """

    font: typing_extensions.NotRequired[str]
    """
    Font name from Google Fonts. Not all fonts support all languages or character sets. 
    We recommend verifying language support and appearance directly on https://fonts.google.com before use.
    """

    font_size: typing_extensions.NotRequired[float]
    """
    Font size in pixels. If not provided, the font size is automatically calculated based on the video resolution.
    """

    font_style: typing_extensions.NotRequired[str]
    """
    Font style (e.g., normal, italic, bold)
    """

    highlighted_text_color: typing_extensions.NotRequired[str]
    """
    Color used to highlight the current spoken text
    """

    horizontal_position: typing_extensions.NotRequired[str]
    """
    Horizontal alignment of the text (e.g., left, center, right)
    """

    stroke_color: typing_extensions.NotRequired[str]
    """
    Stroke (outline) color of the text
    """

    stroke_width: typing_extensions.NotRequired[float]
    """
    Width of the text stroke in pixels. If `stroke_color` is provided, but `stroke_width` is not, the `stroke_width` will be calculated automatically based on the font size.
    """

    text_color: typing_extensions.NotRequired[str]
    """
    Primary text color in hex format
    """

    vertical_position: typing_extensions.NotRequired[str]
    """
    Vertical alignment of the text (e.g., top, center, bottom)
    """


class _SerializerV1AutoSubtitleGeneratorCreateBodyStyleCustomConfig(pydantic.BaseModel):
    """
    Serializer for V1AutoSubtitleGeneratorCreateBodyStyleCustomConfig handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    font: typing.Optional[str] = pydantic.Field(alias="font", default=None)
    font_size: typing.Optional[float] = pydantic.Field(alias="font_size", default=None)
    font_style: typing.Optional[str] = pydantic.Field(alias="font_style", default=None)
    highlighted_text_color: typing.Optional[str] = pydantic.Field(
        alias="highlighted_text_color", default=None
    )
    horizontal_position: typing.Optional[str] = pydantic.Field(
        alias="horizontal_position", default=None
    )
    stroke_color: typing.Optional[str] = pydantic.Field(
        alias="stroke_color", default=None
    )
    stroke_width: typing.Optional[float] = pydantic.Field(
        alias="stroke_width", default=None
    )
    text_color: typing.Optional[str] = pydantic.Field(alias="text_color", default=None)
    vertical_position: typing.Optional[str] = pydantic.Field(
        alias="vertical_position", default=None
    )
