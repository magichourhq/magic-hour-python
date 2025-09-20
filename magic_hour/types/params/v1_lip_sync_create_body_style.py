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
    * `lite` -  Fast and affordable lip sync - best for simple videos. Costs 1 credit per frame of video.
    * `standard` -  Natural, accurate lip sync - best for most creators. Costs 1 credit per frame of video.
    * `pro` -  Premium fidelity with enhanced detail - best for professionals. Costs 2 credits per frame of video.
    
    Note: `standard` and `pro` are only available for users on Creator, Pro, and Business tiers.
                  
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
