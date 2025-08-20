import pydantic
import typing_extensions


class V1AiFaceEditorGenerateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for face editor
    """

    image_file_path: typing_extensions.Required[str]
    """
    This is the image whose face will be edited. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """
