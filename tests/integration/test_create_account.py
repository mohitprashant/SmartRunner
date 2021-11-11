import unittest
import sys
import pygame
import time
sys.path.insert(1, '../../')

from frontend.pages.create_account import CreateAccountPage


class TestCreateAccount(unittest.TestCase):
    def test_create_account(self):
        pygame.init()
        screen = pygame.display.set_mode((720, 480), pygame.RESIZABLE)

        username = "IntegrationUser%s@mail.com" % time.time()
        password = "123456"

        create_account_page = CreateAccountPage(screen)
        create_account_page.set_components(screen)
        create_account_page.components["username_input_box"].input = username
        create_account_page.components["password_input_box"].input = password
        create_account_page.components["password1_input_box"].input = password

        triggered_component_list = [create_account_page.components["create_acc_button"]]
        create_account_page.page_function(triggered_component_list)

        self.assertListEqual([username, password],
                             [create_account_page.output_data['username'], create_account_page.output_data['password']])
