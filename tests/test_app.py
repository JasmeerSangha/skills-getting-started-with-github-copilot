import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

def test_signup_and_unregister():
    activity = "Chess Club"
    email = "testuser@mergington.edu"
    # Ensure user is not already registered
    client.delete(f"/activities/{activity}/unregister", params={"email": email})
    # Sign up
    response = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert response.status_code == 200
    assert f"Signed up {email}" in response.json()["message"]
    # Unregister
    response = client.delete(f"/activities/{activity}/unregister", params={"email": email})
    assert response.status_code == 200
    assert f"Unregistered {email}" in response.json()["message"]

def test_signup_duplicate():
    activity = "Chess Club"
    email = "testduplicate@mergington.edu"
    client.delete(f"/activities/{activity}/unregister", params={"email": email})
    client.post(f"/activities/{activity}/signup", params={"email": email})
    response = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]
    client.delete(f"/activities/{activity}/unregister", params={"email": email})

def test_unregister_not_registered():
    activity = "Chess Club"
    email = "notregistered@mergington.edu"
    response = client.delete(f"/activities/{activity}/unregister", params={"email": email})
    assert response.status_code == 400
    assert "not registered" in response.json()["detail"]
