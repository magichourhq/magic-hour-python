import pytest
import pydantic

from magic_hour import AsyncClient, Client
from magic_hour.environment import Environment
from magic_hour.types import models


def test_get_200_generated_success():
    """Tests a GET request to the /v1/image-projects/{id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.V1ImageProjectsgetResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.v1.image_projects.get(id="string")
    try:
        pydantic.TypeAdapter(models.V1ImageProjectsgetResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v1/image-projects/{id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.V1ImageProjectsgetResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.v1.image_projects.get(id="string")
    try:
        pydantic.TypeAdapter(models.V1ImageProjectsgetResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_204_generated_success():
    """Tests a DELETE request to the /v1/image-projects/{id} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 204
    Mode: Synchronous execution

    Empty response expected

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.v1.image_projects.delete(id="string")
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Tests a DELETE request to the /v1/image-projects/{id} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 204
    Mode: Asynchronous execution

    Empty response expected

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.v1.image_projects.delete(id="string")
    assert response is None
