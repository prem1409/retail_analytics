from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.services.analytics_service import (
    AnalyticsService
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/top-products")
def top_products(
        db: Session = Depends(get_db)
):
    return AnalyticsService(db).top_products()


@router.get("/revenue")
def revenue(
        db: Session = Depends(get_db)
):
    return {
        "revenue": AnalyticsService(db)
        .revenue()
    }


@router.get("/low-stock")
def low_stock(
        db: Session = Depends(get_db)
):
    return AnalyticsService(db).low_stock()


@router.get("/category-revenue")
def category_revenue(
        db: Session = Depends(get_db)
):
    return AnalyticsService(db).category_revenue()


@router.get("/store-revenue/{store_id}")
def store_revenue(
    store_id: int,
    db: Session = Depends(get_db)
):
    return AnalyticsService(db).store_revenue(store_id)


@router.get("/store-forecast/{store_id}")
def store_forecast(
    store_id: int,
    db: Session = Depends(get_db)
):
    return AnalyticsService(db).forecast_store_revenue(store_id)
