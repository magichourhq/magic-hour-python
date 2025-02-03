import pytest
import pydantic

from magic_hour import AsyncClient, Client
from magic_hour.environment import Environment
from magic_hour.types import models


def test_create_200_success_default():
    """Tests a POST request to the /v1/image-to-video endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : PostV1ImageToVideoResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.v1.image_to_video.create(
        assets={"image_file_path": "image/id/1234.png"},
        end_seconds=5,
        height=960,
        style={"prompt": None},
        width=512,
        name="Image To Video video",
    )
    adapter = pydantic.TypeAdapter(models.PostV1ImageToVideoResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_create_200_success_default():
    """Tests a POST request to the /v1/image-to-video endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : PostV1ImageToVideoResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.v1.image_to_video.create(
        assets={"image_file_path": "image/id/1234.png"},
        end_seconds=5,
        height=960,
        style={"prompt": None},
        width=512,
        name="Image To Video video",
    )
    adapter = pydantic.TypeAdapter(models.PostV1ImageToVideoResponse)
    adapter.validate_python(response)
