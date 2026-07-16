import typing_extensions


class V1CharacterReplaceGenerateBodyAssets(typing_extensions.TypedDict):
    """
    Source video and reference character image for the job.
    """

    image_file_path: typing_extensions.Required[str]
    """
    Reference character image used as the replacement or animation target. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """

    video_file_path: typing_extensions.Required[str]
    """
    Source video containing the subject to replace or animate. This value is either
    - a direct URL to the video file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """
