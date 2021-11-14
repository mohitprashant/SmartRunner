import pygame
import sys
import pathlib

sys.path.insert(0, '../../backend/database')
sys.path.insert(1, '../../frontend/pages')

from assets.components import *
from page import *

curr_dir = str(pathlib.Path(__file__).parent.resolve()) + '/'


class MainMenuPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "main_menu"
        self.input_data = {
            "back_navigation": "",
            "username": "",
            "prev_page": ""
        }
        self.output_data = {
            "back_navigation": "",
            "current_page": self.name,
            "prev_page": "",
            "username": "",
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        self.name = "main_menu"

        #change back navigation every time page changes
        if self.input_data["prev_page"] != self.name:
            self.output_data["back_navigation"] = self.input_data["prev_page"]

        # background
        bg_img = pygame.image.load(curr_dir + 'assets/Backgrounds/loginbg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        welcome_image_rel_x = 0.15
        welcome_image_rel_y = 0.02
        welcome_image_rel_width = 0.7
        welcome_image_rel_height = 0.4
        welcome_img = pygame.image.load('assets/Backgrounds/welcome.png')
        welcome_image = ImageDisplay("welcome_image", screen, welcome_image_rel_x, welcome_image_rel_y,
                                     welcome_image_rel_width, welcome_image_rel_height, welcome_img)
        self.components["welcome_image"] = welcome_image

        # Single Player button
        single_player_button_x = 1 / 20
        single_player_button_y = 0.4
        single_player_button_width = 1 / 4
        single_player_button_height = 1 / 5
        single_player_button_img = pygame.image.load(curr_dir + 'assets/Buttons/btn_singleplayer.png')
        single_player_button = ImageButton("single_player_button", screen, single_player_button_x,
                                           single_player_button_y, single_player_button_width,
                                           single_player_button_height, single_player_button_img)
        self.components["single_player_button"] = single_player_button

        # Room button
        room_button_x = 15 / 40
        room_button_y = 0.4
        room_button_width = 1 / 4
        room_button_height = 1 / 5
        room_button__img = pygame.image.load(curr_dir + 'assets/Buttons/btn_rooms.png')
        room_button = ImageButton("room_button",screen, room_button_x, room_button_y,
                                  room_button_width, room_button_height, room_button__img)
        self.components["room_button"] = room_button

        # Leaderboard button
        leaderboard_button_x = 7 / 10
        leaderboard_button_y = 0.4
        leaderboard_button_width = 1 / 4
        leaderboard_button_height = 1 / 5
        leaderboard_button__img = pygame.image.load(curr_dir + 'assets/Buttons/btn_leaderboards.png')
        leaderboard_button = ImageButton("leaderboard_button", screen, leaderboard_button_x, leaderboard_button_y,
                                         leaderboard_button_width, leaderboard_button_height, leaderboard_button__img)
        self.components["leaderboard_button"] = leaderboard_button

        exit_button_rel_x = 1 / 15
        exit_button_rel_y = 4 / 5
        exit_button_rel_width = 1 / 7
        exit_button_rel_height = 1 / 7
        exit_button_img = pygame.image.load(curr_dir + 'assets/Buttons/btn_back.png')
        exit_button = ImageButton("exit_button", screen, exit_button_rel_x, exit_button_rel_y,
                                  exit_button_rel_width, exit_button_rel_height, exit_button_img)
        self.components["exit_button"] = exit_button

        avatar_button_rel_x = 12 / 15
        avatar_button_rel_y = 0.8
        avatar_button_rel_width = 0.1
        avatar_button_rel_height = 1/7
        avatar_button_img = pygame.image.load(curr_dir + 'assets/Buttons/btn_avatar.png')
        avatar_button = ImageButton("exit_button", screen, avatar_button_rel_x, avatar_button_rel_y,
                                    avatar_button_rel_width, avatar_button_rel_height, avatar_button_img)
        self.components["avatar_button"] = avatar_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["username"] = self.input_data["username"]
            self.output_data["subject_topic_list"] = ["Select Topic"]
            self.output_data["subjectselection"] = "Select Subject"
            self.output_data["topicselection"] = "Select Topic"
            self.output_data["difficultylist"] = ["Select Difficulty"]
            self.output_data["difficultyselection"] = "Select Difficulty"
            self.output_data["join_host"] = False
            self.output_data["roomID"] = "singleplayer"
            self.output_data["playertype"] = "singleplayer"

            if triggered_component in [self.components["exit_button"]]:
                self.name = "login"

            if triggered_component in [self.components["single_player_button"]]:
                self.name = "singleplayer"
            elif triggered_component in [self.components["room_button"]]:
                self.name = "room_tab"
            elif triggered_component in [self.components["leaderboard_button"]]:
                self.name = "leadselect"
            elif triggered_component in [self.components["avatar_button"]]:
                self.name = "customize"
            else:
                print("entry failed")
