import pydantic
import typing
import typing_extensions

from .post_v1_ai_clothes_changer_body_assets import (
    PostV1AiClothesChangerBodyAssets,
    _SerializerPostV1AiClothesChangerBodyAssets,
)


class PostV1AiClothesChangerBody(typing_extensions.TypedDict):
    """
    PostV1AiClothesChangerBody
    """

    assets: typing_extensions.Required[PostV1AiClothesChangerBodyAssets]
    """
    Provide the assets for clothes changer
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of image
    """


class _SerializerPostV1AiClothesChangerBody(pydantic.BaseModel):
    """
    Serializer for PostV1AiClothesChangerBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    assets: _SerializerPostV1AiClothesChangerBodyAssets = pydantic.Field(
        alias="assets",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
