import pydantic
import pytest

from magic_hour import AsyncClient, Client
from magic_hour.environment import Environment
from magic_hour.types import models


def test_create_200_success_default():
    """Tests a POST request to the /v1/ai-photo-editor endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.V1AiPhotoEditorCreateResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.v1.ai_photo_editor.create(
        assets={"image_file_path": "api-assets/id/1234.png"},
        resolution=768,
        style={
            "image_description": "A photo of a person",
            "likeness_strength": 5.2,
            "negative_prompt": "painting, cartoon, sketch",
            "prompt": "A photo portrait of a person wearing a hat",
            "prompt_strength": 3.75,
            "steps": 4,
            "upscale_factor": 2,
            "upscale_fidelity": 0.5,
        },
        name="Photo Editor image",
    )
    try:
        pydantic.TypeAdapter(models.V1AiPhotoEditorCreateResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_default():
    """Tests a POST request to the /v1/ai-photo-editor endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.V1AiPhotoEditorCreateResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.v1.ai_photo_editor.create(
        assets={"image_file_path": "api-assets/id/1234.png"},
        resolution=768,
        style={
            "image_description": "A photo of a person",
            "likeness_strength": 5.2,
            "negative_prompt": "painting, cartoon, sketch",
            "prompt": "A photo portrait of a person wearing a hat",
            "prompt_strength": 3.75,
            "steps": 4,
            "upscale_factor": 2,
            "upscale_fidelity": 0.5,
        },
        name="Photo Editor image",
    )
    try:
        pydantic.TypeAdapter(models.V1AiPhotoEditorCreateResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
