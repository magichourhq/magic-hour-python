import pydantic
import typing_extensions


class V1ImageToVideoCreateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for image-to-video.
    """

    image_file_path: typing_extensions.Required[str]
    """
    The path of the image file. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    Please refer to the [Input File documentation](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) to learn more.
    
    """


class _SerializerV1ImageToVideoCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1ImageToVideoCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    image_file_path: str = pydantic.Field(
        alias="image_file_path",
    )
