import pydantic
import typing
import typing_extensions


class V1AiHeadshotGeneratorCreateBodyStyle(typing_extensions.TypedDict):
    """
    V1AiHeadshotGeneratorCreateBodyStyle
    """

    prompt: typing_extensions.NotRequired[str]
    """
    Prompt used to guide the style of your headshot. We recommend omitting the prompt unless you want to customize your headshot. You can visit [AI headshot generator](https://magichour.ai/create/ai-headshot-generator) to view an example of a good prompt used for our 'Professional' style.
    """


class _SerializerV1AiHeadshotGeneratorCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiHeadshotGeneratorCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prompt: typing.Optional[str] = pydantic.Field(alias="prompt", default=None)
