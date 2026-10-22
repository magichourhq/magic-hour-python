import typing_extensions


class V1AiVideoUpscalerGenerateBodyAssets(typing_extensions.TypedDict):
    """Source video for an upscale job."""

    video_file_path: typing_extensions.Required[str]
    """
    Video to upscale. Accepts a local video path or a direct URL.
    Paths beginning with `api-assets` are already uploaded and reused as is.
    """
