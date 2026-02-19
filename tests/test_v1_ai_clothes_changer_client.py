import pydantic
import pytest

from magic_hour import AsyncClient, Client
from magic_hour.environment import Environment
from magic_hour.types import models


def test_create_200_success_all_params() -> None:
    """Tests a POST request to the /v1/ai-clothes-changer endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.V1AiClothesChangerCreateResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.v1.ai_clothes_changer.create(
        assets={
            "garment_file_path": "api-assets/id/outfit.png",
            "garment_type": "entire_outfit",
            "person_file_path": "api-assets/id/model.png",
        },
        name="My Clothes Changer image",
    )
    try:
        pydantic.TypeAdapter(models.V1AiClothesChangerCreateResponse).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a POST request to the /v1/ai-clothes-changer endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.V1AiClothesChangerCreateResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.v1.ai_clothes_changer.create(
        assets={
            "garment_file_path": "api-assets/id/outfit.png",
            "garment_type": "entire_outfit",
            "person_file_path": "api-assets/id/model.png",
        },
        name="My Clothes Changer image",
    )
    try:
        pydantic.TypeAdapter(models.V1AiClothesChangerCreateResponse).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
