import pydantic
import typing_extensions


class V1ImageToVideoGenerateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for image-to-video.
    """

    end_image_file_path: typing_extensions.NotRequired[str]
    """
    The path of the image to use as the last frame of the video. This value is either
    - a direct URL to the image file
    - a path to a local file

    * **`ltx-2`**: Not supported
    * **`seedance`**: Supports 480p, 720p, 1080p.
    * **`kling-2.5`**: Supports 1080p.
    * **`kling-3.0`**: Supports 1080p.
    * **`sora-2`**: Not supported
    * **`veo3.1`**: Not supported
    
    Legacy models:
    * **`kling-1.6`**: Not supported
    """

    image_file_path: typing_extensions.Required[str]
    """
    The path of the image file. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """
