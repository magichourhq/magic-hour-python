import pydantic
import typing
import typing_extensions

from .post_v1_ai_photo_editor_body_assets import (
    PostV1AiPhotoEditorBodyAssets,
    _SerializerPostV1AiPhotoEditorBodyAssets,
)
from .post_v1_ai_photo_editor_body_style import (
    PostV1AiPhotoEditorBodyStyle,
    _SerializerPostV1AiPhotoEditorBodyStyle,
)


class PostV1AiPhotoEditorBody(typing_extensions.TypedDict):
    """
    PostV1AiPhotoEditorBody
    """

    assets: typing_extensions.Required[PostV1AiPhotoEditorBodyAssets]
    """
    Provide the assets for photo editor
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image
    """

    resolution: typing_extensions.Required[int]
    """
    The resolution of the final output image. The allowed value is based on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
    """

    steps: typing_extensions.NotRequired[int]
    """
    Deprecated: Please use `.style.steps` instead. Number of iterations used to generate the output. Higher values improve quality and increase the strength of the prompt but increase processing time.
    """

    style: typing_extensions.Required[PostV1AiPhotoEditorBodyStyle]


class _SerializerPostV1AiPhotoEditorBody(pydantic.BaseModel):
    """
    Serializer for PostV1AiPhotoEditorBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerPostV1AiPhotoEditorBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    resolution: int = pydantic.Field(
        alias="resolution",
    )
    steps: typing.Optional[int] = pydantic.Field(alias="steps", default=None)
    style: _SerializerPostV1AiPhotoEditorBodyStyle = pydantic.Field(
        alias="style",
    )
