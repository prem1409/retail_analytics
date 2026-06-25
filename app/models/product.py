from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DECIMAL

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    category = Column(String(100))
    price = Column(DECIMAL(10, 2))
    stock_quantity = Column(Integer)