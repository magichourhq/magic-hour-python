import pydantic
import typing
import typing_extensions

from .v1_face_swap_photo_generate_body_assets_face_mappings_item import (
    V1FaceSwapPhotoGenerateBodyAssetsFaceMappingsItem,
)


class V1FaceSwapPhotoGenerateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for face swap photo
    """

    face_mappings: typing_extensions.NotRequired[
        typing.List[V1FaceSwapPhotoGenerateBodyAssetsFaceMappingsItem]
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
    This is the image from which the face is extracted. The value is required if `face_swap_mode` is `all-faces`. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """

    target_file_path: typing_extensions.Required[str]
    """
    This is the image where the face from the source image will be placed. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """
