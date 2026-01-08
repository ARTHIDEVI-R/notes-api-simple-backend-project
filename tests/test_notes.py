from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_note():
    response = client.post("/notes", json={
        "title": "Test Note",
        "content": "Testing pytest integration"
    })
    assert response.status_code == 201
    assert "id" in response.json()


def test_get_note():
    response = client.get("/notes/1")
    assert response.status_code in [200, 404]

