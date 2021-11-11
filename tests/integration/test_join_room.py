import unittest
import sys
import pygame

sys.path.insert(1, '../../')

from frontend.pages.join_room import JoinRoomPage
from backend.database.RoomManager import remove_user_from_room, is_user_in_room

class TestJoinRoom(unittest.TestCase):
    def test_join_room(self):
        pygame.init()
        screen = pygame.display.set_mode((720, 480), pygame.RESIZABLE)

        username = "integrationUser1@mail.com"
        room_id = "123456"
        prev_page = "room_tab"
        password = "123456"

        if is_user_in_room(username, room_id):
            remove_user_from_room(username, username, room_id)

        join_room_page = JoinRoomPage(screen)

        join_room_page.input_data["prev_page"] = prev_page
        join_room_page.input_data["username"] = username

        join_room_page.set_components(screen)

        join_room_page.components["roomID_input_box"].input = room_id
        join_room_page.components["password_input_box"].input = password

        triggered_component_list = [join_room_page.components["room_confirm_button"]]
        join_room_page.page_function(triggered_component_list)

        self.assertTrue(is_user_in_room(username, room_id))
