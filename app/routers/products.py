from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.product import ProductCreate
from app.repositories.product_repository import ProductRepository

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/")
def create_product(
        product: ProductCreate,
        db: Session = Depends(get_db)
):

    repo = ProductRepository(db)

    return repo.create(product)


@router.get("/")
def get_products(
        db: Session = Depends(get_db)
):

    repo = ProductRepository(db)

    return repo.get_all()


@router.get("/{product_id}")
def get_product(
        product_id: int,
        db: Session = Depends(get_db)
):

    repo = ProductRepository(db)

    return repo.get_by_id(product_id)


@router.delete("/{product_id}")
def delete_product(
        product_id: int,
        db: Session = Depends(get_db)
):

    repo = ProductRepository(db)

    repo.delete(product_id)

    return {
        "message": "deleted"
    }