"""
Generated by Sideko (sideko.dev)
"""

import pydantic


class PostV1ImageBackgroundRemoverResponse(pydantic.BaseModel):
    """
    Success
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    frame_cost: int = pydantic.Field(
        alias="frame_cost",
    )
    """
    The frame cost of the image generation
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique ID of the image. This value can be used in the [get image project API](/api/tag/image-projects/get/v1/image-projects/{id}) to fetch additional details such as status
    """