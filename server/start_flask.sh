export FIREBASE_AUTH_EMULATOR_HOST="localhost:9099"
firebase emulators:start
export FLASK_APP=main && flask run --host=0.0.0.0 --port 8080
