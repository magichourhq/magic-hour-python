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
    The mode of face swap.
    * `all-faces` - Swap all faces in the target image or video. `source_file_path` is required.
    * `individual-faces` - Swap individual faces in the target image or video. `source_faces` is required.
    """

    image_file_path: typing_extensions.NotRequired[str]
    """
    The path of the input image with the face to be swapped.  The value is required if `face_swap_mode` is `all-faces`.
    
    This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.
    
    """

    video_file_path: typing_extensions.NotRequired[str]
    """
    Required if `video_source` is `file`. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.
    
    """

    video_source: typing_extensions.Required[
        typing_extensions.Literal["file", "youtube"]
    ]

    youtube_url: typing_extensions.NotRequired[str]
    """
    Using a youtube video as the input source. This field is required if `video_source` is `youtube`
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
