from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from datetime import datetime

from app.database import Base


class Sale(Base):

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    store_id = Column(
        Integer,
        ForeignKey("stores.id")
    )

    quantity = Column(Integer)

    sale_date = Column(
        DateTime,
        default=datetime.utcnow
    )