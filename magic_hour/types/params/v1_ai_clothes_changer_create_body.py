import pydantic
import typing
import typing_extensions

from .v1_ai_clothes_changer_create_body_assets import (
    V1AiClothesChangerCreateBodyAssets,
    _SerializerV1AiClothesChangerCreateBodyAssets,
)


class V1AiClothesChangerCreateBody(typing_extensions.TypedDict):
    """
    V1AiClothesChangerCreateBody
    """

    assets: typing_extensions.Required[V1AiClothesChangerCreateBodyAssets]
    """
    Provide the assets for clothes changer
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image. This value is mainly used for your own identification of the image.
    """


class _SerializerV1AiClothesChangerCreateBody(pydantic.BaseModel):
    """
    Serializer for V1AiClothesChangerCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerV1AiClothesChangerCreateBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
