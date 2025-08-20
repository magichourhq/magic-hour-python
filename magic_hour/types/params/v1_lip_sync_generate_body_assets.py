import pydantic
import typing
import typing_extensions


class V1LipSyncGenerateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for lip-sync. For video, The `video_source` field determines whether `video_file_path` or `youtube_url` field is used
    """

    audio_file_path: typing_extensions.Required[str]
    """
    The path of the audio file. This value is either
    - a direct URL to the video file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """

    video_file_path: typing_extensions.NotRequired[str]
    """
    Required if `video_source` is `file`. This value is either
    - a direct URL to the video file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """

    video_source: typing_extensions.Required[
        typing_extensions.Literal["file", "youtube"]
    ]

    youtube_url: typing_extensions.NotRequired[str]
    """
    Using a youtube video as the input source. This field is required if `video_source` is `youtube`
    """
