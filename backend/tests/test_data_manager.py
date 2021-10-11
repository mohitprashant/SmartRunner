import unittest
import uuid
import sys
import pathlib
import time

sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve()) + "/../..")
from backend.database import DatabaseManager
from backend.database import Enums

class TestSubjects(unittest.TestCase):
    def test_get_subjects(self):
        num_subjects = 5
        valid_subjects = ['Biology', 'Chemistry', 'Economics', 'Mathematics', 'Physics']
        subjects = DatabaseManager.get_subjects()
        # check number of Math topics
        self.assertEqual(num_subjects, len(subjects))
        # check all topic names
        for i in range(0, 5):
            self.assertEqual(valid_subjects[i], subjects[i])


class TestTopics(unittest.TestCase):
    def test_get_math_topics(self):
        num_math_topics = 5
        valid_topics = ['Algebra', 'Calculus', 'Geometry', 'Numbers', 'Statistics']
        topics = DatabaseManager.get_topics('Mathematics')
        # check number of Math topics
        self.assertEqual(num_math_topics, len(topics))
        # check all topic names
        for i in range(0, 5):
            self.assertEqual(valid_topics[i], topics[i])


class TestQuestions(unittest.TestCase):
    def test_get_math_questions(self):
        num_math_questions = 25
        topic = 'Mathematics'
        # check number of Algebra questions
        self.assertEqual(num_math_questions, len(DatabaseManager.get_questions(topic, 'Algebra')))
        # check number of Calculus questions
        self.assertEqual(num_math_questions, len(DatabaseManager.get_questions(topic, 'Calculus')))
        # check number of Calculus questions
        self.assertEqual(num_math_questions, len(DatabaseManager.get_questions(topic, 'Geometry')))
        # check number of Numbers questions
        self.assertEqual(num_math_questions, len(DatabaseManager.get_questions(topic, 'Numbers')))
        # check number of Statistics questions
        self.assertEqual(num_math_questions, len(DatabaseManager.get_questions(topic, 'Statistics')))

    def test_get_math_algebra_questions(self):
        questions = DatabaseManager.get_questions('Mathematics', 'Algebra')
        question = questions[0]
        description = '（0.001）² ÷ 1000'
        difficulty_level = 3
        correct = 1e-09
        wrong_1 = 1000
        wrong_2 = 0.001
        wrong_3 = 1e-08
        self.assertEqual(description, question['Description'])
        self.assertEqual(difficulty_level, question['Difficulty_level'])
        self.assertEqual(correct, question['Correct'])
        self.assertEqual(wrong_1, question['Wrong_1'])
        self.assertEqual(wrong_2, question['Wrong_2'])
        self.assertEqual(wrong_3, question['Wrong_3'])

class TestLeaderboard(unittest.TestCase):
    def test_get_leaderboard(self):
        leaderboard = DatabaseManager.get_leaderboard('Mathematics', 'Algebra')
        self.assertLessEqual(len(leaderboard), Enums.leaderboardSize)
        self.assertGreaterEqual(len(leaderboard), 0)
        
        if len(leaderboard) > 0:
            curr = leaderboard[0]
            for i in range(1, len(leaderboard)):
                self.assertLessEqual(curr["score"], leaderboard[i]["score"])
                curr = leaderboard[i]

    def test_update_full_leaderboard_lower_score(self):
        # Inserting a score lower than the current lowest should not be successful
        subject = "Mathematics"
        topic = "Algebra"
        leaderboard = DatabaseManager.get_leaderboard(subject, topic)
        currLowest = leaderboard[0]

        otherUser = { "score": currLowest["score"] - 1, "uid": str(uuid.uuid4()), "epochTimeAdded": currLowest["epochTimeAdded"] }
        DatabaseManager.update_leaderboard(otherUser, subject, topic)
        updatedLeaderboard = DatabaseManager.get_leaderboard(subject, topic)
        self.assertEqual(currLowest, updatedLeaderboard[0])
        self.assertNotEqual(otherUser, updatedLeaderboard[0])

    def test_update_full_leaderboard_same_score(self):
        # Inserting a score equal to the current lowest should not be successful
        subject = "Mathematics"
        topic = "Algebra"
        leaderboard = DatabaseManager.get_leaderboard(subject, topic)
        currLowest = leaderboard[0]

        otherUser = { "score": currLowest["score"], "uid": str(uuid.uuid4()), "epochTimeAdded": time.time() }
        DatabaseManager.update_leaderboard(otherUser, subject, topic)
        updatedLeaderboard = DatabaseManager.get_leaderboard(subject, topic)
        self.assertEqual(currLowest, updatedLeaderboard[0])
        self.assertNotEqual(otherUser, updatedLeaderboard[0])

    def test_update_full_leaderboard_higher_score(self):
        # Inserting a score higher than the current lowest should be successful
        subject = "Mathematics"
        topic = "Algebra"
        leaderboard = DatabaseManager.get_leaderboard(subject, topic)
        currLowest = leaderboard[0]

        otherUser = { "score": currLowest["score"] + 1, "uid": str(uuid.uuid4()), "epochTimeAdded": currLowest["epochTimeAdded"] }
        DatabaseManager.update_leaderboard(otherUser, subject, topic)
        updatedLeaderboard = DatabaseManager.get_leaderboard(subject, topic)
        self.assertNotEqual(currLowest, updatedLeaderboard[0])
