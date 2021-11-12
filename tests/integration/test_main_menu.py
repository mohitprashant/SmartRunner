import unittest
import sys
import pygame
from frontend.pages.main_menu import MainMenuPage

sys.path.insert(1, '../../')


class TestMainMenu(unittest.TestCase):
    def test_room_creation(self):
        pygame.init()
        screen = pygame.display.set_mode((720, 480), pygame.RESIZABLE)

        prev_page = "login"
        username = "integrationUser1@mail.com"

        main_menu_page = MainMenuPage(screen)

        main_menu_page.input_data["prev_page"] = prev_page
        main_menu_page.input_data["username"] = username

        main_menu_page.set_components(screen)

        triggered_component_list = [main_menu_page.components["single_player_button"],
                                    main_menu_page.components["room_button"],
                                    main_menu_page.components["leaderboard_button"],
                                    main_menu_page.components["exit_button"]]

        main_menu_page.page_function(triggered_component_list)

        self.assertTrue(main_menu_page.output_data["username"] == username)
