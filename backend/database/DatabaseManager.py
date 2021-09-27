# from firebase import firebase

import firebase_admin as fa 
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

from google.cloud import storage
# from google.auth import load_credentials_from_file

import requests

cred = credentials.Certificate("../serviceAccountKey.json")
fa.initialize_app(cred)

db = firestore.client()

subjects = db.collection(u'subjects')
docs = subjects.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')