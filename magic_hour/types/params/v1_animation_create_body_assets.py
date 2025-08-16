import pydantic
import typing
import typing_extensions


class V1AnimationCreateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for animation.
    """

    audio_file_path: typing_extensions.NotRequired[str]
    """
    The path of the input audio. This field is required if `audio_source` is `file`. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.
    
    """

    audio_source: typing_extensions.Required[
        typing_extensions.Literal["file", "none", "youtube"]
    ]
    """
    Optionally add an audio source if you'd like to incorporate audio into your video
    """

    image_file_path: typing_extensions.NotRequired[str]
    """
    An initial image to use a the first frame of the video. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.
    
    """

    youtube_url: typing_extensions.NotRequired[str]
    """
    Using a youtube video as the input source. This field is required if `audio_source` is `youtube`
    """


class _SerializerV1AnimationCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1AnimationCreateBodyAssets handling case conversions
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
