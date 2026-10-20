import pydantic
import typing
import typing_extensions


class V1AiUgcAdCreateBodyAssets(typing_extensions.TypedDict, total=False):
    """
    V1AiUgcAdCreateBodyAssets
    """

    image_file_path: typing_extensions.Required[str]
    """
    Prepared image to animate. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.
    
    """


class _SerializerV1AiUgcAdCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1AiUgcAdCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    image_file_path: str = pydantic.Field(
        alias="image_file_path",
    )
