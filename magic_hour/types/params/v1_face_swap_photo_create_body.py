import pydantic
import typing
import typing_extensions

from .v1_face_swap_photo_create_body_assets import (
    V1FaceSwapPhotoCreateBodyAssets,
    _SerializerV1FaceSwapPhotoCreateBodyAssets,
)


class V1FaceSwapPhotoCreateBody(typing_extensions.TypedDict):
    """
    V1FaceSwapPhotoCreateBody
    """

    assets: typing_extensions.Required[V1FaceSwapPhotoCreateBodyAssets]
    """
    Provide the assets for face swap photo
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image. This value is mainly used for your own identification of the image.
    """


class _SerializerV1FaceSwapPhotoCreateBody(pydantic.BaseModel):
    """
    Serializer for V1FaceSwapPhotoCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1FaceSwapPhotoCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
