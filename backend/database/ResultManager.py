import random
from backend.database import FirebaseManager

db = FirebaseManager.get_firestore()


def save_game_results(result, room_id, quiz_id):
    """
    Saves the scores that a user has attained for a game in the room.
    :param result: Dictionary of score_board to be saved for this room_id and quiz_id. {“user1":30, “user5": 25, “user3":20}
    :param room_id: Room that this quiz is for.
    :param quiz_id: ID of the current quiz that is being saved.
    :return: true if scores were saved.
    """

    if type(result) is not dict:
        raise Exception("Given arguments is not of type dict")

    if type(room_id) is not str:
        raise Exception("Given arguments is not of type str")

    if type(quiz_id) is not str:
        raise Exception("Given arguments is not of type str")

    try:
        db.collection("rooms").document(room_id).collection("results").document(quiz_id).set(result)
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
