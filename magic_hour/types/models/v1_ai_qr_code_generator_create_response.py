import pydantic


class V1AiQrCodeGeneratorCreateResponse(pydantic.BaseModel):
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
    The amount of credits deducted from your account to generate the image. We charge credits right when the request is made. 
    
    If an error occurred while generating the image(s), credits will be refunded and this field will be updated to include the refund.
    """
    frame_cost: int = pydantic.Field(
        alias="frame_cost",
    )
    """
    Deprecated: Previously represented the number of frames (original name of our credit system) used for image generation. Use 'credits_charged' instead.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique ID of the image. This value can be used in the [get image project API](https://docs.magichour.ai/api-reference/image-projects/get-image-details) to fetch additional details such as status
    """
