import pathlib
import firebase_admin as fa
import sys
from firebase_admin import credentials
from firebase_admin import firestore

sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve()) + "/../..")

cred = credentials.Certificate(str(pathlib.Path(__file__).parent.resolve()) + "/../serviceAccountKey.json")

fa.initialize_app(cred)
db = firestore.client()


def get_firestore():
    return db
