import pygame
import sys
import pathlib

sys.path.insert(0, '../../backend/database')
sys.path.insert(1, '../../frontend/pages')

from assets.components import *
from page import *

curr_dir = str(pathlib.Path(__file__).parent.resolve()) + '/'


class SharePage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "share"
        self.input_data = {
            "roomID": "RoomID",
            "room_password": "",
            "username":"username",
            "back_navigation":"",
        }
        self.output_data = {
            "room_ID": "",
            "room_password": "",
            "username":"",
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

        # # toggle test
        # toggle_rel_x = 9 / 20
        # toggle_rel_y = 1 / 20
        # toggle_rel_width = 1 / 10
        # toggle_rel_height = 1 / 10
        # toggle_image = pygame.image.load('assets/Buttons/btn_togglenotpressed.png')
        # toggle_image2 = pygame.image.load('assets/Buttons/btn_togglepressed.png')
        # # print("toggled image", self.input_data["toggled"])
        # toggle_pw = ToggleButton("toggle_pw", screen, toggle_rel_x, toggle_rel_y, toggle_rel_width, toggle_rel_height,
        #                       toggle_image, toggle_image2, self.input_data["toggled"])
        # self.components["toggle_pw"] = toggle_pw

        # toggle test
        # toggle_rel_x = 9 / 20
        # toggle_rel_y = 1 / 20
        # toggle_rel_width = 1 / 10
        # toggle_rel_height = 1 / 10
        # toggle_image = pygame.image.load('assets/img/save_btn.png')
        # toggle_image2 = pygame.image.load('assets/img/load_btn.png')
        # toggle_password = ToggleButton("toggle", screen, toggle_rel_x, toggle_rel_y, toggle_rel_width, toggle_rel_height,
        #                       toggle_image, toggle_image2)
        # self.components["toggle"] = toggle_password

        #Include Room password Toggle
        #Need to change it to toggle
        # roompassword_toggle_x = 9 / 20
        # roompassword_toggle_y = 1 / 20
        # roompassword_toggle_width = 1 / 10
        # roompassword_toggle_height = 1 / 10
        # roompassword_toggle_img = pygame.image.load('assets/img/start_btn.png')
        # roompassword_toggle = ImageButton("roompassword", screen, roompassword_toggle_x, roompassword_toggle_y,
        #                                  roompassword_toggle_width,
        #                                  roompassword_toggle_height, roompassword_toggle_img)
        # self.components["roompassword"] = roompassword_toggle

        # # Room Password display
        # display_roompassword_display_x = 0.08
        # display_roompassword_display_y = 0.04
        # display_roompassword_display_width = 1 / 3
        # display_roompassword_display_height = 1 / 6
        # display_roompassword_text = pygame.image.load('assets/Backgrounds/includepwd.png')
        # display_roompassword_display = ImageDisplay("display_roompassword_display", screen, display_roompassword_display_x,
        #                                      display_roompassword_display_y, display_roompassword_display_width,
        #                                      display_roompassword_display_height, display_roompassword_text)
        # self.components["display_roompassword_display"] = display_roompassword_display

        # Twitter Button
        twitter_button_x = 3 / 20
        twitter_button_y = 0.4
        twitter_button_width = 1 / 4
        twitter_button_height = 0.30
        twitter_button_img = pygame.image.load(curr_dir + 'assets/Buttons/btn_twitter.png')
        twitter_button = ImageButton("twitter_button", screen, twitter_button_x, twitter_button_y,
                                         twitter_button_width,
                                         twitter_button_height, twitter_button_img)
        self.components["twitter_button"] = twitter_button

        # # IG Button
        # ig_button_x = 10 / 20
        # ig_button_y = 1 / 4
        # ig_button_width = 0.18
        # ig_button_height = 1 / 5
        # ig_button_img = pygame.image.load('assets/img/Instagram.png')
        # ig_button = ImageButton("ig_button", screen, ig_button_x, ig_button_y,
        #                              ig_button_width,
        #                              ig_button_height, ig_button_img)
        # self.components["ig_button"] = ig_button


        # whatsapp Button
        # whatsapp_button_x = 3 / 20
        # whatsapp_button_y = 2 / 4
        # whatsapp_button_width = 1 / 4
        # whatsapp_button_height = 1 / 4
        # whatsapp_button_img = pygame.image.load('assets/img/whatsapp.png')
        # whatsapp_button = ImageButton("whatsapp_button", screen, whatsapp_button_x, whatsapp_button_y,
        #                         whatsapp_button_width,
        #                         whatsapp_button_height, whatsapp_button_img)
        # self.components["whatsapp_button"] = whatsapp_button

        # Facebook Button
        facebook_button_x = 10 / 20
        facebook_button_y = 0.4
        facebook_button_width = 1 / 4
        facebook_button_height = 0.3
        facebook_button_img = pygame.image.load(curr_dir + 'assets/Buttons/btn_fb.png')
        facebook_button = ImageButton("facebook_button", screen, facebook_button_x, facebook_button_y,
                                      facebook_button_width,
                                      facebook_button_height, facebook_button_img)
        self.components["facebook_button"] = facebook_button

        # return button
        return_button_x = 17 / 20
        return_button_y = 17 / 20
        return_button_width = 1 / 10
        return_button_height = 1 / 10
        return_button__img = pygame.image.load(curr_dir + 'assets/Buttons/btn_back.png')
        return_button = ImageButton("return_button", screen, return_button_x, return_button_y,
                                    return_button_width,
                                    return_button_height, return_button__img)
        self.components["return_button"] = return_button



        # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["roomID"] = self.input_data["roomID"]
            self.output_data["player_status"] = []

            print(self.output_data["room_ID"])
            # self.output_data["room_password"] = self.input_data["room_password"]
            self.output_data["username"] = self.input_data["username"]
            if triggered_component in [self.components["twitter_button"]]:
                print("open twitter")
            if triggered_component in [self.components["facebook_button"]]:
                print("open facebook")
            if triggered_component in [self.components["return_button"]]:
                self.output_data["roomID"] = self.input_data["roomID"]
                self.name = self.output_data["back_navigation"]
                #if statement if returned data is very different (refer to share_results)
            # if triggered_component in [self.components["toggle_pw"]]:
            #     print("hello")
            #     if triggered_component.toggled:
            #         # self.output_data["toggle_password"] = True
            #         self.input_data["toggled"] = True
            #         print("Include room password")
            #     else:
            #         self.input_data["toggled"] = False
            #         print("False")


