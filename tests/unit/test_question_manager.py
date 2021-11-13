import unittest

from backend.database import QuestionManager


class TestSubjects(unittest.TestCase):
    def test_get_subjects(self):
        num_subjects = 5
        valid_subjects = ['Biology', 'Chemistry', 'Economics', 'Mathematics', 'Physics']
        subjects = QuestionManager.get_subjects()
        # check number of Math topics
        self.assertEqual(num_subjects, len(subjects))
        # check all topic names
        for i in range(0, 5):
            self.assertEqual(valid_subjects[i], subjects[i])


class TestTopics(unittest.TestCase):
    def test_get_math_topics(self):
        num_math_topics = 5
        valid_topics = ['Algebra', 'Calculus', 'Geometry', 'Numbers', 'Statistics']
        topics = QuestionManager.get_topics('Mathematics')
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
        self.assertEqual(num_math_questions, len(QuestionManager.get_questions(topic, 'Algebra')))
        # check number of Calculus questions
        self.assertEqual(num_math_questions, len(QuestionManager.get_questions(topic, 'Calculus')))
        # check number of Calculus questions
        self.assertEqual(num_math_questions, len(QuestionManager.get_questions(topic, 'Geometry')))
        # check number of Numbers questions
        self.assertEqual(num_math_questions, len(QuestionManager.get_questions(topic, 'Numbers')))
        # check number of Statistics questions
        self.assertEqual(num_math_questions, len(QuestionManager.get_questions(topic, 'Statistics')))

    def test_get_math_algebra_questions(self):
        questions = QuestionManager.get_questions('Mathematics', 'Algebra')
        question = questions[0]
        description = '(0.84)^2 × (0.41)'
        difficulty_level = 1
        correct = '0.2893'
        wrong_1 = '3.444'
        wrong_2 = '2.893'
        wrong_3 = '0.3444'
        self.assertEqual(description, question['Description'])
        self.assertEqual(difficulty_level, question['Difficulty_level'])
        self.assertEqual(correct, question['Correct'])
        self.assertEqual(wrong_1, question['Wrong_1'])
        self.assertEqual(wrong_2, question['Wrong_2'])
        self.assertEqual(wrong_3, question['Wrong_3'])

    def test_get_questions_by_difficulty(self):
        difficulty_level = 3
        questions = QuestionManager.get_questions_by_difficulty('Mathematics', 'Calculus', difficulty_level)
        for question in questions:
            self.assertEqual(question['Difficulty_level'], difficulty_level)

    def test_get_question_difficulty_list(self):
        test_difficulty_list = [1, 2, 3, 4, 5]
        difficulty_list = QuestionManager.get_question_difficulty_list('Mathematics', 'Geometry')
        self.assertListEqual(test_difficulty_list, difficulty_list)
