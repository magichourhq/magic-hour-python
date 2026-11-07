import pydantic
import typing_extensions


class V1AiVideoEditorCreateBodyReferencesItem(typing_extensions.TypedDict):
    """
    V1AiVideoEditorCreateBodyReferencesItem
    """

    file_path: typing_extensions.Required[str]
    """
    This value is either
    - a direct URL to the file. The URL path must end in a supported file extension.
    - `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls).
    
    See the [file upload guide](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls#input-file) for details.
    
    """

    name: typing_extensions.Required[str]


class _SerializerV1AiVideoEditorCreateBodyReferencesItem(pydantic.BaseModel):
    """
    Serializer for V1AiVideoEditorCreateBodyReferencesItem handling case conversions
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
