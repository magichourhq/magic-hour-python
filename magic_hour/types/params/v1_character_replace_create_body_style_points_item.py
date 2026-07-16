import pydantic
import typing_extensions


class V1CharacterReplaceCreateBodyStylePointsItem(typing_extensions.TypedDict):
    """
    V1CharacterReplaceCreateBodyStylePointsItem
    """

    position_x: typing_extensions.Required[int]
    """
    Horizontal pixel coordinate in the source video frame at `time_seconds`, measured from the left edge.
    """

    position_y: typing_extensions.Required[int]
    """
    Vertical pixel coordinate in the source video frame at `time_seconds`, measured from the top edge.
    """

    time_seconds: typing_extensions.Required[float]
    """
    Timestamp on the source video timeline in seconds. Uses the same clock as `start_seconds` and `end_seconds`.
    """


class _SerializerV1CharacterReplaceCreateBodyStylePointsItem(pydantic.BaseModel):
    """
    Serializer for V1CharacterReplaceCreateBodyStylePointsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    position_x: int = pydantic.Field(
        alias="position_x",
    )
    position_y: int = pydantic.Field(
        alias="position_y",
    )
    time_seconds: float = pydantic.Field(
        alias="time_seconds",
    )
