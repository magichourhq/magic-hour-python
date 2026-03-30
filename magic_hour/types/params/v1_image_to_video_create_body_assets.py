import pydantic
import typing
import typing_extensions


class V1ImageToVideoCreateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for image-to-video. Sora 2 only supports images with an aspect ratio of `9:16` or `16:9`.
    """

    end_image_file_path: typing_extensions.NotRequired[str]
    """
    The image to use as the last frame of the video.
    
    * **`ltx-2`**: Not supported
    * **`wan-2.2`**: Not supported
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
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.
    
    """


class _SerializerV1ImageToVideoCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1ImageToVideoCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end_image_file_path: typing.Optional[str] = pydantic.Field(
        alias="end_image_file_path", default=None
    )
    image_file_path: str = pydantic.Field(
        alias="image_file_path",
    )
