import pydantic
import typing
import typing_extensions

from .v1_ai_image_editor_create_body_assets import (
    V1AiImageEditorCreateBodyAssets,
    _SerializerV1AiImageEditorCreateBodyAssets,
)
from .v1_ai_image_editor_create_body_style import (
    V1AiImageEditorCreateBodyStyle,
    _SerializerV1AiImageEditorCreateBodyStyle,
)


class V1AiImageEditorCreateBody(typing_extensions.TypedDict):
    """
    V1AiImageEditorCreateBody
    """

    aspect_ratio: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "16:9", "1:1", "2:3", "3:2", "4:3", "4:5", "9:16", "auto"
        ]
    ]
    """
    The aspect ratio of the output image(s). If not specified, defaults to `auto`.
    """

    assets: typing_extensions.Required[V1AiImageEditorCreateBodyAssets]
    """
    Provide the assets for image edit
    """

    image_count: typing_extensions.NotRequired[float]
    """
    Number of images to generate. Maximum varies by model. Defaults to 1 if not specified.
    """

    model: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "default",
            "nano-banana",
            "nano-banana-2",
            "nano-banana-pro",
            "qwen-edit",
            "seedream-v4",
            "seedream-v4.5",
        ]
    ]
    """
    The AI model to use for image editing. Each model has different capabilities and costs.
    
    **Models:**
    - `default` - Use the model we recommend, which will change over time. This is recommended unless you need a specific model. This is the default behavior.
    - `qwen-edit` - from 10 credits/image
      - Supported resolutions: 640px, 1k, 2k
      - Available for tiers: free, creator, pro, business
      - Image count allowed: 1, 2, 3, 4
      - Max additional input images: 2
    - `nano-banana` - from 50 credits/image
      - Supported resolutions: 640px, 1k
      - Available for tiers: free, creator, pro, business
      - Image count allowed: 1, 2, 3, 4
      - Max additional input images: 9
    - `nano-banana-2` - from 100 credits/image
      - Supported resolutions: 640px, 1k, 2k, 4k
      - Available for tiers: free, creator, pro, business
      - Image count allowed: 1, 2, 3, 4
      - Max additional input images: 9
    - `seedream-v4` - from 40 credits/image
      - Supported resolutions: 640px, 1k, 2k, 4k
      - Available for tiers: free, creator, pro, business
      - Image count allowed: 1, 2, 3, 4
      - Max additional input images: 9
    - `nano-banana-pro` - from 150 credits/image
      - Supported resolutions: 1k, 2k, 4k
      - Available for tiers: creator, pro, business
      - Image count allowed: 1, 4, 9, 16
      - Max additional input images: 9
    - `seedream-v4.5` - from 50 credits/image
      - Supported resolutions: 640px, 1k, 2k, 4k
      - Available for tiers: creator, pro, business
      - Image count allowed: 1, 2, 3, 4
      - Max additional input images: 9
    
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your image a custom name for easy identification.
    """

    resolution: typing_extensions.NotRequired[
        typing_extensions.Literal["1k", "2k", "4k", "640px", "auto"]
    ]
    """
    Maximum resolution (longest edge) for the output image.
    
    **Options:**
    - `640px` — up to 640px
    - `1k` — up to 1024px
    - `2k` — up to 2048px
    - `4k` — up to 4096px
    - `auto` — **Deprecated.** Mapped server-side from your subscription tier to the best matching resolution the model supports
    
    **Per-model support:**
    - `qwen-edit` - 640px, 1k, 2k
    - `nano-banana` - 640px, 1k
    - `nano-banana-2` - 640px, 1k, 2k, 4k
    - `seedream-v4` - 640px, 1k, 2k, 4k
    - `nano-banana-pro` - 1k, 2k, 4k
    - `seedream-v4.5` - 640px, 1k, 2k, 4k
    
    Note: Resolution availability depends on the model and your subscription tier.
    """

    style: typing_extensions.Required[V1AiImageEditorCreateBodyStyle]


class _SerializerV1AiImageEditorCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiImageEditorCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    aspect_ratio: typing.Optional[
        typing_extensions.Literal[
            "16:9", "1:1", "2:3", "3:2", "4:3", "4:5", "9:16", "auto"
        ]
    ] = pydantic.Field(alias="aspect_ratio", default=None)
    assets: _SerializerV1AiImageEditorCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    image_count: typing.Optional[float] = pydantic.Field(
        alias="image_count", default=None
    )
    model: typing.Optional[
        typing_extensions.Literal[
            "default",
            "nano-banana",
            "nano-banana-2",
            "nano-banana-pro",
            "qwen-edit",
            "seedream-v4",
            "seedream-v4.5",
        ]
    ] = pydantic.Field(alias="model", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    resolution: typing.Optional[
        typing_extensions.Literal["1k", "2k", "4k", "640px", "auto"]
    ] = pydantic.Field(alias="resolution", default=None)
    style: _SerializerV1AiImageEditorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
