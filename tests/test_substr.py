def test_status(client):
    response = client.get('/')
    assert response.status == '200 OK'

def test_admin_status(client):
    print("Test1: Expect server to respond with status code 200")
    response = client.get('/admin')
    assert response.status_code == 200 

def test_admin_body(client):
    print("Test2: Expect server to respond with body")
    response = client.get('/admin')
    assert response.json["body"] == "You are an admin"


