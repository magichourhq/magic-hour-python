import pydantic
import typing
import typing_extensions


class PostV1VideoToVideoBodyStyle(typing_extensions.TypedDict):
    """
    PostV1VideoToVideoBodyStyle
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
            "Celestial Skin",
            "Clay",
            "Comic",
            "Cyberpunk",
            "Cypher",
            "Dark Fantasy",
            "Dragonball Z",
            "Future Bot",
            "Futuristic Fantasy",
            "GTA",
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
            "Master Chief",
            "Mech",
            "Minecraft",
            "Naruto",
            "Neon Dream",
            "Oil Painting",
            "On Fire",
            "Origami",
            "Pixel",
            "Power Armor",
            "Power Ranger",
            "Retro Anime",
            "Retro Sci-Fi",
            "Samurai",
            "Samurai Bot",
            "Solid Snake",
            "Spartan",
            "Starfield",
            "Street Fighter",
            "Studio Ghibli",
            "Sub-Zero",
            "The Void",
            "Underwater",
            "Van Gogh",
            "Viking",
            "Watercolor",
            "Wu Kong",
            "Zelda",
        ]
    ]

    model: typing_extensions.Required[
        typing_extensions.Literal[
            "Absolute Reality", "Dreamshaper", "Flat 2D Anime", "default"
        ]
    ]
    """
    * `Dreamshaper` - a good all-around model that works for both animations as well as realism. 
    * `Absolute Reality` - better at realism, but you'll often get similar results with Dreamshaper as well. 
    * `Flat 2D Anime` - best for a flat illustration style that's common in most anime.
    * `default` - use the default recommended model for the selected art style.
    """

    prompt: typing_extensions.Required[typing.Optional[str]]
    """
    The prompt used for the video. Prompt is required if `prompt_type` is `custom` or `append_default`. If `prompt_type` is `default`, then the `prompt` value passed will be ignored.
    """

    prompt_type: typing_extensions.Required[
        typing_extensions.Literal["append_default", "custom", "default"]
    ]
    """
    * `default` - Use the default recommended prompt for the art style.
    * `custom` - Only use the prompt passed in the API. Note: for v1, lora prompt will still be auto added to apply the art style properly.
    * `append_default` - Add the default recommended prompt to the end of the prompt passed in the API.
    """

    version: typing_extensions.Required[
        typing_extensions.Literal["default", "v1", "v2"]
    ]
    """
    * `v1` - more detail, closer prompt adherence, and frame-by-frame previews.
    * `v2` - faster, more consistent, and less noisy.
    * `default` - use the default version for the selected art style.
    """


class _SerializerPostV1VideoToVideoBodyStyle(pydantic.BaseModel):
    """
    Serializer for PostV1VideoToVideoBodyStyle handling case conversions
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
        "Celestial Skin",
        "Clay",
        "Comic",
        "Cyberpunk",
        "Cypher",
        "Dark Fantasy",
        "Dragonball Z",
        "Future Bot",
        "Futuristic Fantasy",
        "GTA",
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
        "Master Chief",
        "Mech",
        "Minecraft",
        "Naruto",
        "Neon Dream",
        "Oil Painting",
        "On Fire",
        "Origami",
        "Pixel",
        "Power Armor",
        "Power Ranger",
        "Retro Anime",
        "Retro Sci-Fi",
        "Samurai",
        "Samurai Bot",
        "Solid Snake",
        "Spartan",
        "Starfield",
        "Street Fighter",
        "Studio Ghibli",
        "Sub-Zero",
        "The Void",
        "Underwater",
        "Van Gogh",
        "Viking",
        "Watercolor",
        "Wu Kong",
        "Zelda",
    ] = pydantic.Field(
        alias="art_style",
    )
    model: typing_extensions.Literal[
        "Absolute Reality", "Dreamshaper", "Flat 2D Anime", "default"
    ] = pydantic.Field(
        alias="model",
    )
    prompt: typing.Optional[str] = pydantic.Field(
        alias="prompt",
    )
    prompt_type: typing_extensions.Literal["append_default", "custom", "default"] = (
        pydantic.Field(
            alias="prompt_type",
        )
    )
    version: typing_extensions.Literal["default", "v1", "v2"] = pydantic.Field(
        alias="version",
    )
