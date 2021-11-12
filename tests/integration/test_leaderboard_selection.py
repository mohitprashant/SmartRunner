import unittest
import sys
import pygame

sys.path.insert(1, '../../')

from frontend.pages.leaderboardselection import LeadSelectPage


class TestTopicLeaderboard(unittest.TestCase):
    def test_room_creation(self):
        pygame.init()
        screen = pygame.display.set_mode((720, 480), pygame.RESIZABLE)

        prev_page = "topic_leaderboard"
        leaderboardlist = ["Test1", "Test2"]
        username = "integrationUser1@mail.com"

        leaderboard_selection_page = LeadSelectPage(screen)

        leaderboard_selection_page.input_data["prev_page"] = prev_page
        leaderboard_selection_page.input_data["leaderboardlist"] = leaderboardlist
        leaderboard_selection_page.input_data["username"] = username

        leaderboard_selection_page.set_components(screen)

        triggered_component_list = [leaderboard_selection_page.components["exit_button"], leaderboard_selection_page.components["textbox_button_list"]]
        leaderboard_selection_page.page_function(triggered_component_list)

        self.assertTrue(leaderboard_selection_page.output_data["current_page"], "topic_leaderboard")
        self.assertTrue(leaderboard_selection_page.output_data["prev_page"], prev_page)
