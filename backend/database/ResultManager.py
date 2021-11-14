import firebase_admin
from backend.database import Enums
from firebase_admin import firestore
from backend.database import FirebaseManager
from backend.database.DatabaseManager import check_fields
from backend.database.RoomManager import room_id_exists, get_room_quizzes_list

db = FirebaseManager.get_firestore()


def save_game_results(room_id, quiz_name, username, attempted, correct):
    """
    :param room_id: 6 digit ID of the room
    :param quiz_name: Unique name of quiz
    :param username: Username of the user to be saved
    :param attempted: Questions attempted by user
    :param correct: Correct answers by user
    :return:
    """

    if type(room_id) is not str or type(quiz_name) is not str or type(username) \
            is not str:
        raise Exception("Given arguments is not of type str")

    if type(attempted) is not int or type(correct) is not int:
        raise Exception("Given arguments is not of type int")

    if room_id == "" or quiz_name == "" or username == "":
        raise Exception("Given arguments cannot be empty")

    if not room_id_exists(room_id):
        return False

    current_quizzes = get_room_quizzes_list(room_id)
    if quiz_name not in current_quizzes:
        return False

    try:
        result = {
            'no_of_questions_attempted': attempted,
            'no_of_questions_correct': correct,
            'player_end_time': firestore.SERVER_TIMESTAMP,
            'player_name': username
        }

        db.collection("rooms").document(room_id).collection("quizzes").document(quiz_name) \
            .collection("player results").document().set(result)
        return True
    except:
        raise Exception("Scores could not be saved")


def get_game_results_list(room_id, quiz_name):
    """
    :param room_id: 6 digit ID of the room
    :param quiz_name: Unique name of quiz
    :return: List of scores.
    """

    if type(room_id) is not str or type(quiz_name) is not str:
        raise Exception("Given arguments is not of type str")

    if room_id == "" or quiz_name == "":
        raise Exception("Given arguments cannot be empty")

    try:
        query = db.collection("rooms").document(room_id).collection("quizzes").document(quiz_name) \
            .collection("player results").get()
        results = []
        for q in query:
            result = q.to_dict()
            results.append(result)

        return results
    except:
        raise Exception("Error retrieving scores")


def set_game_question_results(room_id, quiz_name, question_result):
    check_fields(question_result, Enums.question_result_fields)

    try:
        db.collection('rooms').document(room_id).collection('quizzes').document(quiz_name) \
            .collection('question results').document().set(question_result)
    except:
        raise Exception("Error setting scores")


def get_game_question_results_list(room_id, quiz_name):
    query = db.collection('rooms').document(room_id).collection('quizzes').document(
        quiz_name).collection('question results').get()

    players_results = []
    for player_result in query:
        players_results.append(player_result.to_dict())

    return players_results
