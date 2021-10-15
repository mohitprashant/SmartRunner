import pathlib
import firebase_admin as fa
import sys
import time
import hashlib
import random

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


def get_questions(subject, topic, room_id = "", quiz_name = ""):
    """
    Returns a randomised array of questions from the subject and topic.
    Each question is of a dictionary type.
    """
    query = db.collection("subjects").document(subject).collection(topic).get()
    questions = []
    
    for question in query:
        questions.append(question.to_dict())
        
    if room_id != "":
        if quiz_name == "":
            raise Exception("Quiz name is missing")

        custom_questions = get_custom_questions()
        for custom_question in custom_questions:
            questions.append(custom_question.to_dict())

    # This randomises the questions to prevent the same questions from being selected each time
    numQuestions = len(questions)
    randomised_questions = []
    samples = random.sample(range(numQuestions), numQuestions)
    for sample in samples:
        randomised_questions.append(questions[sample])

    return randomised_questions

def get_custom_questions(room_id, quiz_name):
    if type(room_id) is not str or type(quiz_name) is not str:
        raise Exception("Given arguments are not of type str")

    if room_id == "" or quiz_name == "":
        raise Exception("Given arguments cannot be empty")

    questions = db.collection("rooms")\
                            .document(room_id)\
                            .collection("quizzes")\
                            .document(quiz_name)\
                            .collection("questions")\
                            .get()
    
    return questions

def add_custom_questions(room_id, quiz_name, questions):
    """
    Adds the given list of custom questions to the room_id
    """
    if type(room_id) is not str or type(quiz_name) is not str:
        raise Exception("Given arguments are not of type str")

    if room_id == "" or quiz_name == "":
        raise Exception("Given arguments cannot be empty")

    if type(questions) is not list:
        raise Exception("Given question object is not a list")

    # Must check entire list before adding to database, or there will be duplicate additions
    for question in questions:
        check_fields(question, Enums.question_fields)

    for question in questions:
        db.collection("rooms").document(room_id)\
            .collection("quizzes").document(quiz_name)\
            .collection("questions").document().set(question)

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


def add_global_questions(subject, topic, questions):
    """
    Add a question to the specified subject and topic
    Throws an exception if the given question is not a dictionary type or does not have the specified keys
    """
    # Must check entire list before adding to database, or there will be duplicate additions
    for question in questions:
        check_fields(question, Enums.question_fields)

    for question in questions:
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

def create_room(host_id, room_name, room_password):
    """
    Creates a custom game room given host_id, room_name, room_password
    Returns the random 6 digit room_id as a string if successfully created, or an empty string if the room already exists
    """
    if type(host_id) is not str or type(room_name) is not str or type(room_password) is not str:
        raise Exception("Given arguments are not of type str")

    if host_id == "" or room_name == "" or room_password == "":
        raise Exception("Given arguments cannot be empty")

    if room_name_exists(room_name) is True:
        return ""

    # add password restriction checks here if required

    set_data = {
        "host_id": host_id, 
        "room_name": room_name, 
        "room_password_hash": hash_string_sha256(room_password)
    }

    room_id = generate_room_id()
    # Regenerate room_id until we get a unique one
    while room_id_exists(room_id):
        room_id = generate_room_id()

    db.collection("rooms").document(room_id).set(set_data)

    return room_id

def get_room_by_id(room_id):
    """
    Returns the DocumentSnapshot of a room if it exists. Returns an empty string if it does not.
    """
    if type(room_id) is not str:
        raise Exception("Given argument is not of type str")

    if room_id_exists(room_id) is False:
        return ""

    room = db.collection("rooms").document(room_id).get()
    return room

def join_room(room_id, room_password):
    if type(room_id) is not str or type(room_password) is not str:
        raise Exception("Given arguments are not of type str")

    if room_id == "" or room_password == "":
        raise Exception("Given arguments cannot be empty")
    
    room = get_room_by_id(room_id)
    if room == "":
        return False

    storedHash = room.to_dict()["room_password_hash"]
    if storedHash != hash_string_sha256(room_password):
        return False
    else:
        return True

def room_name_exists(room_name):
    """
    Returns True if room exists based on room_name, else False
    """
    if type(room_name) is not str:
        raise Exception("Given argument is not of type str")
    
    result = db.collection("rooms")\
                .where("room_name", "==", room_name)\
                .get()
    
    if len(result) != 0:
        return True
    else:
        return False

def room_id_exists(room_id):
    """
    Returns True if room exists based on room_id, else False
    """
    if type(room_id) is not str:
        raise Exception("Given argument is not of type str")
    
    result = db.collection("rooms").document(room_id).get()
    if result.exists:
        return True
    else:
        return False

def get_room_quizzes(room_id):
    """
    Returns a list of quizzes in this room_id. 
    Returns an empty list if the room does not have any custom quizzes or if the room does not exist.
    """
    if type(room_id) is not str:
        raise Exception("Given argument is not of type str")

    if room_id_exists(room_id) is False:
        return []

    quizzes = []
    
    query = db.collection("rooms").document(room_id).collection("quizzes").get()
    for quiz in query:
        quizzes.append(quiz.id)

    return quizzes
    
def generate_room_id():
    return str(random.randint(0, 999999)).rjust(6, '0')

def hash_string_sha256(plaintext):
    if type(plaintext) is not str:
        raise Exception("Given arguments is not of type str")
    
    return hashlib.sha256(plaintext.encode()).hexdigest()

# print(get_subjects())
# print(get_topics('Mathematics'))
# print(get_questions('Mathematics', 'Algebra'))
# print(len(get_questions('Mathematics', 'Algebra')))
