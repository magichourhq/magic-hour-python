import pydantic
import pytest

from magic_hour import AsyncClient, Client
from magic_hour.environment import Environment
from magic_hour.types import models


def test_create_200_success_all_params() -> None:
    """Tests a POST request to the /v1/ai-face-editor endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.V1AiFaceEditorCreateResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.v1.ai_face_editor.create(
        assets={"image_file_path": "api-assets/id/1234.png"},
        style={
            "enhance_face": False,
            "eye_gaze_horizontal": 0.0,
            "eye_gaze_vertical": 0.0,
            "eye_open_ratio": 0.0,
            "eyebrow_direction": 0.0,
            "head_pitch": 0.0,
            "head_roll": 0.0,
            "head_yaw": 0.0,
            "lip_open_ratio": 0.0,
            "mouth_grim": 0.0,
            "mouth_position_horizontal": 0.0,
            "mouth_position_vertical": 0.0,
            "mouth_pout": 0.0,
            "mouth_purse": 0.0,
            "mouth_smile": 0.0,
        },
        name="My Face Editor image",
    )
    try:
        pydantic.TypeAdapter(models.V1AiFaceEditorCreateResponse).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a POST request to the /v1/ai-face-editor endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.V1AiFaceEditorCreateResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.v1.ai_face_editor.create(
        assets={"image_file_path": "api-assets/id/1234.png"},
        style={
            "enhance_face": False,
            "eye_gaze_horizontal": 0.0,
            "eye_gaze_vertical": 0.0,
            "eye_open_ratio": 0.0,
            "eyebrow_direction": 0.0,
            "head_pitch": 0.0,
            "head_roll": 0.0,
            "head_yaw": 0.0,
            "lip_open_ratio": 0.0,
            "mouth_grim": 0.0,
            "mouth_position_horizontal": 0.0,
            "mouth_position_vertical": 0.0,
            "mouth_pout": 0.0,
            "mouth_purse": 0.0,
            "mouth_smile": 0.0,
        },
        name="My Face Editor image",
    )
    try:
        pydantic.TypeAdapter(models.V1AiFaceEditorCreateResponse).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
