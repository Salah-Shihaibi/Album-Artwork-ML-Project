import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("./serviceAccount.json")
firebase_admin.initialize_app(cred)

