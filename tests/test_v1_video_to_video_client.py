import pydantic
import pytest

from magic_hour import AsyncClient, Client
from magic_hour.environment import Environment
from magic_hour.types import models


def test_create_200_success_all_params():
    """Tests a POST request to the /v1/video-to-video endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.V1VideoToVideoCreateResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.v1.video_to_video.create(
        assets={
            "video_file_path": "api-assets/id/1234.mp4",
            "video_source": "file",
            "youtube_url": "http://www.example.com",
        },
        end_seconds=15.0,
        start_seconds=0.0,
        style={
            "art_style": "3D Render",
            "model": "Absolute Reality",
            "prompt": "string",
            "prompt_type": "append_default",
            "version": "default",
        },
        fps_resolution="HALF",
        height=960,
        name="Video To Video video",
        width=512,
    )
    try:
        pydantic.TypeAdapter(models.V1VideoToVideoCreateResponse).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params():
    """Tests a POST request to the /v1/video-to-video endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.V1VideoToVideoCreateResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.v1.video_to_video.create(
        assets={
            "video_file_path": "api-assets/id/1234.mp4",
            "video_source": "file",
            "youtube_url": "http://www.example.com",
        },
        end_seconds=15.0,
        start_seconds=0.0,
        style={
            "art_style": "3D Render",
            "model": "Absolute Reality",
            "prompt": "string",
            "prompt_type": "append_default",
            "version": "default",
        },
        fps_resolution="HALF",
        height=960,
        name="Video To Video video",
        width=512,
    )
    try:
        pydantic.TypeAdapter(models.V1VideoToVideoCreateResponse).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
