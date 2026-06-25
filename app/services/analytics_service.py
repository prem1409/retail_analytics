from sqlalchemy import func
from sqlalchemy import desc


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