import pydantic
import typing_extensions


class PostV1AiQrCodeGeneratorBodyStyle(typing_extensions.TypedDict):
    """
    PostV1AiQrCodeGeneratorBodyStyle
    """

    art_style: typing_extensions.Required[str]
    """
    To use our templates, pass in one of Watercolor, Cyberpunk City, Ink Landscape, Interior Painting, Japanese Street, Mech, Minecraft, Picasso Painting, Game Map, Spaceship, Chinese Painting, Winter Village, or pass any custom art style.
    """


class _SerializerPostV1AiQrCodeGeneratorBodyStyle(pydantic.BaseModel):
    """
    Serializer for PostV1AiQrCodeGeneratorBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    art_style: str = pydantic.Field(
        alias="art_style",
    )
