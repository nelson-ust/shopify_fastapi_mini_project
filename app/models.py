from pydantic import BaseModel

class Order(BaseModel):
    id: int
    #customer_id: int