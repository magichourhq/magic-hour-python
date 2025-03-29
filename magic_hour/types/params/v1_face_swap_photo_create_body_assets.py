import pydantic
import typing_extensions


class V1FaceSwapPhotoCreateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for face swap photo
    """

    source_file_path: typing_extensions.Required[str]
    """
    This is the image from which the face is extracted. This value can be either the `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls), or the url of the file.
    """

    target_file_path: typing_extensions.Required[str]
    """
    This is the image where the face from the source image will be placed. This value can be either the `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls), or the url of the file.
    """


class _SerializerV1FaceSwapPhotoCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1FaceSwapPhotoCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    source_file_path: str = pydantic.Field(
        alias="source_file_path",
    )
    target_file_path: str = pydantic.Field(
        alias="target_file_path",
    )
