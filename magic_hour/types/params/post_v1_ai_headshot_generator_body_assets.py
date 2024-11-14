"""
Generated by Sideko (sideko.dev)
"""

import typing_extensions
import pydantic


class PostV1AiHeadshotGeneratorBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for headshot photo
    """

    image_file_path: typing_extensions.Required[str]


class _SerializerPostV1AiHeadshotGeneratorBodyAssets(pydantic.BaseModel):
    """
    Serializer for PostV1AiHeadshotGeneratorBodyAssets handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    image_file_path: str = pydantic.Field(alias="image_file_path")