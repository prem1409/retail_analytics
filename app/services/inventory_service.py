from app.models.product import Product


class InventoryService:

    def __init__(self, db):
        self.db = db

    def reduce_stock(
        self,
        product_id,
        quantity
    ):
        product = (
            self.db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

        if not product:
            raise Exception("Product not found")

        if product.stock_quantity < quantity:
            raise Exception("Insufficient stock")

        product.stock_quantity -= quantity

        self.db.commit()