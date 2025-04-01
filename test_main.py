import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "version" in data
    assert "status" in data
    assert "supported_tools" in data


def test_calculator_add():
    """Test calculator add operation"""
    response = client.post(
        "/execute",
        json={
            "tool_name": "calculator",
            "parameters": {"operation": "add", "numbers": [1, 2, 3]},
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["result"] == 6


def test_calculator_multiply():
    """Test calculator multiply operation"""
    response = client.post(
        "/execute",
        json={
            "tool_name": "calculator",
            "parameters": {"operation": "multiply", "numbers": [2, 3, 4]},
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["result"] == 24


def test_weather():
    """Test weather tool"""
    response = client.post(
        "/execute", json={"tool_name": "weather", "parameters": {"location": "Hanoi"}}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "location" in data["result"]
    assert "temperature" in data["result"]
    assert "condition" in data["result"]


def test_search():
    """Test search tool"""
    response = client.post(
        "/execute",
        json={"tool_name": "search", "parameters": {"query": "python programming"}},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "query" in data["result"]
    assert "results" in data["result"]


def test_invalid_tool():
    """Test invalid tool name"""
    response = client.post(
        "/execute", json={"tool_name": "invalid_tool", "parameters": {}}
    )
    assert response.status_code == 400


def test_calculator_invalid_operation():
    """Test calculator with invalid operation"""
    response = client.post(
        "/execute",
        json={
            "tool_name": "calculator",
            "parameters": {"operation": "divide", "numbers": [1, 2]},
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is False
    assert "error" in data
