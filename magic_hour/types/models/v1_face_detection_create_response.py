import pydantic


class V1FaceDetectionCreateResponse(pydantic.BaseModel):
    """
    V1FaceDetectionCreateResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    credits_charged: int = pydantic.Field(
        alias="credits_charged",
    )
    """
    The credits charged for the task.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    The id of the task. Use this value in the [get face detection details API](/api-reference/files/get-face-detection-details) to get the details of the face detection task.
    """
