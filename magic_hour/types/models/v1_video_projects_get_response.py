import pydantic
import typing
import typing_extensions

from .v1_video_projects_get_response_download import V1VideoProjectsGetResponseDownload
from .v1_video_projects_get_response_downloads_item import (
    V1VideoProjectsGetResponseDownloadsItem,
)
from .v1_video_projects_get_response_error import V1VideoProjectsGetResponseError


class V1VideoProjectsGetResponse(pydantic.BaseModel):
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
    credits_charged: int = pydantic.Field(
        alias="credits_charged",
    )
    """
    The amount of credits deducted from your account to generate the video. If the status is not 'complete', this value is an estimate and may be adjusted upon completion based on the actual FPS of the output video. 
    
    If video generation fails, credits will be refunded, and this field will be updated to include the refund.
    """
    download: typing.Optional[V1VideoProjectsGetResponseDownload] = pydantic.Field(
        alias="download",
    )
    """
    Deprecated: Please use `.downloads` instead. The download url and expiration date of the video project
    """
    downloads: typing.List[V1VideoProjectsGetResponseDownloadsItem] = pydantic.Field(
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
    The end time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.1, and more than the start_seconds.
    """
    error: typing.Optional[V1VideoProjectsGetResponseError] = pydantic.Field(
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
    The height of the final output video. A value of -1 indicates the height can be ignored.
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
    The start time of the input video in seconds. This value is used to trim the input video. The value must be greater than 0.
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
    Deprecated: Previously represented the number of frames (original name of our credit system) used for video generation. Use 'credits_charged' instead.
    
    The amount of frames used to generate the video. If the status is not 'complete', the cost is an estimate and will be adjusted when the video completes.
    """
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    The type of the video project. Possible values are ANIMATION, IMAGE_TO_VIDEO, VIDEO_TO_VIDEO, TEXT_TO_VIDEO, FACE_SWAP, LIP_SYNC, AUTO_SUBTITLE, TALKING_PHOTO, UGC_AD
    """
    width: int = pydantic.Field(
        alias="width",
    )
    """
    The width of the final output video. A value of -1 indicates the width can be ignored.
    """
