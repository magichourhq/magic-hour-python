import pytest
import pydantic

from magic_hour import AsyncClient, Client
from magic_hour.environment import Environment
from magic_hour.types import models


def test_create_200_success_default():
    """Tests a POST request to the /v1/animation endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : PostV1AnimationResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.v1.animation.create(
        assets={
            "audio_file_path": "api-assets/id/1234.mp3",
            "audio_source": "file",
            "image_file_path": "api-assets/id/1234.png",
        },
        end_seconds=15,
        fps=12,
        height=960,
        style={
            "art_style": "Painterly Illustration",
            "camera_effect": "Accelerate",
            "prompt": "Cyberpunk city",
            "prompt_type": "ai_choose",
            "transition_speed": 5,
        },
        width=512,
        name="Animation video",
    )
    adapter = pydantic.TypeAdapter(models.PostV1AnimationResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_create_200_success_default():
    """Tests a POST request to the /v1/animation endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : PostV1AnimationResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.v1.animation.create(
        assets={
            "audio_file_path": "api-assets/id/1234.mp3",
            "audio_source": "file",
            "image_file_path": "api-assets/id/1234.png",
        },
        end_seconds=15,
        fps=12,
        height=960,
        style={
            "art_style": "Painterly Illustration",
            "camera_effect": "Accelerate",
            "prompt": "Cyberpunk city",
            "prompt_type": "ai_choose",
            "transition_speed": 5,
        },
        width=512,
        name="Animation video",
    )
    adapter = pydantic.TypeAdapter(models.PostV1AnimationResponse)
    adapter.validate_python(response)
