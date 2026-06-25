
def test_get_sales(test_client):

    response = test_client.get("/sales/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)