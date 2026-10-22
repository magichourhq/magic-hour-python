from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock, patch

import pytest
from make_api_request import RequestOptions
from typing_extensions import TypedDict

from magic_hour.resources.v1.ai_music_generator.client import (
    AiMusicGeneratorClient,
    AsyncAiMusicGeneratorClient,
)


class GenerateOptions(TypedDict, total=False):
    wait_for_completion: bool
    download_outputs: bool
    download_directory: str


@pytest.mark.parametrize("custom_options", [False, True])
def test_generate_returns_audio_result(custom_options: bool) -> None:
    base_client = Mock()
    base_client.request.return_value = SimpleNamespace(id="music-123")
    client = AiMusicGeneratorClient(base_client=base_client)
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
            "magic_hour.resources.v1.ai_music_generator.client.AudioProjectsClient.check_result",
            return_value=result,
        ) as check_result,
    ):
        response = client.generate(
            duration=120,
            style={"prompt": "Synthwave", "instrumental": True, "lyrics": "Ignored"},
            name="Music",
            additional_properties={"extra_option": True},
            request_options=request_options,
            **options,
        )

    assert response is result
    sent = base_client.request.call_args.kwargs
    assert sent["path"] == "/v1/ai-music-generator"
    assert sent["json"] == {
        "duration": 120,
        "style": {"prompt": "Synthwave", "instrumental": True, "lyrics": "Ignored"},
        "name": "Music",
        "extra_option": True,
    }
    assert sent["request_options"] is request_options
    check_result.assert_called_once_with(
        id="music-123",
        wait_for_completion=not custom_options,
        download_outputs=not custom_options,
        download_directory="outputs" if custom_options else None,
    )


@pytest.mark.asyncio
@pytest.mark.parametrize("custom_options", [False, True])
async def test_async_generate_returns_audio_result(
    custom_options: bool,
) -> None:
    base_client = AsyncMock()
    base_client.request.return_value = SimpleNamespace(id="music-123")
    client = AsyncAiMusicGeneratorClient(base_client=base_client)
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
            "magic_hour.resources.v1.ai_music_generator.client.AsyncAudioProjectsClient.check_result",
            new_callable=AsyncMock,
            return_value=result,
        ) as check_result,
    ):
        response = await client.generate(
            duration=120,
            style={"prompt": "Synthwave", "instrumental": True, "lyrics": "Ignored"},
            name="Music",
            additional_properties={"extra_option": True},
            request_options=request_options,
            **options,
        )

    assert response is result
    sent = base_client.request.call_args.kwargs
    assert sent["path"] == "/v1/ai-music-generator"
    assert sent["json"] == {
        "duration": 120,
        "style": {"prompt": "Synthwave", "instrumental": True, "lyrics": "Ignored"},
        "name": "Music",
        "extra_option": True,
    }
    assert sent["request_options"] is request_options
    check_result.assert_awaited_once_with(
        id="music-123",
        wait_for_completion=not custom_options,
        download_outputs=not custom_options,
        download_directory="outputs" if custom_options else None,
    )
