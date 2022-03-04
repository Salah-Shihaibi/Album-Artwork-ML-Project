def test_status(client):
    response = client.get('/')
    assert response.status == '200 OK'




