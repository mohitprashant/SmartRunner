import unittest
import sys
import pygame

sys.path.insert(1, '../../')

from frontend.pages.topic_leaderboard import TopicLeaderboardPage


class TestTopicLeaderboard(unittest.TestCase):
    def test_room_creation(self):
        pygame.init()
        screen = pygame.display.set_mode((720, 480), pygame.RESIZABLE)

        prev_page = "main_menu"
        subject = "test_subject"
        topic = "test_topic"
        topic_leaderboard = ["test"]
        username = "integrationUser1@mail.com"

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
