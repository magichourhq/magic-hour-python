import pydantic
import pytest

from magic_hour import AsyncClient, Client
from magic_hour.environment import Environment
from magic_hour.types import models


def test_create_200_success_all_params() -> None:
    """Tests a POST request to the /v1/ai-image-editor endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.V1AiImageEditorCreateResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.v1.ai_image_editor.create(
        assets={
            "image_file_path": "string",
            "image_file_paths": ["api-assets/id/1234.png", "api-assets/id/1235.png"],
        },
        style={"model": "Nano Banana", "prompt": "Give me sunglasses"},
        aspect_ratio="1:1",
        image_count=1.0,
        model="default",
        name="My Ai Image Editor image",
    )
    try:
        pydantic.TypeAdapter(models.V1AiImageEditorCreateResponse).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a POST request to the /v1/ai-image-editor endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.V1AiImageEditorCreateResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.v1.ai_image_editor.create(
        assets={
            "image_file_path": "string",
            "image_file_paths": ["api-assets/id/1234.png", "api-assets/id/1235.png"],
        },
        style={"model": "Nano Banana", "prompt": "Give me sunglasses"},
        aspect_ratio="1:1",
        image_count=1.0,
        model="default",
        name="My Ai Image Editor image",
    )
    try:
        pydantic.TypeAdapter(models.V1AiImageEditorCreateResponse).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
