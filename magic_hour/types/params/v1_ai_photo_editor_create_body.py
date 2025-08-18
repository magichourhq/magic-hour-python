import pydantic
import typing
import typing_extensions

from .v1_ai_photo_editor_create_body_assets import (
    V1AiPhotoEditorCreateBodyAssets,
    _SerializerV1AiPhotoEditorCreateBodyAssets,
)
from .v1_ai_photo_editor_create_body_style import (
    V1AiPhotoEditorCreateBodyStyle,
    _SerializerV1AiPhotoEditorCreateBodyStyle,
)


class V1AiPhotoEditorCreateBody(typing_extensions.TypedDict):
    """
    V1AiPhotoEditorCreateBody
    """

    assets: typing_extensions.Required[V1AiPhotoEditorCreateBodyAssets]
    """
    Provide the assets for photo editor
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image. This value is mainly used for your own identification of the image.
    """

    resolution: typing_extensions.Required[int]
    """
    The resolution of the final output image. The allowed value is based on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
    """

    steps: typing_extensions.NotRequired[int]
    """
    Deprecated: Please use `.style.steps` instead. Number of iterations used to generate the output. Higher values improve quality and increase the strength of the prompt but increase processing time.
    """

    style: typing_extensions.Required[V1AiPhotoEditorCreateBodyStyle]


class _SerializerV1AiPhotoEditorCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiPhotoEditorCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1AiPhotoEditorCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    resolution: int = pydantic.Field(
        alias="resolution",
    )
    steps: typing.Optional[int] = pydantic.Field(alias="steps", default=None)
    style: _SerializerV1AiPhotoEditorCreateBodyStyle = pydantic.Field(
        alias="style",
    )
