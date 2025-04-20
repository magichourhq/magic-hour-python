import pydantic
import typing_extensions


class V1AiFaceEditorCreateBodyStyle(typing_extensions.TypedDict):
    """
    Face editing parameters
    """

    enhance_face: typing_extensions.Required[bool]
    """
    Enhance face features
    """

    eye_gaze_horizontal: typing_extensions.Required[float]
    """
    Horizontal eye gaze (-100 to 100), in increments of 5
    """

    eye_gaze_vertical: typing_extensions.Required[float]
    """
    Vertical eye gaze (-100 to 100), in increments of 5
    """

    eye_open_ratio: typing_extensions.Required[float]
    """
    Eye open ratio (-100 to 100), in increments of 5
    """

    eyebrow_direction: typing_extensions.Required[float]
    """
    Eyebrow direction (-100 to 100), in increments of 5
    """

    head_pitch: typing_extensions.Required[float]
    """
    Head pitch (-100 to 100), in increments of 5
    """

    head_roll: typing_extensions.Required[float]
    """
    Head roll (-100 to 100), in increments of 5
    """

    head_yaw: typing_extensions.Required[float]
    """
    Head yaw (-100 to 100), in increments of 5
    """

    lip_open_ratio: typing_extensions.Required[float]
    """
    Lip open ratio (-100 to 100), in increments of 5
    """

    mouth_grim: typing_extensions.Required[float]
    """
    Mouth grim (-100 to 100), in increments of 5
    """

    mouth_position_horizontal: typing_extensions.Required[float]
    """
    Horizontal mouth position (-100 to 100), in increments of 5
    """

    mouth_position_vertical: typing_extensions.Required[float]
    """
    Vertical mouth position (-100 to 100), in increments of 5
    """

    mouth_pout: typing_extensions.Required[float]
    """
    Mouth pout (-100 to 100), in increments of 5
    """

    mouth_purse: typing_extensions.Required[float]
    """
    Mouth purse (-100 to 100), in increments of 5
    """

    mouth_smile: typing_extensions.Required[float]
    """
    Mouth smile (-100 to 100), in increments of 5
    """


class _SerializerV1AiFaceEditorCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1AiFaceEditorCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enhance_face: bool = pydantic.Field(
        alias="enhance_face",
    )
    eye_gaze_horizontal: float = pydantic.Field(
        alias="eye_gaze_horizontal",
    )
    eye_gaze_vertical: float = pydantic.Field(
        alias="eye_gaze_vertical",
    )
    eye_open_ratio: float = pydantic.Field(
        alias="eye_open_ratio",
    )
    eyebrow_direction: float = pydantic.Field(
        alias="eyebrow_direction",
    )
    head_pitch: float = pydantic.Field(
        alias="head_pitch",
    )
    head_roll: float = pydantic.Field(
        alias="head_roll",
    )
    head_yaw: float = pydantic.Field(
        alias="head_yaw",
    )
    lip_open_ratio: float = pydantic.Field(
        alias="lip_open_ratio",
    )
    mouth_grim: float = pydantic.Field(
        alias="mouth_grim",
    )
    mouth_position_horizontal: float = pydantic.Field(
        alias="mouth_position_horizontal",
    )
    mouth_position_vertical: float = pydantic.Field(
        alias="mouth_position_vertical",
    )
    mouth_pout: float = pydantic.Field(
        alias="mouth_pout",
    )
    mouth_purse: float = pydantic.Field(
        alias="mouth_purse",
    )
    mouth_smile: float = pydantic.Field(
        alias="mouth_smile",
    )
