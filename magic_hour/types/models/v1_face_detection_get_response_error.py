import pydantic


class V1FaceDetectionGetResponseError(pydantic.BaseModel):
    """
    Why the face detection failed. Present only when `status` is `error`; `null` otherwise.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    code: str = pydantic.Field(
        alias="code",
    )
    """
    An error code to indicate why a failure happened.
    """
    message: str = pydantic.Field(
        alias="message",
    )
    """
    Details on the reason why a failure happened.
    """
