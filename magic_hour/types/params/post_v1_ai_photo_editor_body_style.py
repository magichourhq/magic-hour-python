import pydantic
import typing
import typing_extensions


class PostV1AiPhotoEditorBodyStyle(typing_extensions.TypedDict):
    """
    PostV1AiPhotoEditorBodyStyle
    """

    image_description: typing_extensions.Required[str]
    """
    Use this to describe what your input image is. This helps maintain aspects of the image you don't want to change.
    """

    likeness_strength: typing_extensions.Required[float]
    """
    Determines the input image's influence. Higher values align the output more with the initial image.
    """

    negative_prompt: typing_extensions.NotRequired[str]
    """
    What you want to avoid seeing in the final output; has a minor effect.
    """

    prompt: typing_extensions.Required[str]
    """
    What you want your final output to look like. We recommend starting with the image description and making minor edits for best results.
    """

    prompt_strength: typing_extensions.Required[float]
    """
    Determines the prompt's influence. Higher values align the output more with the prompt.
    """

    steps: typing_extensions.NotRequired[int]
    """
    Number of iterations used to generate the output. Higher values improve quality and increase the strength of the prompt but increase processing time.
    """


class _SerializerPostV1AiPhotoEditorBodyStyle(pydantic.BaseModel):
    """
    Serializer for PostV1AiPhotoEditorBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    image_description: str = pydantic.Field(
        alias="image_description",
    )
    likeness_strength: float = pydantic.Field(
        alias="likeness_strength",
    )
    negative_prompt: typing.Optional[str] = pydantic.Field(
        alias="negative_prompt", default=None
    )
    prompt: str = pydantic.Field(
        alias="prompt",
    )
    prompt_strength: float = pydantic.Field(
        alias="prompt_strength",
    )
    steps: typing.Optional[int] = pydantic.Field(alias="steps", default=None)
