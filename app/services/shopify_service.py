import os
import httpx
from dotenv import load_dotenv
from typing import Optional, Dict

load_dotenv()

async def fetch_orders(customer_id: int) -> Optional[Dict]:
    shop_url = os.getenv("SHOP_URL")
    access_token = os.getenv("ACCESS_TOKEN")
    url = f"https://{shop_url}/admin/api/2023-01/orders.json?customer_id={customer_id}"
    headers = {"X-Shopify-Access-Token": access_token}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)

            # Check for successful response
            if response.status_code == 200:
                return response.json()  # Return the full JSON response

            # Handle other response statuses such as 404, 401, etc.
            response.raise_for_status()

        except httpx.HTTPStatusError as e:
            # Log the error details here, if necessary
            print(f"HTTP error occurred: {e}")
            return None
        except httpx.RequestError as e:
            # Log the request error details here, if necessary
            print(f"An error occurred while requesting {e.request.url!r}.")
            return None

    return None
