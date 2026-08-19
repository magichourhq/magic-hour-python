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
    Whether this resource is active. If false, it is deleted.
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
    Unique ID of the audio. Use it with the [Get audio Project API](https://docs.magichour.ai/api-reference/audio-projects/get-audio-details) to fetch status and downloads.
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
    
    - `draft` - the project was created but has not been submitted for rendering
    - `queued` - the job is waiting for an available server
    - `rendering` - the job is being processed; the `audio.started` webhook event fires when rendering begins
    - `complete` - the job finished successfully; fires `audio.completed`
    - `error` - the job failed during processing; fires `audio.errored`
    - `canceled` - the job was manually canceled (for example from the Magic Hour web app)
    
    **Note:** `rendering`, `complete`, and `error` have matching webhook events; `canceled` does not - a canceled job emits no webhook event, so poll this endpoint to detect cancellation.
    """
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    The type of the audio project. Possible values are VOICE_GENERATOR, VOICE_CHANGER, VOICE_CLONER, VIDEO_TO_AUDIO, MUSIC_GENERATOR
    """
