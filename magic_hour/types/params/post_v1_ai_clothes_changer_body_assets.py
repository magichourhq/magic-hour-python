import typing_extensions
import pydantic


class PostV1AiClothesChangerBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for clothes changer
    """

    garment_file_path: typing_extensions.Required[str]
    """
    The image of the outfit. This value can be the `file_path` field from the response of the [upload urls API](/docs/api/tag/files/post/v1/files/upload-urls), or the url of the file.
    """

    garment_type: typing_extensions.Required[
        typing_extensions.Literal["dresses", "lower_body", "upper_body"]
    ]

    person_file_path: typing_extensions.Required[str]
    """
    The image with the person. This value can be the `file_path` field from the response of the [upload urls API](/docs/api/tag/files/post/v1/files/upload-urls), or the url of the file.
    """


class _SerializerPostV1AiClothesChangerBodyAssets(pydantic.BaseModel):
    """
    Serializer for PostV1AiClothesChangerBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    garment_file_path: str = pydantic.Field(
        alias="garment_file_path",
    )
    garment_type: typing_extensions.Literal["dresses", "lower_body", "upper_body"] = (
        pydantic.Field(
            alias="garment_type",
        )
    )
    person_file_path: str = pydantic.Field(
        alias="person_file_path",
    )
