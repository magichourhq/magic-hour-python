import pydantic
import typing
import typing_extensions

from .post_v1_face_swap_body_assets import (
    PostV1FaceSwapBodyAssets,
    _SerializerPostV1FaceSwapBodyAssets,
)


class PostV1FaceSwapBody(typing_extensions.TypedDict):
    """
    PostV1FaceSwapBody
    """

    assets: typing_extensions.Required[PostV1FaceSwapBodyAssets]
    """
    Provide the assets for face swap. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
    """

    end_seconds: typing_extensions.Required[float]
    """
    The end time of the input video in seconds
    """

    height: typing_extensions.Required[int]
    """
    The height of the final output video. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of video
    """

    start_seconds: typing_extensions.Required[float]
    """
    The start time of the input video in seconds
    """

    width: typing_extensions.Required[int]
    """
    The width of the final output video. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
    """


class _SerializerPostV1FaceSwapBody(pydantic.BaseModel):
    """
    Serializer for PostV1FaceSwapBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerPostV1FaceSwapBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    height: int = pydantic.Field(
        alias="height",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    start_seconds: float = pydantic.Field(
        alias="start_seconds",
    )
    width: int = pydantic.Field(
        alias="width",
    )
