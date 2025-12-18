import pydantic
import typing
import typing_extensions


class V1FaceSwapCreateBodyStyle(typing_extensions.TypedDict):
    """
    Style of the face swap video.
    """

    version: typing_extensions.NotRequired[
        typing_extensions.Literal["default", "v1", "v2"]
    ]
    """
    * `v1` - May preserve skin detail and texture better, but weaker identity preservation.
    * `v2` - Faster, sharper, better handling of hair and glasses. stronger identity preservation.
    * `default` - Use the version we recommend, which will change over time. This is recommended unless you need a specific earlier version. This is the default behavior.
    """


class _SerializerV1FaceSwapCreateBodyStyle(pydantic.BaseModel):
    """
    Serializer for V1FaceSwapCreateBodyStyle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    version: typing.Optional[typing_extensions.Literal["default", "v1", "v2"]] = (
        pydantic.Field(alias="version", default=None)
    )
