import unittest
import sys
import pygame
sys.path.insert(0, '../../')

from frontend.pages.room_creation import RoomCreationPage
from frontend.pages.login import LoginPage
from backend.database.RoomManager import room_id_exists, delete_room

class TestLoginCreateRoom(unittest.TestCase):
    def test_login_create_room(self):
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

        prev_page = "room_tab"
        password = "123456"
        room_name = "Integration test room"

        room_creation_page = RoomCreationPage(screen)

        room_creation_page.input_data["prev_page"] = prev_page
        room_creation_page.input_data["username"] = username

        room_creation_page.set_components(screen)

        room_creation_page.components["roomID_input_box"].input = room_name
        room_creation_page.components["password_input_box"].input = password

        triggered_component_list = [room_creation_page.components["room_confirm_button"]]
        room_creation_page.page_function(triggered_component_list)

        self.assertTrue(room_id_exists(room_creation_page.output_data["roomID"]))
        delete_room(username, room_creation_page.output_data["roomID"])
