import requests

BASE_URL = "https://example.com/api"

def test_health_endpoint():
    """
    Example API smoke test.

    In production, this would typically be part of a larger
    test suite validating service readiness and dependencies.
    """
    response = requests.get(f"{BASE_URL}/health")

    assert response.status_code == 200
    assert response.json().get("status") == "ok"


def test_user_creation_contract():
    """
    Example contract-style test.

    Focuses on response structure and key fields rather than
    full business logic.
    """
    payload = {
        "email": "test@example.com",
        "name": "Test User"
    }

    response = requests.post(f"{BASE_URL}/users", json=payload)

    assert response.status_code == 201
    body = response.json()

    assert "id" in body
    assert body["email"] == payload["email"]
