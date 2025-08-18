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

    assets: typing_extensions.Required[V1AiImageEditorCreateBodyAssets]
    """
    Provide the assets for image edit
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image. This value is mainly used for your own identification of the image.
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

    assets: _SerializerV1AiImageEditorCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    style: _SerializerV1AiImageEditorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
