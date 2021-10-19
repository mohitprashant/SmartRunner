import pathlib
import firebase_admin as fa
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve()) + "/../..")
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(str(pathlib.Path(__file__).parent.resolve()) + "/../serviceAccountKey.json")

fa.initialize_app(cred)
db = firestore.client()


def get_firestore():
    return db
