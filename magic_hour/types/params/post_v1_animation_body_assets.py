import pydantic
import typing
import typing_extensions


class PostV1AnimationBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for animation.
    """

    audio_file_path: typing_extensions.NotRequired[str]
    """
    The path of the input audio. This field is required if `audio_source` is `file`. This value can be either the `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls), or the url of the file.
    """

    audio_source: typing_extensions.Required[
        typing_extensions.Literal["file", "none", "youtube"]
    ]
    """
    Optionally add an audio source if you'd like to incorporate audio into your video
    """

    image_file_path: typing_extensions.NotRequired[str]
    """
    An initial image to use a the first frame of the video. This value can be either the `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls), or the url of the file.
    """

    youtube_url: typing_extensions.NotRequired[str]
    """
    Using a youtube video as the input source. This field is required if `audio_source` is `youtube`
    """


class _SerializerPostV1AnimationBodyAssets(pydantic.BaseModel):
    """
    Serializer for PostV1AnimationBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    audio_file_path: typing.Optional[str] = pydantic.Field(
        alias="audio_file_path", default=None
    )
    audio_source: typing_extensions.Literal["file", "none", "youtube"] = pydantic.Field(
        alias="audio_source",
    )
    image_file_path: typing.Optional[str] = pydantic.Field(
        alias="image_file_path", default=None
    )
    youtube_url: typing.Optional[str] = pydantic.Field(
        alias="youtube_url", default=None
    )
