import pydantic
import typing
import typing_extensions


class V1AnimationGenerateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for animation.
    """

    audio_file_path: typing_extensions.NotRequired[str]
    """
    The path of the input audio. This field is required if `audio_source` is `file`. This value is either
    - a direct URL to the video file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
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
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """

    youtube_url: typing_extensions.NotRequired[str]
    """
    Using a youtube video as the input source. This field is required if `audio_source` is `youtube`
    """
