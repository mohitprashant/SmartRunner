from backend.database import FirebaseManager

db = FirebaseManager.get_firestore()


def add_to_user_collection(username, user_token):
    """
    Returns a user dictionary object if given username exists
    """
    if type(username) is not str:
        raise Exception("Given arguments is not of type str")

    user = {
        'username': username,
        'user_token': user_token
    }

    try:
        existingUser = db.collection("users").where("username", "==", username).get()

        if not existingUser:
            user = db.collection("users").add(user)
            userid = user[1].id

            proficiencyFields = {
                'Algebra': "",
                'Calculus': "",
                'Geometry': "",
                'Numbers': "",
                'Statistics': ""
            }
            db.collection("users").document(userid).collection('proficiency').document('Mathematics')\
                .set(proficiencyFields)

    except:
        raise Exception("Could not add user")


def set_avatar(username, avatar):
    """
    :param username: Username of the user
    :param avatar: Avatar value to be set
    :return: Returns false if user does not exist. True if successfully set
    """
    if type(username) is not str or type(avatar) is not str:
        raise Exception("Given arguments are not of type str")

    if username == "" or avatar == "":
        raise Exception("Given arguments cannot be empty")

    if not user_exists(username):
        return False

    existing_user = get_user_collection_record(username)
    db.collection("users").document(existing_user.id).update({"avatar": avatar})
    return True


def get_avatar(username):
    """
    :param username: Username of the user
    :return: returns None if the user does not exist, else returns the string value of the avatar
    """
    if type(username) is not str:
        raise Exception("Given arguments are not of type str")

    if username == "":
        raise Exception("Given arguments cannot be empty")

    if not user_exists(username):
        return None

    user = get_user_collection_record(username).to_dict()
    if "avatar" in user:
        avatar = user["avatar"]
    else:
        avatar = None

    return avatar


def user_exists(username):
    """
    :param username: Username of the user
    :return: True if user exists
    :raises: An exception if database is corrupted
    """
    if type(username) is not str:
        raise Exception("Given arguments are not of type str")

    if username == "":
        return False

    existing_user = db.collection("users").where("username", "==", username).get()
    if len(existing_user) == 0:
        return False
    elif len(existing_user) == 1:
        return True
    else:
        raise Exception("Duplicate user entries in database. Please remove the duplicate entry")


def get_user_collection_record(username):
    return db.collection("users").where("username", "==", username).get()[0]


def delete_user_collection_record(username):
    if not user_exists(username):
        return False

    user = get_user_collection_record(username)
    db.collection("users").document(user.id).delete()
    return True


def get_user_token(username):
    if not user_exists(username):
        return None

    user = get_user_collection_record(username).to_dict()
    if "user_token" not in user:
        return None

    return user["user_token"]
