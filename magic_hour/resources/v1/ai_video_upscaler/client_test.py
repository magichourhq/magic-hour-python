from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock, patch

import pytest
from make_api_request import RequestOptions
from typing_extensions import TypedDict

from magic_hour.types import params

from magic_hour.resources.v1.ai_video_upscaler.client import (
    AiVideoUpscalerClient,
    AsyncAiVideoUpscalerClient,
)


class GenerateOptions(TypedDict, total=False):
    wait_for_completion: bool
    download_outputs: bool
    download_directory: str


@pytest.mark.parametrize("custom_options", [False, True])
def test_generate_uploads_video_and_returns_video_result(custom_options: bool) -> None:
    base_client = Mock()
    base_client.request.return_value = SimpleNamespace(id="upscale-123")
    client = AiVideoUpscalerClient(base_client=base_client)
    assets: params.V1AiVideoUpscalerGenerateBodyAssets = {
        "video_file_path": "local/video.mp4"
    }
    result = object()
    options: GenerateOptions = (
        dict(
            wait_for_completion=False,
            download_outputs=False,
            download_directory="outputs",
        )
        if custom_options
        else {}
    )
    request_options: RequestOptions = {"timeout": 30}

    with (
        patch(
            "magic_hour.resources.v1.ai_video_upscaler.client.FilesClient.upload_file",
            return_value="api-assets/video.mp4",
        ) as upload,
        patch(
            "magic_hour.resources.v1.ai_video_upscaler.client.VideoProjectsClient.check_result",
            return_value=result,
        ) as check_result,
    ):
        response = client.generate(
            assets=assets,
            end_seconds=4,
            resolution="1080p",
            name="Upscale",
            start_seconds=1,
            request_options=request_options,
            **options,
        )

    assert response is result
    upload.assert_called_once_with(file="local/video.mp4")
    assert assets == {"video_file_path": "local/video.mp4"}
    sent = base_client.request.call_args.kwargs
    assert sent["path"] == "/v1/ai-video-upscaler"
    assert sent["json"] == {
        "assets": {"video_file_path": "api-assets/video.mp4"},
        "end_seconds": 4,
        "resolution": "1080p",
        "name": "Upscale",
        "start_seconds": 1,
    }
    assert sent["request_options"] is request_options
    check_result.assert_called_once_with(
        id="upscale-123",
        wait_for_completion=not custom_options,
        download_outputs=not custom_options,
        download_directory="outputs" if custom_options else None,
    )


@pytest.mark.asyncio
@pytest.mark.parametrize("custom_options", [False, True])
async def test_async_generate_uploads_video_and_returns_video_result(
    custom_options: bool,
) -> None:
    base_client = AsyncMock()
    base_client.request.return_value = SimpleNamespace(id="upscale-123")
    client = AsyncAiVideoUpscalerClient(base_client=base_client)
    assets: params.V1AiVideoUpscalerGenerateBodyAssets = {
        "video_file_path": "local/video.mp4"
    }
    result = object()
    options: GenerateOptions = (
        dict(
            wait_for_completion=False,
            download_outputs=False,
            download_directory="outputs",
        )
        if custom_options
        else {}
    )
    request_options: RequestOptions = {"timeout": 30}

    with (
        patch(
            "magic_hour.resources.v1.ai_video_upscaler.client.AsyncFilesClient.upload_file",
            new_callable=AsyncMock,
            return_value="api-assets/video.mp4",
        ) as upload,
        patch(
            "magic_hour.resources.v1.ai_video_upscaler.client.AsyncVideoProjectsClient.check_result",
            new_callable=AsyncMock,
            return_value=result,
        ) as check_result,
    ):
        response = await client.generate(
            assets=assets,
            end_seconds=4,
            resolution="1080p",
            name="Upscale",
            start_seconds=1,
            request_options=request_options,
            **options,
        )

    assert response is result
    upload.assert_awaited_once_with(file="local/video.mp4")
    assert assets == {"video_file_path": "local/video.mp4"}
    sent = base_client.request.call_args.kwargs
    assert sent["path"] == "/v1/ai-video-upscaler"
    assert sent["json"] == {
        "assets": {"video_file_path": "api-assets/video.mp4"},
        "end_seconds": 4,
        "resolution": "1080p",
        "name": "Upscale",
        "start_seconds": 1,
    }
    assert sent["request_options"] is request_options
    check_result.assert_awaited_once_with(
        id="upscale-123",
        wait_for_completion=not custom_options,
        download_outputs=not custom_options,
        download_directory="outputs" if custom_options else None,
    )
