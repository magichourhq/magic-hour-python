import pydantic
import typing_extensions


class V1CharacterReplaceCreateBodyAssets(typing_extensions.TypedDict):
    """
    Source video and reference character image for the job.
    """

    image_file_path: typing_extensions.Required[str]
    """
    Reference character image used as the replacement or animation target. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.
    
    """

    video_file_path: typing_extensions.Required[str]
    """
    Source video containing the subject to replace or animate. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.
    
    """


class _SerializerV1CharacterReplaceCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1CharacterReplaceCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    image_file_path: str = pydantic.Field(
        alias="image_file_path",
    )
    video_file_path: str = pydantic.Field(
        alias="video_file_path",
    )
