import pydantic
import typing
import typing_extensions

from .v1_audio_projects_get_response_downloads_item import (
    V1AudioProjectsGetResponseDownloadsItem,
)
from .v1_audio_projects_get_response_error import V1AudioProjectsGetResponseError


class V1AudioProjectsGetResponse(pydantic.BaseModel):
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
    The amount of credits deducted from your account to generate the audio. We charge credits right when the request is made. 
    
    If an error occurred while generating the audio, credits will be refunded and this field will be updated to include the refund.
    """
    downloads: typing.List[V1AudioProjectsGetResponseDownloadsItem] = pydantic.Field(
        alias="downloads",
    )
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Indicates whether the resource is deleted
    """
    error: typing.Optional[V1AudioProjectsGetResponseError] = pydantic.Field(
        alias="error",
    )
    """
    In the case of an error, this object will contain the error encountered during video render
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique ID of the audio. This value can be used in the [get audio project API](https://docs.magichour.ai/api-reference/audio-projects/get-audio-details) to fetch additional details such as status
    """
    name: typing.Optional[str] = pydantic.Field(
        alias="name",
    )
    """
    The name of the audio.
    """
    status: typing_extensions.Literal[
        "canceled", "complete", "draft", "error", "queued", "rendering"
    ] = pydantic.Field(
        alias="status",
    )
    """
    The status of the audio.
    """
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    The type of the audio project. Possible values are VOICE_GENERATOR, VOICE_CHANGER, VOICE_CLONER
    """
