import unittest
import sys
import pygame
import time
sys.path.insert(0, '../../')

from frontend.pages.create_account import CreateAccountPage
from frontend.pages.login import LoginPage


class TestFailureCreateAccountLogin(unittest.TestCase):
    def test_failure_create_account_login(self):
        pygame.init()
        screen = pygame.display.set_mode((720, 480), pygame.RESIZABLE)

        username = "IntegrationUser%s" % time.time()
        password = "123456"

        create_account_page = CreateAccountPage(screen)
        create_account_page.set_components(screen)
        create_account_page.components["username_input_box"].input = username
        create_account_page.components["password_input_box"].input = password
        create_account_page.components["password1_input_box"].input = password

        triggered_component_list = [create_account_page.components["create_acc_button"]]
        create_account_page.page_function(triggered_component_list)

        self.assertEqual(create_account_page.output_data["error_check"], True)

        login_page = LoginPage(screen)
        login_page.set_components(screen)
        login_page.components["username_input_box"].input = username
        login_page.components["password_input_box"].input = password

        triggered_component_list = [login_page.components["sign_in_button"]]
        login_page.page_function(triggered_component_list)

        self.assertEqual(login_page.output_data["error_check"], True)
