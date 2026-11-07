import pydantic
import typing

from .v1_voices_list_response_voices_item import V1VoicesListResponseVoicesItem


class V1VoicesListResponse(pydantic.BaseModel):
    """
    V1VoicesListResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    next_cursor: typing.Optional[str] = pydantic.Field(
        alias="next_cursor",
    )
    """
    Cursor for the next page, or null when there are no more voices.
    """
    voices: typing.List[V1VoicesListResponseVoicesItem] = pydantic.Field(
        alias="voices",
    )
