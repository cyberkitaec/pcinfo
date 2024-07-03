import pytest
from fastapi.testclient import TestClient
from main import app


test_client = TestClient(app)


def test_get_all_metrics():
    response = test_client.get(f"api/metrics")
    assert response.status_code == 200


def test_get_limit_metrics():
    limit_number = 40
    response = test_client.get(f"api/metrics/limit/{limit_number}")
    assert response.status_code == 200


