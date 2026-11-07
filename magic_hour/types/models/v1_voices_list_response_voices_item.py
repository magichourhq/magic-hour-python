import pydantic
import typing


class V1VoicesListResponseVoicesItem(pydantic.BaseModel):
    """
    V1VoicesListResponseVoicesItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    avatar_url: typing.Optional[str] = pydantic.Field(
        alias="avatar_url",
    )
    """
    URL of the voice's avatar image, or null when the voice has no avatar.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique ID of the voice. Pass it as `style.voice_name` when generating speech. Names are not unique, so use the ID.
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    Display name of the voice.
    """
    preview_url: str = pydantic.Field(
        alias="preview_url",
    )
    """
    URL of an audio sample of the voice.
    """
