"""
Generated by Sideko (sideko.dev)
"""

import typing_extensions
import pydantic


class PostV1AiImageGeneratorBodyStyle(typing_extensions.TypedDict):
    """ """

    prompt: typing_extensions.Required[str]


class _SerializerPostV1AiImageGeneratorBodyStyle(pydantic.BaseModel):
    """
    Serializer for PostV1AiImageGeneratorBodyStyle handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prompt: str = pydantic.Field(alias="prompt")
