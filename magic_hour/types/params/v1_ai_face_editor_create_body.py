import pydantic
import typing
import typing_extensions

from .v1_ai_face_editor_create_body_assets import (
    V1AiFaceEditorCreateBodyAssets,
    _SerializerV1AiFaceEditorCreateBodyAssets,
)
from .v1_ai_face_editor_create_body_style import (
    V1AiFaceEditorCreateBodyStyle,
    _SerializerV1AiFaceEditorCreateBodyStyle,
)


class V1AiFaceEditorCreateBody(typing_extensions.TypedDict):
    """
    V1AiFaceEditorCreateBody
    """

    assets: typing_extensions.Required[V1AiFaceEditorCreateBodyAssets]
    """
    Provide the assets for face editor
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image. This value is mainly used for your own identification of the image.
    """

    style: typing_extensions.Required[V1AiFaceEditorCreateBodyStyle]
    """
    Face editing parameters
    """


class _SerializerV1AiFaceEditorCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiFaceEditorCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1AiFaceEditorCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    style: _SerializerV1AiFaceEditorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
