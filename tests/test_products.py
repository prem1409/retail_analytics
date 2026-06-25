def test_create_product(test_client):
    
    response = test_client.post(
        "/products/",
        json={
            "name": "Drill",
            "category": "Tools",
            "price": 100.0,
            "stock_quantity": 50
        }
    )

    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "Drill"
    assert data["category"] == "Tools"
    assert data["stock_quantity"] == 50


def test_get_products(test_client):

    response = test_client.get("/products/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_product_by_id(test_client):

    create = test_client.post(
        "/products/",
        json={
            "name": "Hammer",
            "category": "Tools",
            "price": 50.0,
            "stock_quantity": 20
        }
    )

    product_id = create.json()["id"]

    response = test_client.get(f"/products/{product_id}")

    assert response.status_code == 200
    assert response.json()["name"] == "Hammer"