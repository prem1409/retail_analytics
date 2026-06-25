from sqlalchemy import func
from sqlalchemy import desc

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

from app.models.sale import Sale
from app.models.product import Product


class AnalyticsService:

    def __init__(self, db):
        self.db = db

    def top_products(self):

        rows = (
            self.db.query(
                Product.name,
                func.sum(Sale.quantity)
                .label("units_sold")
            )
            .join(
                Sale,
                Product.id == Sale.product_id
            )
            .group_by(Product.name)
            .all()
        )
        rows=  sorted(rows, key=lambda row: row.units_sold, reverse=True)

        return [
            {
                "product_name": row.name,
                "units_sold": row.units_sold
            }
            for row in rows
        ]

    def revenue(self):

        rows = (
            self.db.query(
                Product.price,
                Sale.quantity
            )
            .join(
                Sale,
                Product.id == Sale.product_id
            )
            .all()
        )

        total = 0

        for row in rows:
            total += float(row.price) * row.quantity

        return total

    def low_stock(self):

        return (
            self.db.query(Product)
            .filter(
                Product.stock_quantity < 10
            )
            .all()
        )

    def category_revenue(self):

        rows = (
            self.db.query(
                Product.category,
                func.sum(
                    Product.price *
                    Sale.quantity
                ).label("revenue")
            )
            .join(
                Sale,
                Product.id == Sale.product_id
            )
            .group_by(
                Product.category
            )
            .all()
        )
        rows = sorted(rows, key=lambda row: row.revenue, reverse=True)

        return  [
            {
                "product_category": row.category,
                "revenue": row.revenue
            }
            for row in rows
        ]

    def store_revenue(self, store_id):
        rows = (
            self.db.query(
                func.date(Sale.sale_date).label("date"),
                func.sum(Product.price * Sale.quantity).label("revenue")
            )
            .join(Product)
            .filter(Sale.store_id == store_id)
            .group_by(func.date(Sale.sale_date))
            .order_by(func.date(Sale.sale_date))
            .all()
        )
        return  [
            {
                "date": row.date,
                "revenue": row.revenue
            }
            for row in rows
        ]

    def forecast_store_revenue(self, store_id):
        data = self.store_revenue(store_id)

        df = pd.DataFrame(data, columns=["date", "revenue"])

        if len(df) < 2:
            return {"message": "Not enough data"}

        df["day_index"] = np.arange(len(df))

        X = df[["day_index"]]
        y = df["revenue"]

        model = LinearRegression()
        model.fit(X, y)

        next_day = np.array([[len(df)]])

        prediction = model.predict(next_day)[0]

        return {
            "store_id": store_id,
            "forecast_next_day_revenue": float(prediction)
        }