from fastapi import FastAPI

from app.routers.products import router as products
from app.routers.sales import router as sales
from app.routers.analytics import router as analytics

app = FastAPI(
    title="Retail Analytics Platform"
)

app.include_router(products)
app.include_router(sales)
app.include_router(analytics)


@app.get("/")
def health():

    return {
        "status": "running"
    }