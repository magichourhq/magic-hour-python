import pydantic
import typing
import typing_extensions


class V1AiFaceEditorCreateBodyStyle(typing_extensions.TypedDict):
    """
    Face editing parameters
    """

    enhance_face: typing_extensions.NotRequired[bool]
    """
    Enhance face features
    """

    eye_gaze_horizontal: typing_extensions.NotRequired[float]
    """
    Horizontal eye gaze (-100 to 100), in increments of 5
    """

    eye_gaze_vertical: typing_extensions.NotRequired[float]
    """
    Vertical eye gaze (-100 to 100), in increments of 5
    """

    eye_open_ratio: typing_extensions.NotRequired[float]
    """
    Eye open ratio (-100 to 100), in increments of 5
    """

    eyebrow_direction: typing_extensions.NotRequired[float]
    """
    Eyebrow direction (-100 to 100), in increments of 5
    """

    head_pitch: typing_extensions.NotRequired[float]
    """
    Head pitch (-100 to 100), in increments of 5
    """

    head_roll: typing_extensions.NotRequired[float]
    """
    Head roll (-100 to 100), in increments of 5
    """

    head_yaw: typing_extensions.NotRequired[float]
    """
    Head yaw (-100 to 100), in increments of 5
    """

    lip_open_ratio: typing_extensions.NotRequired[float]
    """
    Lip open ratio (-100 to 100), in increments of 5
    """

    mouth_grim: typing_extensions.NotRequired[float]
    """
    Mouth grim (-100 to 100), in increments of 5
    """

    mouth_position_horizontal: typing_extensions.NotRequired[float]
    """
    Horizontal mouth position (-100 to 100), in increments of 5
    """

    mouth_position_vertical: typing_extensions.NotRequired[float]
    """
    Vertical mouth position (-100 to 100), in increments of 5
    """

    mouth_pout: typing_extensions.NotRequired[float]
    """
    Mouth pout (-100 to 100), in increments of 5
    """

    mouth_purse: typing_extensions.NotRequired[float]
    """
    Mouth purse (-100 to 100), in increments of 5
    """

    mouth_smile: typing_extensions.NotRequired[float]
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

    enhance_face: typing.Optional[bool] = pydantic.Field(
        alias="enhance_face", default=None
    )
    eye_gaze_horizontal: typing.Optional[float] = pydantic.Field(
        alias="eye_gaze_horizontal", default=None
    )
    eye_gaze_vertical: typing.Optional[float] = pydantic.Field(
        alias="eye_gaze_vertical", default=None
    )
    eye_open_ratio: typing.Optional[float] = pydantic.Field(
        alias="eye_open_ratio", default=None
    )
    eyebrow_direction: typing.Optional[float] = pydantic.Field(
        alias="eyebrow_direction", default=None
    )
    head_pitch: typing.Optional[float] = pydantic.Field(
        alias="head_pitch", default=None
    )
    head_roll: typing.Optional[float] = pydantic.Field(alias="head_roll", default=None)
    head_yaw: typing.Optional[float] = pydantic.Field(alias="head_yaw", default=None)
    lip_open_ratio: typing.Optional[float] = pydantic.Field(
        alias="lip_open_ratio", default=None
    )
    mouth_grim: typing.Optional[float] = pydantic.Field(
        alias="mouth_grim", default=None
    )
    mouth_position_horizontal: typing.Optional[float] = pydantic.Field(
        alias="mouth_position_horizontal", default=None
    )
    mouth_position_vertical: typing.Optional[float] = pydantic.Field(
        alias="mouth_position_vertical", default=None
    )
    mouth_pout: typing.Optional[float] = pydantic.Field(
        alias="mouth_pout", default=None
    )
    mouth_purse: typing.Optional[float] = pydantic.Field(
        alias="mouth_purse", default=None
    )
    mouth_smile: typing.Optional[float] = pydantic.Field(
        alias="mouth_smile", default=None
    )
