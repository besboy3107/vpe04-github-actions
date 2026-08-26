"""Автотесты HTTP-эндпоинтов приложения."""

import pytest

from app import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Docker" in response.get_json()["message"]


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_info(client):
    response = client.get("/info")
    data = response.get_json()
    assert response.status_code == 200
    assert data["application"] == "VPe04 GitHub Actions App"
    assert data["deployment"] == "GitHub Actions -> VPS"
    assert data["python_version"]
    assert data["version"] == "local"


@pytest.mark.parametrize(
    ("path", "expected"),
    [("/calc/7/5", 12), ("/multiply/7/5", 35), ("/divide/10/2", 5.0)],
)
def test_calculations(client, path, expected):
    response = client.get(path)
    assert response.status_code == 200
    assert response.get_json()["result"] == expected


def test_division_by_zero(client):
    response = client.get("/divide/10/0")
    assert response.status_code == 400
    assert response.get_json() == {"error": "Division by zero is not allowed"}


def test_unknown_route(client):
    assert client.get("/unknown").status_code == 404
