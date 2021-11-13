import unittest
import sys
import pygame

sys.path.insert(1, '../../')

from frontend.pages.share import SharePage


class TestShare(unittest.TestCase):
    def test_share(self):
        pygame.init()
        screen = pygame.display.set_mode((720, 480), pygame.RESIZABLE)

        prev_page = "main_menu"
        roomID = "id123"
        room_password = "123"
        username = "integrationUser1@mail.com"

        share_page = SharePage(screen)

        share_page.input_data["prev_page"] = prev_page
        share_page.input_data["roomID"] = roomID
        share_page.input_data["room_password"] = room_password
        share_page.input_data["username"] = username

        share_page.set_components(screen)

        triggered_component_list = [share_page.components["twitter_button"], share_page.components["facebook_button"], share_page.components["return_button"]]
        share_page.page_function(triggered_component_list)

        self.assertTrue(share_page.output_data["prev_page"], prev_page)
        self.assertTrue(share_page.output_data["username"], username)
