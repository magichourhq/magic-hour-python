import pydantic
import typing_extensions


class V1BodySwapCreateBodyAssets(typing_extensions.TypedDict):
    """
    Person image and scene image for body swap
    """

    person_file_path: typing_extensions.Required[str]
    """
    Image of the person to place into the scene. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.
    
    """

    scene_file_path: typing_extensions.Required[str]
    """
    Target scene image (background). This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.
    
    """


class _SerializerV1BodySwapCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1BodySwapCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    person_file_path: str = pydantic.Field(
        alias="person_file_path",
    )
    scene_file_path: str = pydantic.Field(
        alias="scene_file_path",
    )
