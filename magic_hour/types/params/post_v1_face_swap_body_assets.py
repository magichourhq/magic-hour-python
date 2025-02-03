import typing
import typing_extensions
import pydantic


class PostV1FaceSwapBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for face swap. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
    """

    image_file_path: typing_extensions.Required[str]
    """
    The path of the input image. This value can be either the `file_path` field from the response of the [upload urls API](/docs/api/tag/files/post/v1/files/upload-urls), or the url of the file.
    """

    video_file_path: typing_extensions.NotRequired[str]
    """
    The path of the input video. This is the `file_path` field from the response of the [upload urls API](/docs/api/tag/files/post/v1/files/upload-urls). This field is required if `video_source` is `file`
    """

    video_source: typing_extensions.Required[
        typing_extensions.Literal["file", "youtube"]
    ]

    youtube_url: typing_extensions.NotRequired[str]
    """
    Using a youtube video as the input source. This field is required if `video_source` is `youtube`
    """


class _SerializerPostV1FaceSwapBodyAssets(pydantic.BaseModel):
    """
    Serializer for PostV1FaceSwapBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    image_file_path: str = pydantic.Field(
        alias="image_file_path",
    )
    video_file_path: typing.Optional[str] = pydantic.Field(
        alias="video_file_path", default=None
    )
    video_source: typing_extensions.Literal["file", "youtube"] = pydantic.Field(
        alias="video_source",
    )
    youtube_url: typing.Optional[str] = pydantic.Field(
        alias="youtube_url", default=None
    )
