import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert "Day 19 Search API" in response.json()["name"]

def test_healthz():
    with TestClient(app) as client:
        response = client.get("/healthz")
        assert response.status_code == 200
        assert response.json()["ready"] is True

def test_search_endpoint():
    with TestClient(app) as client:
        response = client.get("/search", params={"q": "machine learning", "mode": "hybrid", "top_k": 5})
        assert response.status_code == 200
        data = response.json()
        assert data["query"] == "machine learning"
        assert len(data["hits"]) == 5
        assert "latency_ms" in data

def test_search_invalid_mode():
    with TestClient(app) as client:
        response = client.get("/search", params={"q": "test", "mode": "invalid"})
        assert response.status_code == 422 # FastAPI validation error for Literal
