import typing_extensions


class V1AiVideoTranslatorGenerateBodyAssets(typing_extensions.TypedDict):
    """Source video for the translation job."""

    video_file_path: typing_extensions.Required[str]
    """Local file path, direct URL, or previously uploaded ``api-assets`` path."""
