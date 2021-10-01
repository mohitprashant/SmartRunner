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


def getSubjects():
    subjects = db.collection('subjects').get()
    items = []

    for subject in subjects:
        items.append(subject.id)

    print(items)
    return items


def getTopics(subject):
    topics = db.collection('subjects').document(subject).collections()
    items = []

    for topic in topics:
        items.append(topic.id)

    print(items)
    return items


def getQuestions(subject, topic):
    """
    Returns an array of questions from the subject and topic.
    Each question is of a dictionary type.
    """
    query = db.collection("subjects").document(subject).collection(topic).get()
    questions = []
    
    for question in query:
        questions.append(question.to_dict())
        
    return questions

def getLeaderboard(subject, topic):
    """
    Returns an unsorted list of users in the specified leaderboard
    """
    query = db.collection("leaderboard").document(subject).collection(topic).get()
    users = []
    for user in query:
        users.append(user.to_dict())
    
    return users

def addQuestion(subject, topic, question):
    """
    Add a question to the specified subject and topic
    Throws an exception if the given question is not a dictionary type or does not have the specified keys
    """
    if type(question) is not dict:
        raise Exception("Question is not of a dictionary type")

    question_keys = ["Description", "Difficulty_level", "Correct", "Wrong_1", "Wrong_2", "Wrong_3"]
    for question_key in question_keys:
        if question_key not in question:
            raise Exception("Question does not have the key " + question_key)
         
        if question_key == "Difficulty_level" and type(question[question_key]) is not int:
            raise Exception("Given difficulty_level is not of type int")
    
    db.collection("subjects").document(subject).collection(topic).document().set(question)
    return question
    
def getUserByUsername(username):
    """
    Returns a user dictionary object if given username exists
    """
    users = db.collection("users").where("username", "==", username).get()
    
    if len(users) != 1:
        # username should be unique. return empty dict if more than 1 users (something is wrong) or no user found
        return {}
    
    return users[0].to_dict()

getSubjects()
getTopics('Mathematics')
getQuestions('Mathematics', 'Algebra')
