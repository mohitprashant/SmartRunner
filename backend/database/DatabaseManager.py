import pathlib
import firebase_admin as fa
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve()) + "/../..")
from firebase_admin import credentials
from firebase_admin import firestore
from backend.database import Enums

cred = credentials.Certificate(str(pathlib.Path(__file__).parent.resolve()) + "/../serviceAccountKey.json")

fa.initialize_app(cred)
db = firestore.client()


def get_subjects():
    """
        Returns a list of available subjects.
    """
    subjects = db.collection('subjects').list_documents()
    items = []

    for subject in subjects:
        items.append(subject.id)

    return items


def get_topics(subject):
    """
        Returns a list of available topics for a given subject.
    """
    topics = db.collection('subjects').document(subject).collections()
    items = []

    for topic in topics:
        items.append(topic.id)

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
    unsorted_list = []
    for user in query:
        unsorted_list.append(user.to_dict())

    sorted_list = []
    smallest_idx = 0
    while len(unsorted_list) > 0:
        for i in range(len(unsorted_list)):
            if unsorted_list[i]["score"] < unsorted_list[smallest_idx]["score"]:
                smallest_idx = i
            elif unsorted_list[i]["score"] == unsorted_list[smallest_idx]["score"]:
                if unsorted_list[i]["epochTimeAdded"] > unsorted_list[smallest_idx]["epochTimeAdded"]:
                    smallest_idx = i
        
        sorted_list.append(unsorted_list[smallest_idx])
        unsorted_list.pop(smallest_idx)
        smallest_idx = 0

    return sorted_list


def update_leaderboard(user, subject, topic):
    check_fields(user, Enums.leaderboard_user_fields)
    currentLeaderboard = get_leaderboard(subject, topic)

    if len(currentLeaderboard) < Enums.leaderboardSize:
        # Just insert
        db.collection("leaderboard").document(subject).collection(topic).document().set(user)
    else:
        # Remove lowest and insert next highest
        lowestCollection = db.collection("leaderboard").document(subject).collection(topic)\
                    .where("uid", "==", currentLeaderboard[0]['uid'])\
                    .where("score", "==", currentLeaderboard[0]['score'])\
                    .where("epochTimeAdded", "==", currentLeaderboard[0]['epochTimeAdded'])\
                    .get()

        if len(lowestCollection) > 0 and lowestCollection[0].to_dict()['score'] < user['score']:
            db.collection("leaderboard").document(subject).collection(topic).document(lowestCollection[0].id).delete()
            db.collection("leaderboard").document(subject).collection(topic).document().set(user)


def add_question(subject, topic, question):
    """
    Add a question to the specified subject and topic
    Throws an exception if the given question is not a dictionary type or does not have the specified keys
    """
    check_fields(question, Enums.question_fields)
    
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

# print(get_subjects())
# print(get_topics('Mathematics'))
# print(get_questions('Mathematics', 'Algebra'))
# print(len(get_questions('Mathematics', 'Algebra')))
