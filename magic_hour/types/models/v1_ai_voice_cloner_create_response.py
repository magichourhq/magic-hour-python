import pydantic


class V1AiVoiceClonerCreateResponse(pydantic.BaseModel):
    """
    Success
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    credits_charged: int = pydantic.Field(
        alias="credits_charged",
    )
    """
    The amount of credits deducted from your account to generate the audio. We charge credits right when the request is made. 
    
    If an error occurred while generating the audio, credits will be refunded and this field will be updated to include the refund.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique ID of the audio. Use it with the [Get audio Project API](https://docs.magichour.ai/api-reference/audio-projects/get-audio-details) to fetch status and downloads.
    """
