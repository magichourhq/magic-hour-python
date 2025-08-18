import pydantic
import typing
import typing_extensions


class V1VideoToVideoCreateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for video-to-video. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
    """

    video_file_path: typing_extensions.NotRequired[str]
    """
    Required if `video_source` is `file`. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.
    
    """

    video_source: typing_extensions.Required[
        typing_extensions.Literal["file", "youtube"]
    ]

    youtube_url: typing_extensions.NotRequired[str]
    """
    Using a youtube video as the input source. This field is required if `video_source` is `youtube`
    """


class _SerializerV1VideoToVideoCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1VideoToVideoCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
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
