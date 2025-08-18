import pydantic
import typing
import typing_extensions


class V1ImageBackgroundRemoverCreateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for background removal
    """

    background_image_file_path: typing_extensions.NotRequired[str]
    """
    The image used as the new background for the image_file_path. This image will be resized to match the image in image_file_path. Please make sure the resolution between the images are similar.
    
    This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.
    
    """

    image_file_path: typing_extensions.Required[str]
    """
    The image to remove the background. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.
    
    """


class _SerializerV1ImageBackgroundRemoverCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1ImageBackgroundRemoverCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    background_image_file_path: typing.Optional[str] = pydantic.Field(
        alias="background_image_file_path", default=None
    )
    image_file_path: str = pydantic.Field(
        alias="image_file_path",
    )
