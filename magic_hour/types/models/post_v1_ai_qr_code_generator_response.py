"""
Generated by Sideko (sideko.dev)
"""

import pydantic


class PostV1AiQrCodeGeneratorResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    frame_cost: float = pydantic.Field(alias="frame_cost")
    id: str = pydantic.Field(alias="id")
