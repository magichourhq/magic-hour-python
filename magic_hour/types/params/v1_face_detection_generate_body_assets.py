import pydantic
import typing_extensions


class V1FaceDetectionGenerateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for face detection
    """

    target_file_path: typing_extensions.Required[str]
    """
    This is the image or video where the face will be detected. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """
