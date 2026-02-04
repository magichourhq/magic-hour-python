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
    - `qwen-edit` - 10 credits/image
      - Available for tiers: free, creator, pro, business
      - Image count allowed: 1
      - Max additional input images: 2
    - `nano-banana` - 50 credits/image
      - Available for tiers: free, creator, pro, business
      - Image count allowed: 1
      - Max additional input images: 9
    - `seedream-v4` - 50 credits/image
      - Available for tiers: free, creator, pro, business
      - Image count allowed: 1
      - Max additional input images: 9
    - `nano-banana-pro` - 150 credits/image
      - Available for tiers: creator, pro, business
      - Image count allowed: 1, 4, 9, 16
      - Max additional input images: 9
    - `seedream-v4.5` - 100 credits/image
      - Available for tiers: creator, pro, business
      - Image count allowed: 1
      - Max additional input images: 9
    
    """

    name: typing_extensions.NotRequired[str]
    """
    Give your image a custom name for easy identification.
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
            "nano-banana-pro",
            "qwen-edit",
            "seedream-v4",
            "seedream-v4.5",
        ]
    ] = pydantic.Field(alias="model", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    style: _SerializerV1AiImageEditorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
