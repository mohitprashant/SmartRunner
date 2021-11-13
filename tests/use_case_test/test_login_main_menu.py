import unittest
import sys
import pygame

sys.path.insert(0, '../../')

from frontend.pages.main_menu import MainMenuPage
from frontend.pages.login import LoginPage


class TestLoginMainMenu(unittest.TestCase):
    def test_login_main_menu(self):
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

        prev_page = "login"

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
