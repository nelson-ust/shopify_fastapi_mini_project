from fastapi import APIRouter, HTTPException
from ..services.shopify_service import fetch_orders

router = APIRouter()

@router.get("/orders/{customer_id}")
async def read_orders(customer_id: str):
    # Check for non-zero numeric customer ID
    if not customer_id.isdigit() or int(customer_id) == 0:
        raise HTTPException(status_code=404, detail="Invalid customer ID format")

    numeric_customer_id = int(customer_id)

    # Validate for extremely large customer IDs
    if numeric_customer_id >= 1e18:  # Adjust the threshold as needed
        raise HTTPException(status_code=404, detail="Customer ID is too large")

    orders_data = await fetch_orders(numeric_customer_id)
    if orders_data is None:
        raise HTTPException(status_code=404, detail="No orders found for this customer ID")

    return orders_data
