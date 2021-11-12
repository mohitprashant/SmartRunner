import unittest
import sys
import pygame
import time

sys.path.insert(1, '../../')

from frontend.pages.room_creation import RoomCreationPage
from backend.database.RoomManager import room_id_exists, delete_room

class TestRoomCreation(unittest.TestCase):
    def test_room_creation(self):
        pygame.init()
        screen = pygame.display.set_mode((720, 480), pygame.RESIZABLE)

        username = "integrationUser1@mail.com"
        room_id = "Room %s" % time.time()
        prev_page = "room_tab"
        password = "123456"

        room_creation_page = RoomCreationPage(screen)

        room_creation_page.input_data["prev_page"] = prev_page
        room_creation_page.input_data["username"] = username

        room_creation_page.set_components(screen)

        room_creation_page.components["roomID_input_box"].input = room_id
        room_creation_page.components["password_input_box"].input = password

        triggered_component_list = [room_creation_page.components["room_confirm_button"]]
        room_creation_page.page_function(triggered_component_list)

        self.assertTrue(room_id_exists(room_creation_page.output_data["roomID"]))
        delete_room(username, room_creation_page.output_data["roomID"])
