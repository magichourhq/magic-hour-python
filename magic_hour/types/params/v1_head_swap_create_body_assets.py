import pydantic
import typing_extensions


class V1HeadSwapCreateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the body and head images for head swap
    """

    body_file_path: typing_extensions.Required[str]
    """
    Image that receives the swapped head. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.
    
    """

    head_file_path: typing_extensions.Required[str]
    """
    Image of the head to place on the body. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.
    
    """


class _SerializerV1HeadSwapCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1HeadSwapCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    body_file_path: str = pydantic.Field(
        alias="body_file_path",
    )
    head_file_path: str = pydantic.Field(
        alias="head_file_path",
    )
