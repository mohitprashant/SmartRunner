import firebase_admin
from firebase_admin import firestore
from backend.database import FirebaseManager
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
            'player_end_time': firestore.SERVER_TIMESTAMP
        }

        db.collection("rooms").document(room_id).collection("quizzes").document(quiz_name) \
            .collection("player results").document(username).set(result)
        return True
    except:
        raise Exception("Scores could not be saved")


def get_game_results(room_id, quiz_id):
    """
    Saves the scores that a user has attained for a game in the room.
    :param room_id: Room that this quiz was for.
    :param quiz_id: ID of the  quiz that was saved.
    :return: List of scores.
    """

    if type(room_id) is not str:
        raise Exception("Given arguments is not of type str")

    if type(quiz_id) is not str:
        raise Exception("Given arguments is not of type str")

    try:
        query = db.collection("rooms").document(room_id).collection("results").document(quiz_id).get()
        scores = query.to_dict()

        return scores
    except:
        raise Exception("Error retrieving scores")
