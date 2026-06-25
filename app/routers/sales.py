from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.sale import Sale

from app.services.inventory_service import (
    InventoryService
)

router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)


@router.post("/")
def create_sale(
        product_id: int,
        store_id: int,
        quantity: int,
        db: Session = Depends(get_db)
):

    inventory = InventoryService(db)

    inventory.reduce_stock(
        product_id,
        quantity
    )

    sale = Sale(
        product_id=product_id,
        store_id=store_id,
        quantity=quantity
    )

    db.add(sale)
    db.commit()

    return {
        "message": "sale recorded"
    }


@router.get("/")
def all_sales(
        db: Session = Depends(get_db)
):
    return db.query(Sale).all()