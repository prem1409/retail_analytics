import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.models.product import Base  # IMPORTANT: adjust import if Base is elsewhere


# TEST DATABASE (MySQL)
TEST_DATABASE_URL = (
    "mysql+pymysql://root:Prem1409$@localhost:3306/analytics"
)

engine = create_engine(TEST_DATABASE_URL, echo=False)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Create tables in TEST DB
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides = {}

client = TestClient(app)


@pytest.fixture
def test_client():
    return client