import pydantic
import pytest

from magic_hour import AsyncClient, Client
from magic_hour.environment import Environment
from magic_hour.types import models


def test_create_200_success_all_params():
    """Tests a POST request to the /v1/face-detection endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.V1FaceDetectionCreateResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.v1.face_detection.create(
        assets={"target_file_path": "api-assets/id/1234.png"}, confidence_score=0.5
    )
    try:
        pydantic.TypeAdapter(models.V1FaceDetectionCreateResponse).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params():
    """Tests a POST request to the /v1/face-detection endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.V1FaceDetectionCreateResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.v1.face_detection.create(
        assets={"target_file_path": "api-assets/id/1234.png"}, confidence_score=0.5
    )
    try:
        pydantic.TypeAdapter(models.V1FaceDetectionCreateResponse).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params():
    """Tests a GET request to the /v1/face-detection/{id} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.V1FaceDetectionGetResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.v1.face_detection.get(id="uuid-example")
    try:
        pydantic.TypeAdapter(models.V1FaceDetectionGetResponse).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params():
    """Tests a GET request to the /v1/face-detection/{id} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.V1FaceDetectionGetResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.v1.face_detection.get(id="uuid-example")
    try:
        pydantic.TypeAdapter(models.V1FaceDetectionGetResponse).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
