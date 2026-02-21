"""Unit tests for the Flask application."""

import pytest
from unittest.mock import patch, Mock
import sys
import os

# Add parent directory to path to import app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app  # noqa: E402


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Test the home endpoint returns correct JSON."""
    response = client.get("/")
    assert response.status_code == 200

    json_data = response.get_json()
    assert json_data["service"] == "devex-sample"
    assert json_data["status"] == "ok"


def test_home_endpoint_content_type(client):
    """Test that home endpoint returns JSON content type."""
    response = client.get("/")
    assert response.content_type == "application/json"


@patch("app.requests.get")
def test_products_endpoint_success(mock_get, client):
    """Test the products endpoint with successful API response."""
    # Mock the external API response
    mock_response = Mock()
    mock_response.json.return_value = {
        "products": [
            {"id": 1, "title": "Product 1"},
            {"id": 2, "title": "Product 2"},
        ]
    }
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    response = client.get("/products")
    assert response.status_code == 200

    json_data = response.get_json()
    assert "products" in json_data
    assert len(json_data["products"]) == 2


@patch("app.requests.get")
def test_products_endpoint_api_failure(mock_get, client):
    """Test products endpoint handles API failures gracefully."""
    # Mock an API failure
    mock_get.side_effect = Exception("API unavailable")

    response = client.get("/products")
    # Flask will return 500 for unhandled exceptions
    assert response.status_code == 500


@patch("app.requests.get")
def test_products_endpoint_timeout(mock_get, client):
    """Test that products endpoint has proper timeout."""
    mock_get.side_effect = Exception("Timeout")

    response = client.get("/products")
    assert response.status_code == 500

    # Verify timeout parameter was used in the call
    mock_get.assert_called_once_with("https://dummyjson.com/products", timeout=10)


def test_invalid_endpoint(client):
    """Test that invalid endpoints return 404."""
    response = client.get("/nonexistent")
    assert response.status_code == 404
