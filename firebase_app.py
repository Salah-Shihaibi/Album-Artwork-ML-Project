import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("./serviceAccount.json")
firebase_admin.initialize_app(cred)


def validate_token(request):
    try:
        idToken = request.headers.get("Authorization")
        return auth.verify_id_token(idToken)
    except Exception as err:
        raise err


def validate_access(decoded):
    try:
        return decoded["admin"]

    except Exception as err:
        raise err
