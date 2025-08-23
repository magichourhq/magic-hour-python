import pydantic
import pytest

from magic_hour import AsyncClient, Client
from magic_hour.environment import Environment
from magic_hour.types import models


def test_create_200_success_all_params() -> None:
    """Tests a POST request to the /v1/face-swap endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.V1FaceSwapCreateResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.v1.face_swap.create(
        assets={
            "face_mappings": [
                {
                    "new_face": "api-assets/id/1234.png",
                    "original_face": "api-assets/id/0-0.png",
                }
            ],
            "face_swap_mode": "all-faces",
            "image_file_path": "image/id/1234.png",
            "video_file_path": "api-assets/id/1234.mp4",
            "video_source": "file",
            "youtube_url": "http://www.example.com",
        },
        end_seconds=15.0,
        start_seconds=0.0,
        height=123,
        name="Face Swap video",
        style={"version": "default"},
        width=123,
    )
    try:
        pydantic.TypeAdapter(models.V1FaceSwapCreateResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a POST request to the /v1/face-swap endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.V1FaceSwapCreateResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.v1.face_swap.create(
        assets={
            "face_mappings": [
                {
                    "new_face": "api-assets/id/1234.png",
                    "original_face": "api-assets/id/0-0.png",
                }
            ],
            "face_swap_mode": "all-faces",
            "image_file_path": "image/id/1234.png",
            "video_file_path": "api-assets/id/1234.mp4",
            "video_source": "file",
            "youtube_url": "http://www.example.com",
        },
        end_seconds=15.0,
        start_seconds=0.0,
        height=123,
        name="Face Swap video",
        style={"version": "default"},
        width=123,
    )
    try:
        pydantic.TypeAdapter(models.V1FaceSwapCreateResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
