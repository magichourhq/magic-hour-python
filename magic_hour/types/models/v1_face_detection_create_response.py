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
    The id of the task
    """
