import pydantic
import typing
import typing_extensions

from .post_v1_face_swap_photo_body_assets import (
    PostV1FaceSwapPhotoBodyAssets,
    _SerializerPostV1FaceSwapPhotoBodyAssets,
)


class PostV1FaceSwapPhotoBody(typing_extensions.TypedDict):
    """
    PostV1FaceSwapPhotoBody
    """

    assets: typing_extensions.Required[PostV1FaceSwapPhotoBodyAssets]
    """
    Provide the assets for face swap photo
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image
    """


class _SerializerPostV1FaceSwapPhotoBody(pydantic.BaseModel):
    """
    Serializer for PostV1FaceSwapPhotoBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerPostV1FaceSwapPhotoBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
