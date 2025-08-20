import pydantic
import typing
import typing_extensions


class V1ImageBackgroundRemoverGenerateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for background removal
    """

    background_image_file_path: typing_extensions.NotRequired[str]
    """
    The image used as the new background for the image_file_path. This image will be resized to match the image in image_file_path. Please make sure the resolution between the images are similar. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """

    image_file_path: typing_extensions.Required[str]
    """
    The image to remove the background. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """
