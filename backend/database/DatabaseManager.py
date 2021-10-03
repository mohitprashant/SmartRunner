import pathlib
import firebase_admin as fa
from uuid import uuid4 as genUid
from firebase_admin import credentials
from firebase_admin import firestore
from Enums import leaderboardSize, leaderboard_user_fields, question_fields
# from firebase import firebase
# from firebase_admin import storage
# from google.cloud import storage
# from google.auth import load_credentials_from_file
# import requests

cred = credentials.Certificate(str(pathlib.Path(__file__).parent.resolve()) + "/../serviceAccountKey.json")
fa.initialize_app(cred)
db = firestore.client()


def get_subjects():
    subjects = db.collection('subjects').get()
    items = []

    for subject in subjects:
        items.append(subject.id)

    print(items)
    return items


def get_topics(subject):
    topics = db.collection('subjects').document(subject).collections()
    items = []

    for topic in topics:
        items.append(topic.id)

    print(items)
    return items


def get_questions(subject, topic):
    """
    Returns an array of questions from the subject and topic.
    Each question is of a dictionary type.
    """
    query = db.collection("subjects").document(subject).collection(topic).get()
    questions = []
    
    for question in query:
        questions.append(question.to_dict())
        
    return questions


def get_leaderboard(subject, topic):
    """
    Returns a sorted list of users in the specified leaderboard by increasing order
    """
    query = db.collection("leaderboard").document(subject).collection(topic).get()
    unsorted = []
    for user in query:
        unsorted.append(user.to_dict())

    sorted = []
    smallest_idx = 0
    while (len(unsorted) > 0):
        for i in range(len(unsorted)):
            if unsorted[i]["score"] < unsorted[smallest_idx]["score"]:
                smallest_idx = i
        
        sorted.append(unsorted[smallest_idx])
        unsorted.pop(smallest_idx)
        smallest_idx = 0

    return sorted


def update_leaderboard(user, subject, topic):
    check_fields(user, leaderboard_user_fields)
    currentLeaderboard = get_leaderboard(subject, topic)

    if len(currentLeaderboard) < leaderboardSize:
        # Just insert
        db.collection("leaderboard").document(subject).collection(topic).document().set(user)
    else:
        # Remove lowest and insert next highest
        lowestCollection = db.collection("leaderboard").document(subject).collection(topic)\
                    .where("uid", "==", currentLeaderboard[0]['uid'])\
                    .where("score", "==", currentLeaderboard[0]['score']).get()

        if len(lowestCollection) > 0 and lowestCollection[0].to_dict()['score'] < user['score']:
            db.collection("leaderboard").document(subject).collection(topic).document(lowestCollection[0].id).delete()
            db.collection("leaderboard").document(subject).collection(topic).document().set(user)


def add_question(subject, topic, question):
    """
    Add a question to the specified subject and topic
    Throws an exception if the given question is not a dictionary type or does not have the specified keys
    """
    check_fields(question, question_fields)
    
    db.collection("subjects").document(subject).collection(topic).document().set(question)
    return question


def check_fields(item, fields):
    if type(item) is not dict:
        raise Exception("Item is not of a dictionary type")

    for field in fields:
        if field not in item:
            raise Exception("Item does not have the key " + field)
         
        if type(item[field]) is not fields[field]["Type"]:
            raise Exception("Given " + field + " is not of type " + str(fields[field]["Type"]))


def get_user_by_username(username):
    """
    Returns a user dictionary object if given username exists
    """
    users = db.collection("users").where("username", "==", username).get()
    
    if len(users) != 1:
        # username should be unique. return empty dict if more than 1 users (something is wrong) or no user found
        return {}
    
    return users[0].to_dict()


get_subjects()
get_topics('Mathematics')
get_questions('Mathematics', 'Algebra')
