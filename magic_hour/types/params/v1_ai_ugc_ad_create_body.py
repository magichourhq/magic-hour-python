import pydantic
import typing
import typing_extensions

from .v1_ai_ugc_ad_create_body_assets import (
    V1AiUgcAdCreateBodyAssets,
    _SerializerV1AiUgcAdCreateBodyAssets,
)


class V1AiUgcAdCreateBody(typing_extensions.TypedDict, total=False):
    """
    V1AiUgcAdCreateBody
    """

    assets: typing_extensions.Required[V1AiUgcAdCreateBodyAssets]

    end_seconds: typing_extensions.Required[float]
    """
    Video duration in seconds. Supported values by model:
    * kling-3.0: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 seconds.
    * ltx-2.5: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60 seconds.
    * veo3.1: 4, 6, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99, 106, 113, 120, 127, 134, 141 seconds.
    Free plans are limited to 5 seconds unless a credit pack has been purchased.
    """

    model: typing_extensions.NotRequired[
        typing_extensions.Literal["kling-3.0", "ltx-2.5", "veo3.1"]
    ]
    """
    Defaults to kling-3.0 on paid plans and ltx-2.5 on free plans.
    """

    resolution: typing_extensions.NotRequired[
        typing_extensions.Literal["1080p", "480p", "720p"]
    ]
    """
    Defaults to 720p on paid plans and 480p on free plans. Unsupported model/resolution combinations and resolutions unavailable for your plan are rejected.
    """

    script: typing_extensions.Required[str]
    """
    The words the actor should speak. Character limits apply after trimming:
    * kling-3.0: 2500 characters.
    * ltx-2.5: 1804 characters.
    * veo3.1: 2500 characters.
    LTX's dialogue wrapper counts toward its model prompt limit.
    """


class _SerializerV1AiUgcAdCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiUgcAdCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    assets: _SerializerV1AiUgcAdCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    end_seconds: float = pydantic.Field(
        alias="end_seconds",
    )
    model: typing.Optional[
        typing_extensions.Literal["kling-3.0", "ltx-2.5", "veo3.1"]
    ] = pydantic.Field(alias="model", default=None)
    resolution: typing.Optional[typing_extensions.Literal["1080p", "480p", "720p"]] = (
        pydantic.Field(alias="resolution", default=None)
    )
    script: str = pydantic.Field(
        alias="script",
    )
