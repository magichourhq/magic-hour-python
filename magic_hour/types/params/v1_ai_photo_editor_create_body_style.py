import pydantic
import typing
import typing_extensions


class V1AiPhotoEditorCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1AiPhotoEditorCreateBodyStyle
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

    upscale_factor: typing_extensions.NotRequired[int]
    """
    The multiplier applied to an image's original dimensions during the upscaling process. For example, a scale of 2 doubles the width and height (e.g., from 512x512 to 1024x1024).
    """

    upscale_fidelity: typing_extensions.NotRequired[float]
    """
    Upscale fidelity refers to the level of quality desired in the generated image. Fidelity value of 1 means more details.
    """


class _SerializerV1AiPhotoEditorCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiPhotoEditorCreateBodyStyle handling case conversions
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
    upscale_factor: typing.Optional[int] = pydantic.Field(
        alias="upscale_factor", default=None
    )
    upscale_fidelity: typing.Optional[float] = pydantic.Field(
        alias="upscale_fidelity", default=None
    )
