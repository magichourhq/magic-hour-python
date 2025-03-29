import pydantic


class V1ImageProjectsGetResponseError(pydantic.BaseModel):
    """
    In the case of an error, this object will contain the error encountered during video render
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
