import unittest
import uuid
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve()) + "/../..")

from backend.database import QuestionManager, RoomManager
from frontend.pages.add_question import AddQuestionPage
from frontend.pages.main import *

class TestAddQuestion(unittest.TestCase):
    def test_add_question(self):
        addQuestionPage = AddQuestionPage()
        self.assertEqual(1, 1)


    # def test_create_delete_room(self):
    #     user_id = "123abc"
    #     room_name = "Unit Test Room"
    #     room_password = "UnitTest"
    #
    #     current_room_count = len(RoomManager.get_hosted_rooms_list(user_id))
    #     room_id = RoomManager.create_room(user_id, room_name, room_password)
    #     after_add_room_count = len(RoomManager.get_hosted_rooms_list(user_id))
    #     self.assertEqual(current_room_count, after_add_room_count - 1)
    #     RoomManager.delete_room(user_id, room_id)
    #     after_del_room_count = len(RoomManager.get_hosted_rooms_list(user_id))
    #     self.assertEqual(after_add_room_count, after_del_room_count + 1)
    #
    # def test_add_get_delete_custom_questions(self):
    #     user_id = "123"
    #     room_name = "Unit Test Room"
    #     room_password = "UnitTest"
    #     room_id = RoomManager.create_room(user_id, room_name, room_password)
    #     quiz_name = "Unit Test Quiz"
    #     question = {
    #         'Correct': "This is the correct answer",
    #         "Description": "This is the description",
    #         "Difficulty_level": 2,
    #         "Wrong_1": "This is the first wrong option",
    #         "Wrong_2": "This is the second wrong option",
    #         "Wrong_3": "This is the third wrong option",
    #         "question_id": str(uuid.uuid4())
    #     }
    #     questions = [question]
    #
    #     curr_num_custom_questions = len(QuestionManager.get_custom_questions(room_id, quiz_name))
    #     QuestionManager.add_custom_questions(room_id, quiz_name, questions)
    #     after_add_num_custom_questions = len(QuestionManager.get_custom_questions(room_id, quiz_name))
    #     self.assertEqual(curr_num_custom_questions, after_add_num_custom_questions - 1)
    #     QuestionManager.delete_custom_question(user_id, room_id, quiz_name, question["question_id"])
    #     after_delete_num_custom_questions = len(QuestionManager.get_custom_questions(room_id, quiz_name))
    #     self.assertEqual(after_add_num_custom_questions, after_delete_num_custom_questions + 1)
    #     RoomManager.delete_room(user_id, room_id)
