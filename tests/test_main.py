import json

import main

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def fastapi_test_client():
    client = TestClient(main.app)
    return client


def test_read_city_codes(helpers, fastapi_test_client):
    expected_city_code_msg = helpers().city_code_msg(
        filename="samples/city_code_samples.json"
    )
    city_code = fastapi_test_client.get("/api/v1/city_code/read")

    assert json.dumps(expected_city_code_msg) == json.dumps(city_code.json())


def test_read_crimes_count(helpers, fastapi_test_client):
    expected_crimes_count_msg = helpers().city_code_msg(
        filename="samples/crime_count_samples.json"
    )
    crimes_count = fastapi_test_client.get("/api/v1/crime_count/read")

    assert json.dumps(expected_crimes_count_msg) == json.dumps(crimes_count.json())

