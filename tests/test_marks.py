'''
import ast
import pytest

@pytest.mark.slash
def test_status(client):
    response = client.get('/')
    assert response.status == '200 OK'

@pytest.mark.admin
def test_admin_status(client):
    print("Test1: Expect server to respond with status code 200")
    response = client.get('/admin')
    print(type(response.data), "<<<<<<<<<<<<")
    assert response.status_code == 200 

@pytest.mark.admin
def test_admin_body(client):
    print("Test2: Expect server to respond with body")
    response = client.get('/admin')
    print(response.data)
    dict_str = response.data.decode("UTF-8")
    response_data = ast.literal_eval(dict_str)
    assert response_data["body"] == "You are an admin"
'''