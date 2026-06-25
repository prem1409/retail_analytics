from pydantic import BaseModel

class SaleCreate(BaseModel):
    product_id: int
    store_id: int
    quantity: int