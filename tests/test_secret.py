from firebase_app import auth
import requests

# no JWT sent
def test_no_jwt_sent(client):    
    headers = {
    }
    response = client.get('/secret', headers = headers)
    assert response.status_code == 401
    headers = {
        "authorization":""
    }
    response = client.get('/secret', headers = headers)
    assert response.status_code == 401


# valid token returns status code 200, and ed's secret
def test_jwt_valid_code(client):
    
    # create new user
    user = auth.create_user(
        email = 'firstUser@user.com',
        password = 'password123',
    )

    response = sign_in_test_user()    
    print(response)
    
    headers = {
        "authorization":response['idToken']
    }
    response = client.get('/secret', headers = headers)
    assert response.json["secret"] == "I have an identical twin, also called ed"
    assert response.status_code == 200


sign_in_url = "http://localhost:9099/identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=fake-key"

def sign_in_test_user():
    response = requests.post(sign_in_url, json={ "email": "firstUser@user.com", "password": "password123"})

    return response.json()