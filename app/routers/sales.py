from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.sale import Sale
from app.models.product import Product
from app.models.store import Store
from app.schemas.sale import SaleCreate

router = APIRouter(prefix="/sales", tags=["Sales"])


@router.post("/")
def create_sale(
    request: SaleCreate,
    db: Session = Depends(get_db)
):

    try:
        # 1. Validate product
        product = (
            db.query(Product)
            .filter(Product.id == request.product_id)
            .first()
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        # 2. Validate store
        store = (
            db.query(Store)
            .filter(Store.id == request.store_id)
            .first()
        )

        if not store:
            raise HTTPException(
                status_code=404,
                detail="Store not found"
            )

        # 3. Validate stock
        if product.stock_quantity < request.quantity:
            raise HTTPException(
                status_code=400,
                detail="Insufficient stock"
            )

        # 4. Reduce stock
        product.stock_quantity -= request.quantity

        # 5. Create sale
        sale = Sale(
            product_id=request.product_id,
            store_id=request.store_id,
            quantity=request.quantity
        )

        db.add(sale)

        # 6. Commit BOTH operations together
        db.commit()

        return {
            "message": "sale recorded"
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.get("/")
def all_sales(
        db: Session = Depends(get_db)
):
    return db.query(Sale).all()