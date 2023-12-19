from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

# Example of valid customer IDs (adjust according to your data)
VALID_CUSTOMER_IDS = [5592251564110, 2669175815] # Valid Custumer IDs
INVALID_CUSTOMER_IDS = [0, "not_valid_id"] # Non-existing or invalid IDs

# Test with valid customer IDs
@pytest.mark.parametrize("customer_id", VALID_CUSTOMER_IDS)
def test_get_orders_valid_customer_id(customer_id):
    response = client.get(f"/orders/{customer_id}")
    assert response.status_code == 200

# Test with invalid customer IDs
@pytest.mark.parametrize("customer_id", INVALID_CUSTOMER_IDS)
def test_get_orders_invalid_customer_id(customer_id):
    response = client.get(f"/orders/{customer_id}")
    assert response.status_code == 404 

# Test outragous Customer ID  cases
def test_get_orders_edge_cases():
    # Test with extremely large ID
    response = client.get("/orders/999999999999999999999")
    assert response.status_code == 404 
