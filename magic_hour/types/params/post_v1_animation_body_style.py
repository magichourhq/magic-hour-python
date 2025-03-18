import pydantic
import typing
import typing_extensions


class PostV1AnimationBodyStyle(typing_extensions.TypedDict):
    """
    Defines the style of the output video
    """

    art_style: typing_extensions.Required[
        typing_extensions.Literal[
            "3D Render",
            "90s Streets",
            "Abstract Minimalist",
            "Arcane",
            "Art Deco",
            "Bold Colored Illustration",
            "Cinematic Landscape",
            "Cinematic Miyazaki",
            "Cosmic",
            "Cubist",
            "Custom",
            "Cyberpunk",
            "Dark Graphic Illustration",
            "Dark Watercolor",
            "Directed by AI",
            "Double Exposure",
            "Faded Illustration",
            "Fantasy",
            "Futuristic Anime",
            "Impressionism",
            "Ink and Watercolor Portrait",
            "Inkpunk",
            "Intricate Abstract Lines Portrait",
            "Jackson Pollock",
            "Landscape Painting",
            "Low Poly",
            "Miniatures",
            "Minimal Cold Futurism",
            "Oil Painting",
            "Old School Comic",
            "Overgrown",
            "Painted Cityscape",
            "Painterly Illustration",
            "Photograph",
            "Pixar",
            "Pixel Art",
            "Postapocalyptic",
            "Sin City",
            "Soft Delicate Matte Portrait",
            "Spooky",
            "Studio Ghibli Film Still",
            "Synthwave",
            "Traditional Watercolor",
            "Van Gogh",
            "Vibrant Matte Illustration",
            "Vintage Japanese Anime",
            "Woodcut",
        ]
    ]
    """
    The art style of the final output video
    """

    art_style_custom: typing_extensions.NotRequired[str]
    """
    Describe custom art style. This field is required if `art_style` is `Custom`
    """

    camera_effect: typing_extensions.Required[
        typing_extensions.Literal[
            "Accelerate",
            "Aggressive Zoom In - Audio Sync",
            "Aggressive Zoom Out - Audio Sync",
            "Boost Zoom In",
            "Boost Zoom Out",
            "Bounce In And Out",
            "Bounce Out",
            "Bounce Out - Audio Sync",
            "Bounce and Spin - Audio Sync",
            "Bounce in Place",
            "Cog in the Machine",
            "Devolve - Audio Sync",
            "Directed by AI",
            "Dramatic Zoom In",
            "Dramatic Zoom Out",
            "Drift Spin",
            "Earthquake Bounce",
            "Earthquake Bounce - Audio Sync",
            "Evolve - Audio Sync",
            "Heartbeat",
            "Hesitate In",
            "Jump",
            "Pan Left",
            "Pan Right",
            "Pulse - Audio Sync",
            "Pusher",
            "Pusher - Audio Sync",
            "Quadrant",
            "Rise and Climb",
            "Road Trip",
            "Rodeo",
            "Roll In",
            "Roll In - Audio Sync",
            "Rolling Bounces",
            "Rubber Band",
            "Simple Zoom In",
            "Simple Zoom Out",
            "Slice Bounce",
            "Slideshow",
            "Speed of Light",
            "Spin Bounce",
            "Sway Out",
            "Sway Out - Audio Sync",
            "Tilt Down",
            "Tilt Up",
            "Traverse",
            "Tron",
            "Vertigo",
            "Vertigo - Audio Sync",
            "Zoom In - Audio Sync",
            "Zoom In and Spin - Audio Sync",
            "Zoom Out - Audio Sync",
        ]
    ]

    prompt: typing_extensions.Required[typing.Optional[str]]
    """
    The prompt used for the video. Prompt is required if `prompt_type` is `custom`. Otherwise this value is ignored
    """

    prompt_type: typing_extensions.Required[
        typing_extensions.Literal["ai_choose", "custom", "use_lyrics"]
    ]
    """
    
    * `custom` - use your own prompt for the video.
    * `use_lyrics` - Use the lyrics of the audio to create the prompt. If this option is selected, then `assets.audio_source` must be `file` or `youtube`.
    * `ai_choose` - Let AI write the prompt. If this option is selected, then `assets.audio_source` must be `file` or `youtube`.
    """

    transition_speed: typing_extensions.Required[int]
    """
    Change determines how quickly the video's content changes across frames. Higher = more rapid transitions. Lower = more stable visual experience.
    """


class _SerializerPostV1AnimationBodyStyle(pydantic.BaseModel):
    """
    Serializer for PostV1AnimationBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    art_style: typing_extensions.Literal[
        "3D Render",
        "90s Streets",
        "Abstract Minimalist",
        "Arcane",
        "Art Deco",
        "Bold Colored Illustration",
        "Cinematic Landscape",
        "Cinematic Miyazaki",
        "Cosmic",
        "Cubist",
        "Custom",
        "Cyberpunk",
        "Dark Graphic Illustration",
        "Dark Watercolor",
        "Directed by AI",
        "Double Exposure",
        "Faded Illustration",
        "Fantasy",
        "Futuristic Anime",
        "Impressionism",
        "Ink and Watercolor Portrait",
        "Inkpunk",
        "Intricate Abstract Lines Portrait",
        "Jackson Pollock",
        "Landscape Painting",
        "Low Poly",
        "Miniatures",
        "Minimal Cold Futurism",
        "Oil Painting",
        "Old School Comic",
        "Overgrown",
        "Painted Cityscape",
        "Painterly Illustration",
        "Photograph",
        "Pixar",
        "Pixel Art",
        "Postapocalyptic",
        "Sin City",
        "Soft Delicate Matte Portrait",
        "Spooky",
        "Studio Ghibli Film Still",
        "Synthwave",
        "Traditional Watercolor",
        "Van Gogh",
        "Vibrant Matte Illustration",
        "Vintage Japanese Anime",
        "Woodcut",
    ] = pydantic.Field(
        alias="art_style",
    )
    art_style_custom: typing.Optional[str] = pydantic.Field(
        alias="art_style_custom", default=None
    )
    camera_effect: typing_extensions.Literal[
        "Accelerate",
        "Aggressive Zoom In - Audio Sync",
        "Aggressive Zoom Out - Audio Sync",
        "Boost Zoom In",
        "Boost Zoom Out",
        "Bounce In And Out",
        "Bounce Out",
        "Bounce Out - Audio Sync",
        "Bounce and Spin - Audio Sync",
        "Bounce in Place",
        "Cog in the Machine",
        "Devolve - Audio Sync",
        "Directed by AI",
        "Dramatic Zoom In",
        "Dramatic Zoom Out",
        "Drift Spin",
        "Earthquake Bounce",
        "Earthquake Bounce - Audio Sync",
        "Evolve - Audio Sync",
        "Heartbeat",
        "Hesitate In",
        "Jump",
        "Pan Left",
        "Pan Right",
        "Pulse - Audio Sync",
        "Pusher",
        "Pusher - Audio Sync",
        "Quadrant",
        "Rise and Climb",
        "Road Trip",
        "Rodeo",
        "Roll In",
        "Roll In - Audio Sync",
        "Rolling Bounces",
        "Rubber Band",
        "Simple Zoom In",
        "Simple Zoom Out",
        "Slice Bounce",
        "Slideshow",
        "Speed of Light",
        "Spin Bounce",
        "Sway Out",
        "Sway Out - Audio Sync",
        "Tilt Down",
        "Tilt Up",
        "Traverse",
        "Tron",
        "Vertigo",
        "Vertigo - Audio Sync",
        "Zoom In - Audio Sync",
        "Zoom In and Spin - Audio Sync",
        "Zoom Out - Audio Sync",
    ] = pydantic.Field(
        alias="camera_effect",
    )
    prompt: typing.Optional[str] = pydantic.Field(
        alias="prompt",
    )
    prompt_type: typing_extensions.Literal["ai_choose", "custom", "use_lyrics"] = (
        pydantic.Field(
            alias="prompt_type",
        )
    )
    transition_speed: int = pydantic.Field(
        alias="transition_speed",
    )
