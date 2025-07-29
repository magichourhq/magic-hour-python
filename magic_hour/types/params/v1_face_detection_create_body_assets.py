import pydantic
import typing_extensions


class V1FaceDetectionCreateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for face detection
    """

    target_file_path: typing_extensions.Required[str]
    """
    This is the image or video where the face will be detected. This value can be either the `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls), or the url of the file.
    """


class _SerializerV1FaceDetectionCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1FaceDetectionCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    target_file_path: str = pydantic.Field(
        alias="target_file_path",
    )
