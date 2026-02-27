import pydantic
import typing
import typing_extensions

from .v1_ai_image_generator_create_body_style import (
    V1AiImageGeneratorCreateBodyStyle,
    _SerializerV1AiImageGeneratorCreateBodyStyle,
)


class V1AiImageGeneratorCreateBody(typing_extensions.TypedDict):
    """
    V1AiImageGeneratorCreateBody
    """

    aspect_ratio: typing_extensions.NotRequired[
        typing_extensions.Literal["16:9", "1:1", "9:16"]
    ]
    """
    The aspect ratio of the output image(s). If not specified, defaults to `1:1` (square).
    """

    image_count: typing_extensions.Required[int]
    """
    Number of images to generate. Maximum varies by model.
    """

    model: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "default",
            "flux-schnell",
            "nano-banana",
            "nano-banana-2",
            "nano-banana-pro",
            "seedream",
            "z-image-turbo",
        ]
    ]
    """
    The AI model to use for image generation. Each model has different capabilities and costs.
    
    **Models:**
    - `default` - Use the model we recommend, which will change over time. This is recommended unless you need a specific model. This is the default behavior.
    - `flux-schnell` - 5 credits/image
      - Supported resolutions: auto
      - Available for tiers: free, creator, pro, business
      - Image count allowed: 1, 2, 3, 4
    - `z-image-turbo` - 5 credits/image
      - Supported resolutions: auto, 2k
      - Available for tiers: free, creator, pro, business
      - Image count allowed: 1, 2, 3, 4
    - `seedream` - 30 credits/image
      - Supported resolutions: auto, 2k, 4k
      - Available for tiers: free, creator, pro, business
      - Image count allowed: 1, 2, 3, 4
    - `nano-banana` - 50 credits/image
      - Supported resolutions: auto
      - Available for tiers: free, creator, pro, business
      - Image count allowed: 1, 2, 3, 4
    - `nano-banana-2` - 100 credits/image
      - Supported resolutions: auto
      - Available for tiers: free, creator, pro, business
      - Image count allowed: 1, 2, 3, 4
    - `nano-banana-pro` - 150 credits/image
      - Supported resolutions: auto
      - Available for tiers: creator, pro, business
      - Image count allowed: 1, 4, 9, 16
    
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your image a custom name for easy identification.
    """

    orientation: typing_extensions.NotRequired[
        typing_extensions.Literal["landscape", "portrait", "square"]
    ]
    """
    DEPRECATED: Use `aspect_ratio` instead. 
              
    The orientation of the output image(s). `aspect_ratio` takes precedence when `orientation` if both are provided.
    """

    resolution: typing_extensions.NotRequired[
        typing_extensions.Literal["2k", "4k", "auto"]
    ]
    """
    Maximum resolution for the generated image.
    
    **Options:**
    - `auto` - Automatic resolution (all tiers, default)
    - `2k` - Up to 2048px (requires Pro or Business tier)
    - `4k` - Up to 4096px (requires Business tier)
    
    Note: Resolution availability depends on the model and your subscription tier. See `model` field for which resolutions each model supports. Defaults to `auto` if not specified.
    """

    style: typing_extensions.Required[V1AiImageGeneratorCreateBodyStyle]
    """
    The art style to use for image generation.
    """


class _SerializerV1AiImageGeneratorCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiImageGeneratorCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    aspect_ratio: typing.Optional[typing_extensions.Literal["16:9", "1:1", "9:16"]] = (
        pydantic.Field(alias="aspect_ratio", default=None)
    )
    image_count: int = pydantic.Field(
        alias="image_count",
    )
    model: typing.Optional[
        typing_extensions.Literal[
            "default",
            "flux-schnell",
            "nano-banana",
            "nano-banana-2",
            "nano-banana-pro",
            "seedream",
            "z-image-turbo",
        ]
    ] = pydantic.Field(alias="model", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    orientation: typing.Optional[
        typing_extensions.Literal["landscape", "portrait", "square"]
    ] = pydantic.Field(alias="orientation", default=None)
    resolution: typing.Optional[typing_extensions.Literal["2k", "4k", "auto"]] = (
        pydantic.Field(alias="resolution", default=None)
    )
    style: _SerializerV1AiImageGeneratorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
