import pydantic
import typing
import typing_extensions

from .v1_image_projects_get_response_downloads_item import (
    V1ImageProjectsGetResponseDownloadsItem,
)
from .v1_image_projects_get_response_error import V1ImageProjectsGetResponseError


class V1ImageProjectsGetResponse(pydantic.BaseModel):
    """
    Success
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: str = pydantic.Field(
        alias="created_at",
    )
    credits_charged: int = pydantic.Field(
        alias="credits_charged",
    )
    """
    The amount of credits deducted from your account to generate the image. We charge credits right when the request is made. 
    
    If an error occurred while generating the image(s), credits will be refunded and this field will be updated to include the refund.
    """
    downloads: typing.List[V1ImageProjectsGetResponseDownloadsItem] = pydantic.Field(
        alias="downloads",
    )
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Indicates whether the resource is deleted
    """
    error: typing.Optional[V1ImageProjectsGetResponseError] = pydantic.Field(
        alias="error",
    )
    """
    In the case of an error, this object will contain the error encountered during video render
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique ID of the image. This value can be used in the [get image project API](https://docs.magichour.ai/api-reference/image-projects/get-image-details) to fetch additional details such as status
    """
    image_count: int = pydantic.Field(
        alias="image_count",
    )
    """
    Number of images generated
    """
    name: typing.Optional[str] = pydantic.Field(
        alias="name",
    )
    """
    The name of the image.
    """
    status: typing_extensions.Literal[
        "canceled", "complete", "draft", "error", "queued", "rendering"
    ] = pydantic.Field(
        alias="status",
    )
    """
    The status of the image.
    """
    total_frame_cost: int = pydantic.Field(
        alias="total_frame_cost",
    )
    """
    Deprecated: Previously represented the number of frames (original name of our credit system) used for image generation. Use 'credits_charged' instead.
    """
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    The type of the image project. Possible values are AI_HEADSHOT, AI_IMAGE, IMAGE_UPSCALER, FACE_SWAP, PHOTO_EDITOR, QR_CODE, BACKGROUND_REMOVER, CLOTHES_CHANGER, AI_MEME, FACE_EDITOR, PHOTO_COLORIZER, AI_GIF, AI_SELFIE, AI_IMAGE_EDITOR
    """
