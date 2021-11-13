import random
from backend.database import FirebaseManager
from backend.database import Enums
from backend.database.DatabaseManager import check_fields
from backend.database.RoomManager import room_id_exists, is_room_host, get_room_quizzes_list

db = FirebaseManager.get_firestore()


def get_subjects():
    """
        Returns a list of available subjects.
    """
    subjects = db.collection('subjects').list_documents()
    items = []

    for subject in subjects:
        items.append(subject.id)

    return items


def get_topics(subject):
    """
        Returns a list of available topics for a given subject.
    """
    topics = db.collection('subjects').document(subject).collections()
    items = []

    for topic in topics:
        items.append(topic.id)

    return items


def get_questions_by_difficulty(subject, topic, difficulty_level, randomise=False):
    if type(subject) is not str or type(topic) is not str:
        raise Exception("Given arguments are not of type str")

    if type(difficulty_level) is not int:
        raise Exception("Given argument is not of type int")

    if subject == "" or topic == "":
        raise Exception("Given arguments cannot be empty")

    query = db.collection("subjects")\
            .document(subject)\
            .collection(topic)\
            .where("Difficulty_level", "==", difficulty_level)\
            .get()

    questions = []
    for question in query:
        questions.append(question.to_dict())

    if randomise is False:
        return questions
    randomised_questions = randomise_questions(questions)
    return randomised_questions


def get_questions(subject, topic, room_id="", quiz_name="", randomise=False):
    """
    Returns an array of questions from the subject and topic.
    Each question is of a dictionary type.
    Array of questions will be randomised if randomise argument is set to True
    """
    query = db.collection("subjects").document(subject).collection(topic).get()
    questions = []

    for question in query:
        questions.append(question.to_dict())

    if room_id != "":
        if quiz_name == "":
            raise Exception("Quiz name is missing")

        custom_questions = get_custom_questions(room_id, quiz_name)
        for custom_question in custom_questions:
            questions.append(custom_question.to_dict())

    if randomise is False:
        return questions

    # This randomises the questions to prevent the same questions from being selected each time
    randomised_questions = randomise_questions(questions)
    return randomised_questions


def get_custom_questions(room_id, quiz_name):
    """
    :param room_id: 6 digit ID of room
    :param quiz_name: Quiz name of quiz to retrieve questions from
    :return:
    """
    if type(room_id) is not str or type(quiz_name) is not str:
        raise Exception("Given arguments are not of type str")

    if room_id == "" or quiz_name == "":
        raise Exception("Given arguments cannot be empty")

    query = db.collection("rooms")\
                            .document(room_id)\
                            .collection("quizzes")\
                            .document(quiz_name)\
                            .collection("questions")\
                            .get()
    questions = []
    for question in query:
        questions.append(question.to_dict())

    return questions


def add_custom_questions(room_id, quiz_name, questions):
    """
    Adds the given list of custom questions to the room_id
    :param room_id: Room ID of the room that the questions are to be added in
    :param quiz_name: Quiz name of the room that the questions are to be added in
    :param questions: List of questions to be added
    :return:
    """
    if type(room_id) is not str or type(quiz_name) is not str:
        raise Exception("Given arguments are not of type str")

    if room_id == "" or quiz_name == "":
        raise Exception("Given arguments cannot be empty")

    if type(questions) is not list:
        raise Exception("Given question object is not a list")

    # Must check entire list before adding to database, or there will be duplicate additions
    for question in questions:
        check_fields(question, Enums.question_fields)

    # check if quiz exists, if not, create it
    room_quizzes_list = get_room_quizzes_list(room_id)
    if quiz_name not in room_quizzes_list:
        db.collection("rooms").document(room_id)\
            .collection("quizzes").document(quiz_name).set({'room_id': room_id})

    for question in questions:
        db.collection("rooms").document(room_id)\
            .collection("quizzes").document(quiz_name)\
            .collection("questions").document().set(question)


def add_global_questions(subject, topic, questions):
    """
    :param subject: Subject required
    :param topic: Topic required
    :param questions: List of questions to be added to the global question bank
    :return:     Add a question to the specified subject and topic
    Throws an exception if the given question is not a dictionary type or does not have the specified keys
    """
    # Must check entire list before adding to database, or there will be duplicate additions
    for question in questions:
        check_fields(question, Enums.question_fields)

    for question in questions:
        db.collection("subjects").document(subject).collection(topic).document().set(question)

    return question


def delete_custom_question(user_id, room_id, quiz_name, question_id):
    """
    :param user_id: User ID of the host
    :param room_id: Room ID of the question to be deleted
    :param quiz_name: Quiz name of the question to be deleted
    :param question_id: Question ID of the question to be deleted
    :return: Deletes a custom question entry
    """
    if type(user_id) is not str or type(room_id) is not str or type(quiz_name) is not str or type(question_id) is not str:
        raise Exception("Given arguments are not of type str")

    if user_id == "" or room_id == "" or quiz_name == "" or question_id == "":
        raise Exception("Given arguments cannot be empty")

    if room_id_exists(room_id) is False or is_room_host(user_id, room_id) is False:
        return False

    query = db.collection("rooms").document(room_id).collection("quizzes").document(quiz_name).collection("questions").\
        where("question_id", "==", question_id)\
        .get()

    if len(query) == 0:
        return False

    question = query[0]

    db.collection("rooms").document(room_id).collection("quizzes").document(quiz_name).collection("questions")\
        .document(question.id).delete()

    return True


def randomise_questions(questions_arr):
    num_questions = len(questions_arr)
    randomised_questions_arr = []
    samples = random.sample(range(num_questions), num_questions)
    for sample in samples:
        randomised_questions_arr.append(questions_arr[sample])

    return randomised_questions_arr


def get_question_difficulty_list(subject, topic):
    """
    :param subject: Subject required
    :param topic: Topic required
    :return: Integer list of difficulties available in the Subject and Topic, in ascending order
    """
    query = db.collection("subjects").document(subject).collection(topic).get()
    difficulties = []

    for question in query:
        difficulty = (question.to_dict()["Difficulty_level"])
        if difficulty not in difficulties:
            difficulties.append(difficulty)

    difficulties.sort()
    return difficulties
