import pydantic
import typing
import typing_extensions

from .v1_face_swap_photo_create_body_assets_face_mappings_item import (
    V1FaceSwapPhotoCreateBodyAssetsFaceMappingsItem,
    _SerializerV1FaceSwapPhotoCreateBodyAssetsFaceMappingsItem,
)


class V1FaceSwapPhotoCreateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for face swap photo
    """

    face_mappings: typing_extensions.NotRequired[
        typing.List[V1FaceSwapPhotoCreateBodyAssetsFaceMappingsItem]
    ]
    """
    This is the array of face mappings used for multiple face swap. The value is required if `face_swap_mode` is `individual-faces`.
    """

    face_swap_mode: typing_extensions.NotRequired[
        typing_extensions.Literal["all-faces", "individual-faces"]
    ]
    """
    The mode of face swap.
    * `all-faces` - Swap all faces in the target image or video. `source_file_path` is required.
    * `individual-faces` - Swap individual faces in the target image or video. `source_faces` is required.
    """

    source_file_path: typing_extensions.NotRequired[str]
    """
    This is the image from which the face is extracted. The value is required if `face_swap_mode` is `all-faces`.
    
    This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.
    
    """

    target_file_path: typing_extensions.Required[str]
    """
    This is the image where the face from the source image will be placed. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.
    
    """


class _SerializerV1FaceSwapPhotoCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1FaceSwapPhotoCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    face_mappings: typing.Optional[
        typing.List[_SerializerV1FaceSwapPhotoCreateBodyAssetsFaceMappingsItem]
    ] = pydantic.Field(alias="face_mappings", default=None)
    face_swap_mode: typing.Optional[
        typing_extensions.Literal["all-faces", "individual-faces"]
    ] = pydantic.Field(alias="face_swap_mode", default=None)
    source_file_path: typing.Optional[str] = pydantic.Field(
        alias="source_file_path", default=None
    )
    target_file_path: str = pydantic.Field(
        alias="target_file_path",
    )
