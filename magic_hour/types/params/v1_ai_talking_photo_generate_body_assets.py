import pydantic
import typing_extensions


class V1AiTalkingPhotoGenerateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for creating a talking photo
    """

    audio_file_path: typing_extensions.Required[str]
    """
    The audio file to sync with the image. This value is either
    - a direct URL to the video file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """

    image_file_path: typing_extensions.Required[str]
    """
    The source image to animate. This value is either
    - a direct URL to the video file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """
