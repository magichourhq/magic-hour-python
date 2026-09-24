import pydantic
import typing_extensions


class V1TextToVideoCreateBodyReferencesItem(typing_extensions.TypedDict):
    """
    V1TextToVideoCreateBodyReferencesItem
    """

    file_path: typing_extensions.Required[str]

    name: typing_extensions.Required[str]


class _SerializerV1TextToVideoCreateBodyReferencesItem(pydantic.BaseModel):
    """
    Serializer for V1TextToVideoCreateBodyReferencesItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    file_path: str = pydantic.Field(
        alias="file_path",
    )
    name: str = pydantic.Field(
        alias="name",
    )
