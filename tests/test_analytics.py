def test_revenue_endpoint(test_client):
    
    response = test_client.get("/analytics/revenue")

    assert response.status_code == 200
    assert "revenue" in response.json()


def test_top_products(test_client):

    response = test_client.get("/analytics/top-products")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_low_stock(test_client):

    response = test_client.get("/analytics/low-stock")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_category_revenue(test_client):

    response = test_client.get("/analytics/category-revenue")

    assert response.status_code == 200
    assert isinstance(response.json(), list)