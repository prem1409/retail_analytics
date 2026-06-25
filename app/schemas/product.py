from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    category: str
    price: float
    stock_quantity: int


class ProductResponse(ProductCreate):
    id: int

    model_config = {
        "from_attributes": True
    }