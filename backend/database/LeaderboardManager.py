from backend.database import FirebaseManager
from backend.database import Enums
from backend.database.DatabaseManager import check_fields

db = FirebaseManager.get_firestore()


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


def get_leaderboard_subjects():
    """
    Returns a list of available leaderboards
    """
    query = db.collection('leaderboard').list_documents()
    subjects = []

    for subject in query:
        subjects.append(subject.id)

    return subjects


def get_leaderboard_topics(subject):
    """
    Returns a list of available leaderboards topics for a given subject.
    :param subject: Subject whose leaderboard topics to retrieve.
    :return: List of topics.
    """
    if type(subject) is not str:
        raise Exception("Given argument is not of type str")

    topics = db.collection('leaderboard').document(subject).collections()
    items = []

    for topic in topics:
        items.append(topic.id)

    return items

