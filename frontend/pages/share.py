import pygame
import sys
import pathlib

sys.path.insert(0, '../../backend/database')
sys.path.insert(1, '../../frontend/pages')

from assets.components import *
from page import *
import webbrowser
import facebook as fb

curr_dir = str(pathlib.Path(__file__).parent.resolve()) + '/'


class SharePage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "share"
        self.input_data = {
            "roomID": "RoomID",
            "room_password": "",
            "username": "username",
            "back_navigation": "",
        }
        self.output_data = {
            "current_page": self.name,
            "room_ID": "",
            "room_password": "",
            "username": "",
            "prev_page": "",
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        self.name = "share"

        # change back navigation every time page changes
        if self.input_data["prev_page"] != self.name:
            self.output_data["back_navigation"] = self.input_data["prev_page"]

        # background
        bg_img = pygame.image.load(curr_dir + 'assets/Backgrounds/sharebg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # Twitter Button
        twitter_button_x = 3 / 20
        twitter_button_y = 0.4
        twitter_button_width = 1 / 4
        twitter_button_height = 0.30
        twitter_button_img = pygame.image.load(curr_dir + 'assets/Buttons/btn_twitter.png')
        twitter_button = ImageButton("twitter_button", screen, twitter_button_x, twitter_button_y,
                                     twitter_button_width, twitter_button_height, twitter_button_img)
        self.components["twitter_button"] = twitter_button

        # Facebook Button
        facebook_button_x = 10 / 20
        facebook_button_y = 0.4
        facebook_button_width = 1 / 4
        facebook_button_height = 0.3
        facebook_button_img = pygame.image.load(curr_dir + 'assets/Buttons/btn_fb.png')
        facebook_button = ImageButton("facebook_button", screen, facebook_button_x, facebook_button_y,
                                      facebook_button_width, facebook_button_height, facebook_button_img)
        self.components["facebook_button"] = facebook_button

        # return button
        return_button_x = 17 / 20
        return_button_y = 17 / 20
        return_button_width = 1 / 10
        return_button_height = 1 / 10
        return_button__img = pygame.image.load(curr_dir + 'assets/Buttons/btn_back.png')
        return_button = ImageButton("return_button", screen, return_button_x, return_button_y,
                                    return_button_width, return_button_height, return_button__img)
        self.components["return_button"] = return_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["roomID"] = self.input_data["roomID"]
            message = "Join the SmartRun quiz now @\nRoom ID: " + self.output_data["roomID"]

            self.output_data["player_status"] = []
            self.output_data["mode_toggle"] = self.input_data["mode_toggle"]
            self.output_data["toggled"] = self.input_data["toggled"]
            self.output_data["custom_quiz_selection"] = self.input_data["custom_quiz_selection"]
            self.output_data["join_host"] = self.input_data["join_host"]

            self.output_data["username"] = self.input_data["username"]
            if triggered_component in [self.components["twitter_button"]]:
                url = "https://twitter.com/intent/tweet?text=" + message
                webbrowser.open(url)
            if triggered_component in [self.components["facebook_button"]]:
                fb_access_token = 'EAAZAZBaaDDFy8BAF5z4aE5CSpObkXcZBppVfZBknWNfAdxe1evTfZA0gM0dBFHEzcIQKxqYdKOXab06ZAosuCzhSP49tkZAMmB4TDstS8lXoqIPN1bBzXK2KmGUsjhBKJpCIAlprZBoq5sVgfTChW3laanfxSq5ZCyntOCjbW46cymK8agiFvvmNbeeZCu7n6gLGqTBrS6zoPIiLZAD5ugECL6n'
                fb_api = fb.GraphAPI(fb_access_token)
                fb_api.put_object('me', 'feed', message=message)
                url = 'https://www.facebook.com/SmartRun-Leaderboard-104831658686019/'
                webbrowser.open(url)
            if triggered_component in [self.components["return_button"]]:
                self.output_data["roomID"] = self.input_data["roomID"]
                self.name = self.output_data["back_navigation"]
