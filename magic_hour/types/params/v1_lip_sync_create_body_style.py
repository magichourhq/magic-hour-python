import pydantic
import typing
import typing_extensions


class V1LipSyncCreateBodyStyle(typing_extensions.TypedDict):
    """
    Attributes used to dictate the style of the output
    """

    generation_mode: typing_extensions.NotRequired[
        typing_extensions.Literal["lite", "pro", "standard"]
    ]
    """
    A specific version of our lip sync system, optimized for different needs.
    * `lite` -  Fast lip sync - best for simple videos. Costs 1 credit per frame of video.
    * `standard` -  Natural, accurate lip sync - best for most creators. Requires visible mouth movement in the opening seconds of the input video. Costs 1 credit per frame of video.
    * `pro` -  Premium fidelity with enhanced detail - best for professionals. Requires visible mouth movement in the opening seconds of the input video. Costs 2 credits per frame of video.
    
    If your source is a still image, including a still image saved as a static video, use [AI Talking Photo](https://docs.magichour.ai/api-reference/video-projects/ai-talking-photo) with the original image and your audio instead.
    
    Note: `pro` is only available for users on Creator, Pro, and Business tiers.
                  
    """


class _SerializerV1LipSyncCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1LipSyncCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    generation_mode: typing.Optional[
        typing_extensions.Literal["lite", "pro", "standard"]
    ] = pydantic.Field(alias="generation_mode", default=None)
