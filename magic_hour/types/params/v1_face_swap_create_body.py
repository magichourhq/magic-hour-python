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
