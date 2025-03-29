import pydantic
import typing
import typing_extensions

from .v1_lip_sync_create_body_assets import (
    V1LipSyncCreateBodyAssets,
    _SerializerV1LipSyncCreateBodyAssets,
)


class V1LipSyncCreateBody(typing_extensions.TypedDict):
    """
    V1LipSyncCreateBody
    """

    assets: typing_extensions.Required[V1LipSyncCreateBodyAssets]
    """
    Provide the assets for lip-sync. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
    """

    end_seconds: typing_extensions.Required[float]
    """
    The end time of the input video in seconds
    """

    height: typing_extensions.Required[int]
    """
    The height of the final output video. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
    """

    max_fps_limit: typing_extensions.NotRequired[float]
    """
    Defines the maximum FPS (frames per second) for the output video. If the input video's FPS is lower than this limit, the output video will retain the input FPS. This is useful for reducing unnecessary frame usage in scenarios where high FPS is not required.
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


class _SerializerV1LipSyncCreateBody(pydantic.BaseModel):
    """
    Serializer for V1LipSyncCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1LipSyncCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    height: int = pydantic.Field(
        alias="height",
    )
    max_fps_limit: typing.Optional[float] = pydantic.Field(
        alias="max_fps_limit", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    start_seconds: float = pydantic.Field(
        alias="start_seconds",
    )
    width: int = pydantic.Field(
        alias="width",
    )
