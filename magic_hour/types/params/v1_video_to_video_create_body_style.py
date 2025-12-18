import pydantic
import typing
import typing_extensions


class V1VideoToVideoCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1VideoToVideoCreateBodyStyle
    """

    art_style: typing_extensions.Required[
        typing_extensions.Literal[
            "3D Render",
            "Airbender",
            "Android",
            "Anime Warrior",
            "Armored Knight",
            "Assassin's Creed",
            "Avatar",
            "Black Spiderman",
            "Boba Fett",
            "Bold Anime",
            "Celestial Skin",
            "Chinese Swordsmen",
            "Clay",
            "Comic",
            "Cyberpunk",
            "Cypher",
            "Dark Fantasy",
            "Dragonball Z",
            "Future Bot",
            "Futuristic Fantasy",
            "GTA",
            "Ghibli Anime",
            "Ghost",
            "Gundam",
            "Hologram",
            "Illustration",
            "Impressionism",
            "Ink",
            "Ink Poster",
            "Jinx",
            "Knight",
            "Lego",
            "Link",
            "Marble",
            "Mario",
            "Master Chief",
            "Mech",
            "Minecraft",
            "Mystique",
            "Naruto",
            "Neon Dream",
            "No Art Style",
            "Oil Painting",
            "On Fire",
            "Origami",
            "Painterly Anime",
            "Pixar",
            "Pixel",
            "Power Armor",
            "Power Ranger",
            "Radiant Anime",
            "Realistic Anime",
            "Realistic Pixar",
            "Retro Anime",
            "Retro Sci-Fi",
            "Samurai",
            "Samurai Bot",
            "Sharp Anime",
            "Soft Anime",
            "Solid Snake",
            "Spartan",
            "Starfield",
            "Street Fighter",
            "Studio Ghibli",
            "Sub-Zero",
            "The Void",
            "Tomb Raider",
            "Underwater",
            "Van Gogh",
            "Viking",
            "Watercolor",
            "Western Anime",
            "Wu Kong",
            "Wuxia Anime",
            "Zelda",
        ]
    ]

    model: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "3D Anime",
            "Absolute Reality",
            "Dreamshaper",
            "Flat 2D Anime",
            "Kaywaii",
            "Soft Anime",
            "Western Anime",
            "default",
        ]
    ]
    """
    * `Dreamshaper` - a good all-around model that works for both animations as well as realism.
    * `Absolute Reality` - better at realism, but you'll often get similar results with Dreamshaper as well.
    * `Flat 2D Anime` - best for a flat illustration style that's common in most anime.
    * `default` - use the default recommended model for the selected art style.
    """

    prompt: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The prompt used for the video. Prompt is required if `prompt_type` is `custom` or `append_default`. If `prompt_type` is `default`, then the `prompt` value passed will be ignored.
    """

    prompt_type: typing_extensions.NotRequired[
        typing_extensions.Literal["append_default", "custom", "default"]
    ]
    """
    * `default` - Use the default recommended prompt for the art style.
    * `custom` - Only use the prompt passed in the API. Note: for v1, lora prompt will still be auto added to apply the art style properly.
    * `append_default` - Add the default recommended prompt to the end of the prompt passed in the API.
    """

    version: typing_extensions.NotRequired[
        typing_extensions.Literal["default", "v1", "v2"]
    ]
    """
    * `v1` - more detail, closer prompt adherence, and frame-by-frame previews.
    * `v2` - faster, more consistent, and less noisy.
    * `default` - use the default version for the selected art style.
    """


class _SerializerV1VideoToVideoCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1VideoToVideoCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    art_style: typing_extensions.Literal[
        "3D Render",
        "Airbender",
        "Android",
        "Anime Warrior",
        "Armored Knight",
        "Assassin's Creed",
        "Avatar",
        "Black Spiderman",
        "Boba Fett",
        "Bold Anime",
        "Celestial Skin",
        "Chinese Swordsmen",
        "Clay",
        "Comic",
        "Cyberpunk",
        "Cypher",
        "Dark Fantasy",
        "Dragonball Z",
        "Future Bot",
        "Futuristic Fantasy",
        "GTA",
        "Ghibli Anime",
        "Ghost",
        "Gundam",
        "Hologram",
        "Illustration",
        "Impressionism",
        "Ink",
        "Ink Poster",
        "Jinx",
        "Knight",
        "Lego",
        "Link",
        "Marble",
        "Mario",
        "Master Chief",
        "Mech",
        "Minecraft",
        "Mystique",
        "Naruto",
        "Neon Dream",
        "No Art Style",
        "Oil Painting",
        "On Fire",
        "Origami",
        "Painterly Anime",
        "Pixar",
        "Pixel",
        "Power Armor",
        "Power Ranger",
        "Radiant Anime",
        "Realistic Anime",
        "Realistic Pixar",
        "Retro Anime",
        "Retro Sci-Fi",
        "Samurai",
        "Samurai Bot",
        "Sharp Anime",
        "Soft Anime",
        "Solid Snake",
        "Spartan",
        "Starfield",
        "Street Fighter",
        "Studio Ghibli",
        "Sub-Zero",
        "The Void",
        "Tomb Raider",
        "Underwater",
        "Van Gogh",
        "Viking",
        "Watercolor",
        "Western Anime",
        "Wu Kong",
        "Wuxia Anime",
        "Zelda",
    ] = pydantic.Field(
        alias="art_style",
    )
    model: typing.Optional[
        typing_extensions.Literal[
            "3D Anime",
            "Absolute Reality",
            "Dreamshaper",
            "Flat 2D Anime",
            "Kaywaii",
            "Soft Anime",
            "Western Anime",
            "default",
        ]
    ] = pydantic.Field(alias="model", default=None)
    prompt: typing.Optional[str] = pydantic.Field(alias="prompt", default=None)
    prompt_type: typing.Optional[
        typing_extensions.Literal["append_default", "custom", "default"]
    ] = pydantic.Field(alias="prompt_type", default=None)
    version: typing.Optional[typing_extensions.Literal["default", "v1", "v2"]] = (
        pydantic.Field(alias="version", default=None)
    )
