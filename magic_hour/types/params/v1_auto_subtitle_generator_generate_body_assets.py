import pydantic
import typing_extensions


class V1AutoSubtitleGeneratorGenerateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for auto subtitle generator
    """

    video_file_path: typing_extensions.Required[str]
    """
    This is the video used to add subtitles. This value is either
    - a direct URL to the video file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """
