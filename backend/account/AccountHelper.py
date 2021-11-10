from backend.database import FirebaseManager

db = FirebaseManager.get_firestore()


def add_to_user_collection(username):
    """
    Returns a user dictionary object if given username exists
    """
    if type(username) is not str:
        raise Exception("Given arguments is not of type str")

    user = {
        'username': username,
        'avatar': "",
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

