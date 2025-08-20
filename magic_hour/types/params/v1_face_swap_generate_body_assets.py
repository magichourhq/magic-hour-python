import pydantic
import typing
import typing_extensions

from .v1_face_swap_generate_body_assets_face_mappings_item import (
    V1FaceSwapGenerateBodyAssetsFaceMappingsItem,
)


class V1FaceSwapGenerateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for face swap. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
    """

    face_mappings: typing_extensions.NotRequired[
        typing.List[V1FaceSwapGenerateBodyAssetsFaceMappingsItem]
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

    image_file_path: typing_extensions.NotRequired[str]
    """
    The path of the input image with the face to be swapped.  The value is required if `face_swap_mode` is `all-faces`. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """

    video_file_path: typing_extensions.NotRequired[str]
    """
    Required if `video_source` is `file`. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """

    video_source: typing_extensions.Required[
        typing_extensions.Literal["file", "youtube"]
    ]

    youtube_url: typing_extensions.NotRequired[str]
    """
    Using a youtube video as the input source. This field is required if `video_source` is `youtube`
    """
