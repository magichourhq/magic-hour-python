import pytest
import pydantic

from magic_hour import AsyncClient, Client
from magic_hour.environment import Environment
from magic_hour.types import models


def test_create_200_success_default():
    """Tests a POST request to the /v1/ai-image-upscaler endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PostV1AiImageUpscalerResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.v1.ai_image_upscaler.create(
        assets={"image_file_path": "image/id/1234.png"},
        scale_factor=123.45,
        style={"enhancement": "Balanced"},
        name="Image Upscaler image",
    )
    try:
        pydantic.TypeAdapter(models.PostV1AiImageUpscalerResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_default():
    """Tests a POST request to the /v1/ai-image-upscaler endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PostV1AiImageUpscalerResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.v1.ai_image_upscaler.create(
        assets={"image_file_path": "image/id/1234.png"},
        scale_factor=123.45,
        style={"enhancement": "Balanced"},
        name="Image Upscaler image",
    )
    try:
        pydantic.TypeAdapter(models.PostV1AiImageUpscalerResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
