import pydantic


class GetV1ImageProjectsIdResponseDownloadsItem(pydantic.BaseModel):
    """
    The download url and expiration date of the image project
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    expires_at: str = pydantic.Field(
        alias="expires_at",
    )
    url: str = pydantic.Field(
        alias="url",
    )
