import pydantic
import typing
import typing_extensions


class V1AiImageGeneratorCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1AiImageGeneratorCreateBodyStyle
    """

    prompt: typing_extensions.Required[str]
    """
    The prompt used for the image.
    """

    tool: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "ai-anime-generator",
            "ai-art-generator",
            "ai-background-generator",
            "ai-character-generator",
            "ai-face-generator",
            "ai-fashion-generator",
            "ai-icon-generator",
            "ai-illustration-generator",
            "ai-interior-design-generator",
            "ai-landscape-generator",
            "ai-logo-generator",
            "ai-manga-generator",
            "ai-outfit-generator",
            "ai-pattern-generator",
            "ai-photo-generator",
            "ai-sketch-generator",
            "ai-tattoo-generator",
            "album-cover-generator",
            "animated-characters-generator",
            "architecture-generator",
            "book-cover-generator",
            "comic-book-generator",
            "dark-fantasy-ai",
            "disney-ai-generator",
            "dnd-ai-art-generator",
            "emoji-generator",
            "fantasy-map-generator",
            "general",
            "graffiti-generator",
            "movie-poster-generator",
            "optical-illusion-generator",
            "pokemon-generator",
            "south-park-character-generator",
            "superhero-generator",
            "thumbnail-maker",
        ]
    ]
    """
    The art style to use for image generation. Defaults to 'general' if not provided.
    """


class _SerializerV1AiImageGeneratorCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiImageGeneratorCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prompt: str = pydantic.Field(
        alias="prompt",
    )
    tool: typing.Optional[
        typing_extensions.Literal[
            "ai-anime-generator",
            "ai-art-generator",
            "ai-background-generator",
            "ai-character-generator",
            "ai-face-generator",
            "ai-fashion-generator",
            "ai-icon-generator",
            "ai-illustration-generator",
            "ai-interior-design-generator",
            "ai-landscape-generator",
            "ai-logo-generator",
            "ai-manga-generator",
            "ai-outfit-generator",
            "ai-pattern-generator",
            "ai-photo-generator",
            "ai-sketch-generator",
            "ai-tattoo-generator",
            "album-cover-generator",
            "animated-characters-generator",
            "architecture-generator",
            "book-cover-generator",
            "comic-book-generator",
            "dark-fantasy-ai",
            "disney-ai-generator",
            "dnd-ai-art-generator",
            "emoji-generator",
            "fantasy-map-generator",
            "general",
            "graffiti-generator",
            "movie-poster-generator",
            "optical-illusion-generator",
            "pokemon-generator",
            "south-park-character-generator",
            "superhero-generator",
            "thumbnail-maker",
        ]
    ] = pydantic.Field(alias="tool", default=None)
