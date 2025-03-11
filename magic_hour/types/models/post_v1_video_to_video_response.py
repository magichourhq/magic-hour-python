import pydantic


class PostV1VideoToVideoResponse(pydantic.BaseModel):
    """
    Success
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    estimated_frame_cost: int = pydantic.Field(
        alias="estimated_frame_cost",
    )
    """
    Estimated cost of the video in terms of number of frames needed to render the video. Frames will be adjusted when the video completes
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique ID of the video. This value can be used in the [get video project API](https://docs.magichour.ai/api-reference/video-projects/get-video-details) to fetch additional details such as status
    """
