import pydantic
import typing
import typing_extensions

from .get_v1_video_projects_id_response_download import (
    GetV1VideoProjectsIdResponseDownload,
)
from .get_v1_video_projects_id_response_downloads_item import (
    GetV1VideoProjectsIdResponseDownloadsItem,
)
from .get_v1_video_projects_id_response_error import GetV1VideoProjectsIdResponseError


class GetV1VideoProjectsIdResponse(pydantic.BaseModel):
    """
    Success
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: str = pydantic.Field(
        alias="created_at",
    )
    download: typing.Optional[GetV1VideoProjectsIdResponseDownload] = pydantic.Field(
        alias="download",
    )
    """
    Deprecated: Please use `.downloads` instead. The download url and expiration date of the video project
    """
    downloads: typing.List[GetV1VideoProjectsIdResponseDownloadsItem] = pydantic.Field(
        alias="downloads",
    )
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Indicates whether the resource is deleted
    """
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    """
    The end time of the input video in seconds
    """
    error: typing.Optional[GetV1VideoProjectsIdResponseError] = pydantic.Field(
        alias="error",
    )
    """
    In the case of an error, this object will contain the error encountered during video render
    """
    fps: float = pydantic.Field(
        alias="fps",
    )
    """
    Frame rate of the video. If the status is not 'complete', the frame rate is an estimate and will be adjusted when the video completes.
    """
    height: int = pydantic.Field(
        alias="height",
    )
    """
    The height of the final output video. The maximum height depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique ID of the video. This value can be used in the [get video project API](https://docs.magichour.ai/api-reference/video-projects/get-video-details) to fetch additional details such as status
    """
    name: typing.Optional[str] = pydantic.Field(
        alias="name",
    )
    """
    The name of the video.
    """
    start_seconds: float = pydantic.Field(
        alias="start_seconds",
    )
    """
    The start time of the input video in seconds
    """
    status: typing_extensions.Literal[
        "canceled", "complete", "draft", "error", "queued", "rendering"
    ] = pydantic.Field(
        alias="status",
    )
    """
    The status of the video.
    """
    total_frame_cost: int = pydantic.Field(
        alias="total_frame_cost",
    )
    """
    The amount of frames used to generate the video. If the status is not 'complete', the cost is an estimate and will be adjusted when the video completes.
    """
    type_field: typing_extensions.Literal[
        "ANIMATION",
        "AUTO_SUBTITLE",
        "FACE_SWAP",
        "IMAGE_TO_VIDEO",
        "LIP_SYNC",
        "TEXT_TO_VIDEO",
        "VIDEO_TO_VIDEO",
    ] = pydantic.Field(
        alias="type",
    )
    width: int = pydantic.Field(
        alias="width",
    )
    """
    The width of the final output video. The maximum width depends on your subscription. Please refer to our [pricing page](https://magichour.ai/pricing) for more details
    """
