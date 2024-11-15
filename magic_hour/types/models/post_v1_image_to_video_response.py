"""
Generated by Sideko (sideko.dev)
"""

import pydantic


class PostV1ImageToVideoResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    estimated_frame_cost: float = pydantic.Field(alias="estimated_frame_cost")
    id: str = pydantic.Field(alias="id")
