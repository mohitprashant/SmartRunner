import firebase_admin as fa
from firebase_admin import credentials
from firebase_admin import firestore

# from firebase import firebase
# from firebase_admin import storage
# from google.cloud import storage
# from google.auth import load_credentials_from_file
# import requests

cred = credentials.Certificate("../serviceAccountKey.json")
fa.initialize_app(cred)
db = firestore.client()


def get_subjects():
    subjects = db.collection('subjects').get()
    items = []

    for subject in subjects:
        items.append(subject.to_dict())
        # print(doc.get())
        # print(f'{doc.id} => {doc.to_dict()}')

    print(items)
    return items


def get_topics(subject):
    topics = db.collection('subjects').document(subject).collections()

    for topic in topics:
        print(topic)
        for doc in topic:
            print(doc)

    print(topics)


#get_subjects()
get_topics('Mathematics')