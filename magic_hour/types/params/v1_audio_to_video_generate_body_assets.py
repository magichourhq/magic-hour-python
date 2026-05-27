import typing_extensions


class V1AudioToVideoGenerateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the audio file and an optional reference image.
    """

    audio_file_path: typing_extensions.Required[str]
    """
    The path of the audio file. This value is either
    - a direct URL to the audio file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """

    image_file_path: typing_extensions.NotRequired[str]
    """
    Reference image for the initial frame of the video. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """
