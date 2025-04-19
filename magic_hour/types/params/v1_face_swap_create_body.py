import pydantic
import typing
import typing_extensions

from .v1_face_swap_create_body_assets import (
    V1FaceSwapCreateBodyAssets,
    _SerializerV1FaceSwapCreateBodyAssets,
)


class V1FaceSwapCreateBody(typing_extensions.TypedDict):
    """
    V1FaceSwapCreateBody
    """

    assets: typing_extensions.Required[V1FaceSwapCreateBodyAssets]
    """
    Provide the assets for face swap. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
    """

    end_seconds: typing_extensions.Required[float]
    """
    The end time of the input video in seconds
    """

    height: typing_extensions.NotRequired[int]
    """
    Used to determine the dimensions of the output video. 
      
    * If height is provided, width will also be required. The larger value between width and height will be used to determine the maximum output resolution while maintaining the original aspect ratio.
    * If both height and width are omitted, the video will be resized according to your subscription's maximum resolution, while preserving aspect ratio.
    
    Note: if the video's original resolution is less than the maximum, the video will not be resized.
    
    See our [pricing page](https://magichour.ai/pricing) for more details.
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of video
    """

    start_seconds: typing_extensions.Required[float]
    """
    The start time of the input video in seconds
    """

    width: typing_extensions.NotRequired[int]
    """
    Used to determine the dimensions of the output video. 
      
    * If width is provided, height will also be required. The larger value between width and height will be used to determine the maximum output resolution while maintaining the original aspect ratio.
    * If both height and width are omitted, the video will be resized according to your subscription's maximum resolution, while preserving aspect ratio.
    
    Note: if the video's original resolution is less than the maximum, the video will not be resized.
    
    See our [pricing page](https://magichour.ai/pricing) for more details.
    """


class _SerializerV1FaceSwapCreateBody(pydantic.BaseModel):
    """
    Serializer for V1FaceSwapCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1FaceSwapCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    height: typing.Optional[int] = pydantic.Field(alias="height", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    start_seconds: float = pydantic.Field(
        alias="start_seconds",
    )
    width: typing.Optional[int] = pydantic.Field(alias="width", default=None)
