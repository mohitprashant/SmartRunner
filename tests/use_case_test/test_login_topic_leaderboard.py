import unittest
import sys
import pygame

sys.path.insert(0, '../../')

from frontend.pages.topic_leaderboard import TopicLeaderboardPage
from frontend.pages.login import LoginPage


class TestLoginTopicLeaderboard(unittest.TestCase):
    def test_login_topic_leaderboard(self):
        pygame.init()
        screen = pygame.display.set_mode((720, 480), pygame.RESIZABLE)

        username = "example@mail.com"
        password = "123456"

        login_page = LoginPage(screen)
        login_page.set_components(screen)
        login_page.components["username_input_box"].input = username
        login_page.components["password_input_box"].input = password

        triggered_component_list = [login_page.components["sign_in_button"]]
        login_page.page_function(triggered_component_list)

        self.assertEqual("main_menu", login_page.name)

        prev_page = "main_menu"
        subject = "test_subject"
        topic = "test_topic"
        topic_leaderboard = ["test"]

        topic_leaderboard_page = TopicLeaderboardPage(screen)

        topic_leaderboard_page.input_data["prev_page"] = prev_page
        topic_leaderboard_page.input_data["subject"] = subject
        topic_leaderboard_page.input_data["topic"] = topic
        topic_leaderboard_page.input_data["topic_leaderboard"] = topic_leaderboard
        topic_leaderboard_page.input_data["username"] = username

        topic_leaderboard_page.set_components(screen)

        triggered_component_list = [topic_leaderboard_page.components["share_button"], topic_leaderboard_page.components["return_button"]]
        topic_leaderboard_page.page_function(triggered_component_list)

        self.assertTrue(topic_leaderboard_page.output_data["prev_page"], prev_page)
        self.assertTrue(topic_leaderboard_page.output_data["subject"], subject)
        self.assertTrue(topic_leaderboard_page.output_data["topic"], topic)
        self.assertTrue(topic_leaderboard_page.output_data["topic_leaderboard"], topic_leaderboard)
        self.assertTrue(topic_leaderboard_page.output_data["username"], username)
