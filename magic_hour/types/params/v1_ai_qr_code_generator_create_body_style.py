import pydantic
import typing_extensions


class V1AiQrCodeGeneratorCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1AiQrCodeGeneratorCreateBodyStyle
    """

    art_style: typing_extensions.Required[str]
    """
    To use our templates, pass in one of Watercolor, Cyberpunk City, Ink Landscape, Interior Painting, Japanese Street, Mech, Minecraft, Picasso Painting, Game Map, Spaceship, Chinese Painting, Winter Village, or pass any custom art style.
    """


class _SerializerV1AiQrCodeGeneratorCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiQrCodeGeneratorCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    art_style: str = pydantic.Field(
        alias="art_style",
    )
