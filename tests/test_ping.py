def test_ping(client):
    response = client.get('/')
    assert response.status == '200 OK'




