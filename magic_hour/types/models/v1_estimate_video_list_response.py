import pydantic


class V1EstimateVideoListResponse(pydantic.BaseModel):
    """
    Success
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    estimated_credits: int = pydantic.Field(
        alias="estimated_credits",
    )
    """
    Credits a create request with these fields charges.
    """
