import pydantic
import typing
import typing_extensions


class V1AiImageEditorCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1AiImageEditorCreateBodyStyle
    """

    model: typing_extensions.NotRequired[
        typing_extensions.Literal["Nano Banana", "Seedream", "default"]
    ]
    """
    The AI model to use for image editing. * `Nano Banana` - Precise, realistic edits with consistent results
    * `Seedream` - Creative, imaginative images with artistic freedom
    * `default` - Use the model we recommend, which will change over time. This is recommended unless you need a specific model. This is the default behavior.
    """

    prompt: typing_extensions.Required[str]
    """
    The prompt used to edit the image.
    """


class _SerializerV1AiImageEditorCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiImageEditorCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    model: typing.Optional[
        typing_extensions.Literal["Nano Banana", "Seedream", "default"]
    ] = pydantic.Field(alias="model", default=None)
    prompt: str = pydantic.Field(
        alias="prompt",
    )
