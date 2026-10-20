from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock, patch

import pytest
from make_api_request import RequestOptions
from typing_extensions import TypedDict

from magic_hour.types import params

from magic_hour.resources.v1.ai_ugc_ad.client import (
    AiUgcAdClient,
    AsyncAiUgcAdClient,
)


class GenerateOptions(TypedDict, total=False):
    wait_for_completion: bool
    download_outputs: bool
    download_directory: str


@pytest.mark.parametrize("custom_options", [False, True])
def test_generate_uploads_image_and_returns_video_result(custom_options: bool) -> None:
    base_client = Mock()
    base_client.request.return_value = SimpleNamespace(id="ugc-123")
    client = AiUgcAdClient(base_client=base_client)
    assets: params.V1AiUgcAdGenerateBodyAssets = {"image_file_path": "local/image.jpg"}
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
            "magic_hour.resources.v1.ai_ugc_ad.client.FilesClient.upload_file",
            return_value="api-assets/image.jpg",
        ) as upload,
        patch(
            "magic_hour.resources.v1.ai_ugc_ad.client.VideoProjectsClient.check_result",
            return_value=result,
        ) as check_result,
    ):
        response = client.generate(
            assets=assets,
            end_seconds=4,
            script="Try our product.",
            model="veo3.1",
            resolution="1080p",
            additional_properties={"extra_option": True},
            request_options=request_options,
            **options,
        )

    assert response is result
    upload.assert_called_once_with(file="local/image.jpg")
    assert assets == {"image_file_path": "local/image.jpg"}
    sent = base_client.request.call_args.kwargs
    assert sent["path"] == "/v1/ai-ugc-ad"
    assert sent["json"] == {
        "assets": {"image_file_path": "api-assets/image.jpg"},
        "end_seconds": 4,
        "script": "Try our product.",
        "model": "veo3.1",
        "resolution": "1080p",
        "extra_option": True,
    }
    assert sent["request_options"] is request_options
    check_result.assert_called_once_with(
        id="ugc-123",
        wait_for_completion=not custom_options,
        download_outputs=not custom_options,
        download_directory="outputs" if custom_options else None,
    )


@pytest.mark.asyncio
@pytest.mark.parametrize("custom_options", [False, True])
async def test_async_generate_uploads_image_and_returns_video_result(
    custom_options: bool,
) -> None:
    base_client = AsyncMock()
    base_client.request.return_value = SimpleNamespace(id="ugc-123")
    client = AsyncAiUgcAdClient(base_client=base_client)
    assets: params.V1AiUgcAdGenerateBodyAssets = {"image_file_path": "local/image.jpg"}
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
            "magic_hour.resources.v1.ai_ugc_ad.client.AsyncFilesClient.upload_file",
            new_callable=AsyncMock,
            return_value="api-assets/image.jpg",
        ) as upload,
        patch(
            "magic_hour.resources.v1.ai_ugc_ad.client.AsyncVideoProjectsClient.check_result",
            new_callable=AsyncMock,
            return_value=result,
        ) as check_result,
    ):
        response = await client.generate(
            assets=assets,
            end_seconds=4,
            script="Try our product.",
            model="veo3.1",
            resolution="1080p",
            additional_properties={"extra_option": True},
            request_options=request_options,
            **options,
        )

    assert response is result
    upload.assert_awaited_once_with(file="local/image.jpg")
    assert assets == {"image_file_path": "local/image.jpg"}
    sent = base_client.request.call_args.kwargs
    assert sent["path"] == "/v1/ai-ugc-ad"
    assert sent["json"] == {
        "assets": {"image_file_path": "api-assets/image.jpg"},
        "end_seconds": 4,
        "script": "Try our product.",
        "model": "veo3.1",
        "resolution": "1080p",
        "extra_option": True,
    }
    assert sent["request_options"] is request_options
    check_result.assert_awaited_once_with(
        id="ugc-123",
        wait_for_completion=not custom_options,
        download_outputs=not custom_options,
        download_directory="outputs" if custom_options else None,
    )
