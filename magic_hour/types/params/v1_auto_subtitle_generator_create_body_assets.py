import pydantic
import typing_extensions


class V1AutoSubtitleGeneratorCreateBodyAssets(typing_extensions.TypedDict):
    """
    Provide the assets for auto subtitle generator
    """

    video_file_path: typing_extensions.Required[str]
    """
    This is the video used to add subtitles. This value can be either the `file_path` field from the response of the [upload urls API](https://docs.magichour.ai/api-reference/files/generate-asset-upload-urls), or the url of the file.
    """


class _SerializerV1AutoSubtitleGeneratorCreateBodyAssets(pydantic.BaseModel):
    """
    Serializer for V1AutoSubtitleGeneratorCreateBodyAssets handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    video_file_path: str = pydantic.Field(
        alias="video_file_path",
    )
