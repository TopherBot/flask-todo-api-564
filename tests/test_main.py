import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

sample = {"id": 1, "title": "Write tests", "completed": False}

def test_create_and_get_todo():
    # Create
    resp = client.post("/todos", json=sample)
    assert resp.status_code == 201
    assert resp.json() == sample

    # Retrieve
    resp = client.get(f"/todos/{sample['id']}")
    assert resp.status_code == 200
    assert resp.json() == sample

def test_list_todos():
    resp = client.get("/todos")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    # At least the previously created item is present
    assert any(item["id"] == sample["id"] for item in data)

def test_update_todo():
    updated = {"id": 1, "title": "Write more tests", "completed": True}
    resp = client.put(f"/todos/{sample['id']}", json=updated)
    assert resp.status_code == 200
    assert resp.json() == updated

    # Verify update persisted
    resp = client.get(f"/todos/{sample['id']}")
    assert resp.json() == updated

def test_delete_todo():
    resp = client.delete(f"/todos/{sample['id']}")
    assert resp.status_code == 204

    # Ensure it is gone
    resp = client.get(f"/todos/{sample['id']}")
    assert resp.status_code == 404
