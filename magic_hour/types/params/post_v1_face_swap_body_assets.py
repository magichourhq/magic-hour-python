"""
Generated by Sideko (sideko.dev)
"""

import typing
import typing_extensions
import pydantic


class PostV1FaceSwapBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for face swap. For video, The &#x60;video_source&#x60; field determines whether &#x60;video_file_path&#x60; or &#x60;youtube_url&#x60; field is used
    """

    image_file_path: typing_extensions.Required[str]
    video_file_path: typing_extensions.NotRequired[str]
    video_source: typing_extensions.Required[
        typing_extensions.Literal["file", "youtube"]
    ]
    youtube_url: typing_extensions.NotRequired[str]


class _SerializerPostV1FaceSwapBodyAssets(pydantic.BaseModel):
    """
    Serializer for PostV1FaceSwapBodyAssets handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    image_file_path: str = pydantic.Field(alias="image_file_path")
    video_file_path: typing.Optional[str] = pydantic.Field(
        alias="video_file_path", default=None
    )
    video_source: typing_extensions.Literal["file", "youtube"] = pydantic.Field(
        alias="video_source"
    )
    youtube_url: typing.Optional[str] = pydantic.Field(
        alias="youtube_url", default=None
    )
