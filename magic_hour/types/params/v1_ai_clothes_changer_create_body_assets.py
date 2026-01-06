import pydantic
import typing
import typing_extensions


class V1AiClothesChangerCreateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for clothes changer
    """

    garment_file_path: typing_extensions.Required[str]
    """
    The image of the outfit. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.
    
    """

    garment_type: typing_extensions.NotRequired[
        typing_extensions.Literal["dresses", "lower_body", "upper_body"]
    ]
    """
    Deprecated: garment_type is no longer needed.
    """

    person_file_path: typing_extensions.Required[str]
    """
    The image with the person. This value is either
    - a direct URL to the video file
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.
    
    """


class _SerializerV1AiClothesChangerCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1AiClothesChangerCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    garment_file_path: str = pydantic.Field(
        alias="garment_file_path",
    )
    garment_type: typing.Optional[
        typing_extensions.Literal["dresses", "lower_body", "upper_body"]
    ] = pydantic.Field(alias="garment_type", default=None)
    person_file_path: str = pydantic.Field(
        alias="person_file_path",
    )
