import pygame
from assets.components import *
from page import *


class MainMenuPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "main_menu"
        self.data = {
            "current_page": self.name,
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/img/sky.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # Single Player button
        single_player_button_x = 1 / 20
        single_player_button_y = 1 / 2
        single_player_button_width = 1 / 4
        single_player_button_height = 1 / 5
        single_player_button_img = pygame.image.load('assets/img/start_btn.png')
        single_player_button = ImageButton("single_player_button", screen, single_player_button_x, single_player_button_y, single_player_button_width,
                              single_player_button_height, single_player_button_img)
        self.components["single_player_button"] = single_player_button

        # Room button
        room_button_x = 15 / 40
        room_button_y = 1 / 2
        room_button_width = 1 / 4
        room_button_height = 1 / 5
        room_button__img = pygame.image.load('assets/img/restart_btn.png')
        room_button = ImageButton("room_button",screen, room_button_x, room_button_y,
                                      room_button_width,
                                      room_button_height, room_button__img)
        self.components["room_button"] = room_button

        # Room button
        leaderboard_button_x = 7 / 10
        leaderboard_button_y = 1 / 2
        leaderboard_button_width = 1 / 4
        leaderboard_button_height = 1 / 5
        leaderboard_button__img = pygame.image.load('assets/img/load_btn.png')
        leaderboard_button = ImageButton("leaderboard_button", screen, leaderboard_button_x, leaderboard_button_y,
                             leaderboard_button_width,
                             leaderboard_button_height, leaderboard_button__img)
        self.components["leaderboard_button"] = leaderboard_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            if triggered_component in ["single_player_button", "room_button", "leaderboard_button"]:
                return self.data
            else:
                print("entry failed")
