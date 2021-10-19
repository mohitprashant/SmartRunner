from backend.database import FirebaseManager

db = FirebaseManager.get_firestore()


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
