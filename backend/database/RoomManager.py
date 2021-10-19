import random
import FirebaseManager
from backend.util.util import hash_string_sha256

db = FirebaseManager.get_firestore()


def get_hosted_rooms_list(user_id):
    """
    Returns a list of room ids that are hosted by the given user_id
    """
    if type(user_id) is not str:
        raise Exception("Given arguments is not of type str")

    if user_id == "":
        raise Exception("Given argument cannot be empty")

    rooms = []
    query = db.collection("rooms").where("host_id", "==", user_id).get()
    for room in query:
        rooms.append(room.id)

    return rooms


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


def delete_room(user_id, room_id):
    """
    Deletes a room entry. Returns True if successfully deleted, else False
    """
    if type(user_id) is not str or type(room_id) is not str:
        raise Exception("Given arguments are not of type str")

    if user_id == "" or room_id == "":
        raise Exception("Given arguments cannot be empty")

    if room_id_exists(room_id) is False or is_room_host(user_id, room_id) is False:
        return False

    result = db.collection("rooms").document(room_id).delete()

    return True


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


def is_room_host(user_id, room_id):
    """
    Checks if a given user id is the room's host. Returns True if yes, else False
    """
    if type(user_id) is not str or type(room_id) is not str:
        raise Exception("Given arguments are not of type str")

    if user_id == "" or room_id == "":
        raise Exception("Given arguments cannot be empty")

    if room_id_exists(room_id) is False:
        return False

    rooms = db.collection("rooms").where("host_id", "==", user_id).get()
    if len(rooms) == 0:
        return False

    for room in rooms:
        if room.id == room_id:
            return True

    return False


def generate_room_id():
    return str(random.randint(0, 999999)).rjust(6, '0')
