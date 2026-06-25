from app.database import Base
from app.database import engine

from app.models.product import Product
from app.models.sale import Sale
from app.models.store import Store

Base.metadata.create_all(bind=engine)

print("tables created")