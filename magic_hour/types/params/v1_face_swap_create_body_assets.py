import pydantic
import typing
import typing_extensions

from .v1_face_swap_create_body_assets_face_mappings_item import (
    V1FaceSwapCreateBodyAssetsFaceMappingsItem,
    _SerializerV1FaceSwapCreateBodyAssetsFaceMappingsItem,
)


class V1FaceSwapCreateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for face swap. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
    """

    face_mappings: typing_extensions.NotRequired[
        typing.List[V1FaceSwapCreateBodyAssetsFaceMappingsItem]
    ]
    """
    This is the array of face mappings used for multiple face swap. The value is required if `face_swap_mode` is `individual-faces`.
    """

    face_swap_mode: typing_extensions.NotRequired[
        typing_extensions.Literal["all-faces", "individual-faces"]
    ]
    """
    Choose how to swap faces:
    **all-faces** (recommended) — swap all detected faces using one source image (`source_file_path` required)
    +- **individual-faces** — specify exact mappings using `face_mappings`
    """

    image_file_path: typing_extensions.NotRequired[str]
    """
    The path of the input image with the face to be swapped.  The value is required if `face_swap_mode` is `all-faces`.
    
    This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.
    
    """

    video_file_path: typing_extensions.NotRequired[str]
    """
    Your video file. Required if `video_source` is `file`. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.
    
    """

    video_source: typing_extensions.Required[
        typing_extensions.Literal["file", "youtube"]
    ]
    """
    Choose your video source.
    """

    youtube_url: typing_extensions.NotRequired[str]
    """
    YouTube URL (required if `video_source` is `youtube`).
    """


class _SerializerV1FaceSwapCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1FaceSwapCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    face_mappings: typing.Optional[
        typing.List[_SerializerV1FaceSwapCreateBodyAssetsFaceMappingsItem]
    ] = pydantic.Field(alias="face_mappings", default=None)
    face_swap_mode: typing.Optional[
        typing_extensions.Literal["all-faces", "individual-faces"]
    ] = pydantic.Field(alias="face_swap_mode", default=None)
    image_file_path: typing.Optional[str] = pydantic.Field(
        alias="image_file_path", default=None
    )
    video_file_path: typing.Optional[str] = pydantic.Field(
        alias="video_file_path", default=None
    )
    video_source: typing_extensions.Literal["file", "youtube"] = pydantic.Field(
        alias="video_source",
    )
    youtube_url: typing.Optional[str] = pydantic.Field(
        alias="youtube_url", default=None
    )
