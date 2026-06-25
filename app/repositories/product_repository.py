from app.models.product import Product


class ProductRepository:

    def __init__(self, db):
        self.db = db

    def create(self, product):

        db_product = Product(**product.dict())

        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)

        return db_product

    def get_all(self):
        return self.db.query(Product).all()

    def get_by_id(self, product_id):
        return (
            self.db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

    def delete(self, product_id):

        product = self.get_by_id(product_id)

        if product:
            self.db.delete(product)
            self.db.commit()