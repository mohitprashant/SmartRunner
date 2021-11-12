import random
from backend.database import FirebaseManager
from backend.util.util import hash_string_sha256

db = FirebaseManager.get_firestore()


def get_hosted_rooms_list(username):
    """
    Returns a list of room ids that are hosted by the given username
    """
    if type(username) is not str:
        raise Exception("Given arguments is not of type str")

    if username == "":
        raise Exception("Given argument cannot be empty")

    rooms = []
    query = db.collection("rooms").where("host_username", "==", username).get()
    for room in query:
        rooms.append(room.id)

    return rooms


def create_room(host_username, room_name, room_password):
    """
    Creates a custom game room given host_username, room_name, room_password
    Returns the random 6 digit room_id as a string if successfully created, or an empty string if the room already exists
    """
    if type(host_username) is not str or type(room_name) is not str or type(room_password) is not str:
        raise Exception("Given arguments are not of type str")

    if host_username == "" or room_name == "" or room_password == "":
        raise Exception("Given arguments cannot be empty")

    if room_name_exists(room_name) is True:
        return ""

    # add password restriction checks here if required

    set_data = {
        "host_username": host_username,
        "room_name": room_name,
        "room_password_hash": hash_string_sha256(room_password)
    }

    room_id = generate_room_id()
    # Regenerate room_id until we get a unique one
    while room_id_exists(room_id):
        room_id = generate_room_id()

    db.collection("rooms").document(room_id).set(set_data)

    return room_id


def delete_room(curr_username, room_id):
    """
    :param curr_username: Username of current user
    :param room_id: Room id of room to be deleted
    :return: True if successfully deleted, else False
    """
    if type(curr_username) is not str or type(room_id) is not str:
        raise Exception("Given arguments are not of type str")

    if curr_username == "" or room_id == "":
        raise Exception("Given arguments cannot be empty")

    if room_id_exists(room_id) is False or is_room_host(curr_username, room_id) is False:
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


def join_room(room_id, room_password, username):
    if type(room_id) is not str or type(room_password) is not str or type(username) is not str:
        raise Exception("Given arguments are not of type str")

    if room_id == "" or room_password == "" or username == "":
        raise Exception("Given arguments cannot be empty")

    room = get_room_by_id(room_id)
    if room == "":
        return False

    storedHash = room.to_dict()["room_password_hash"]
    if storedHash != hash_string_sha256(room_password):
        return False

    db.collection("rooms").document(room_id).collection("members").document(username).set({"status": 0})
    return True


def room_name_exists(room_name):
    """
    Returns True if room exists based on room_name, else False
    """
    if type(room_name) is not str:
        raise Exception("Given argument is not of type str")

    result = db.collection("rooms") \
        .where("room_name", "==", room_name) \
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


def get_room_quizzes_list(room_id):
    """
    :param room_id: 6 digit ID of room
    :return: List of quiz names inside this room
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


def is_room_host(username, room_id):
    """
    :param username: Username of current user
    :param room_id: Room ID of room to be deleted
    :return:  Returns True if yes, else False
    """
    if type(username) is not str or type(room_id) is not str:
        raise Exception("Given arguments are not of type str")

    if username == "" or room_id == "":
        raise Exception("Given arguments cannot be empty")

    if room_id_exists(room_id) is False:
        return False

    rooms = db.collection("rooms").where("host_username", "==", username).get()
    if len(rooms) == 0:
        return False

    for room in rooms:
        if room.id == room_id:
            return True

    return False


def generate_room_id():
    return str(random.randint(0, 999999)).rjust(6, '0')


def get_room_name_from_id(room_id):
    """
    Returns room_name of a room if it exists. Returns an empty string if it does not.
    """
    if type(room_id) is not str:
        raise Exception("Given argument is not of type str")

    if room_id_exists(room_id) is False:
        return ""

    query = db.collection("rooms").document(room_id).get()
    room = query.to_dict()
    room_name = room.get('room_name')

    return room_name


def get_list_of_rooms_by_host(host_username):
    """
    Returns room_name of a room if it exists. Returns an empty string if it does not.
    """
    if type(host_username) is not str:
        raise Exception("Given argument is not of type str")

    query = db.collection("rooms").where("host_username", "==", host_username).get()

    rooms = []
    for room in query:
        rooms.append(room.id)

    return rooms


def set_member_status(room_id, username, status=0):
    """
    Saves the scores that a user has attained for a game in the room.
    :param room_id: Room that this quiz is for.
    :param username: Member whose ready status is to be updated.
    :param status: Status to be updated. Has to be 0 (unready) or 1 (ready).
    :return: true if status was saved.
    """

    if type(room_id) is not str:
        raise Exception("Given arguments is not of type str")

    if type(username) is not str:
        raise Exception("Given arguments is not of type str")

    if type(status) is not int:
        raise Exception("Given arguments is not of type int")

    if status != 1 & status != 0:
        raise Exception("Given status is not 0 or 1")

    status_dict = {"status":status}

    try:
        db.collection("rooms").document(room_id).collection("members").document(username).set(status_dict)
        return True
    except:
        raise Exception("Status could not be saved")


def get_room_member_statuses(room_id):
    """
    Returns dictionary of members in a room and their corresponding ready statuses.
    :param room_id: Room whose status to retrieve.
    :return: Returns a dictionary of usernames and the corresponding ready statuses.
    """

    if type(room_id) is not str:
        raise Exception("Given arguments is not of type str")

    members = {}
    query = db.collection("rooms").document(room_id).collection("members").get()
    for member in query:
        temp_status = member.to_dict()
        members[member.id] = temp_status["status"]

    return members


def is_user_in_room(username, room_id):
    """
    :param username: Username/email of the user
    :param room_id: Room id of the room to look for
    :return: True if user is in room, else False
    """
    if room_id_exists(room_id) is False:
        return False

    query = db.collection("rooms").document(room_id).collection("members").get()
    for user in query:
        if user.id == username:
            return True
    return False


def remove_user_from_room(current_username, removed_username, room_id):
    """
    :param current_username: Username of current user
    :param removed_username: username of user to be removed
    :param room_id: ID of the room that removed_username is supposed to be removed from
    :return: True if user is removed or user is not in room or room does not exist. False if current_username is not removed_username, or is not host
    """
    if not room_id_exists(room_id):
        return True

    if current_username != removed_username and not is_room_host(current_username, room_id):
        return False

    if not is_user_in_room(removed_username, room_id):
        return False

    query = db.collection("rooms").document(room_id).collection("members").get()
    for user in query:
        if user.id == removed_username:
            db.collection("rooms").document(room_id).collection("members").document(user.id).delete()

    return True
