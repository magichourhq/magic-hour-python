"""
Generated by Sideko (sideko.dev)
"""

import typing_extensions
import pydantic


class PostV1TextToVideoBodyStyle(typing_extensions.TypedDict):
    """ """

    prompt: typing_extensions.Required[str]


class _SerializerPostV1TextToVideoBodyStyle(pydantic.BaseModel):
    """
    Serializer for PostV1TextToVideoBodyStyle handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prompt: str = pydantic.Field(alias="prompt")
