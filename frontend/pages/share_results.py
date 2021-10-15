import pygame
from assets.components import *
from page import *


class ShareResultsPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "share_results"
        self.input_data = {
            "roomID": "RoomID",
            "username": "username",
            "score_board": []
        }
        self.output_data = {
            "room_ID": "",
            "prev_page": "",
            "score_board": "",
            "username": "",
            "exit": False
        }

        # set all component variables on input screen

    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/img/sky.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # # toggle test
        # toggle_rel_x = 9 / 20
        # toggle_rel_y = 1 / 20
        # toggle_rel_width = 1 / 10
        # toggle_rel_height = 1 / 10
        # toggle_image = pygame.image.load('assets/img/save_btn.png')
        # toggle_image2 = pygame.image.load('assets/img/load_btn.png')
        # toggle_password = ToggleButton("toggle", screen, toggle_rel_x, toggle_rel_y, toggle_rel_width, toggle_rel_height,
        #                       toggle_image, toggle_image2)
        # self.components["toggle"] = toggle_password


        # Room Password display
        diplay_roompassword_display_x = 4 / 20
        diplay_roompassword_display_y = 3 / 40
        diplay_roompassword_display_width = 1 / 2
        diplay_roompassword_display_height = 0.9
        diplay_roompassword_text = "Share results to social media"
        diplay_roompassword_display = TextDisplay("diplay_roompassword_display", screen, diplay_roompassword_display_x,
                                             diplay_roompassword_display_y, diplay_roompassword_display_width,
                                             diplay_roompassword_display_height, diplay_roompassword_text)
        self.components["diplay_roompassword_display"] = diplay_roompassword_display

        # Twitter Button
        twitter_button_x = 3 / 20
        twitter_button_y = 0.23
        twitter_button_width = 1 / 4
        twitter_button_height = 0.30
        twitter_button_img = pygame.image.load('assets/img/twitter.png')
        twitter_button2 = ImageButton("twitter_button", screen, twitter_button_x, twitter_button_y,
                                         twitter_button_width,
                                         twitter_button_height, twitter_button_img)
        self.components["twitter_button"] = twitter_button2

        # IG Button
        ig_button_x = 10 / 20
        ig_button_y = 1 / 4
        ig_button_width = 0.18
        ig_button_height = 1 / 5
        ig_button_img = pygame.image.load('assets/img/Instagram.png')
        ig_button2 = ImageButton("ig_button", screen, ig_button_x, ig_button_y,
                                     ig_button_width,
                                     ig_button_height, ig_button_img)
        self.components["ig_button"] = ig_button2


        # whatsapp Button
        whatsapp_button_x = 3 / 20
        whatsapp_button_y = 2 / 4
        whatsapp_button_width = 1 / 4
        whatsapp_button_height = 1 / 4
        whatsapp_button_img = pygame.image.load('assets/img/whatsapp.png')
        whatsapp_button2 = ImageButton("whatsapp_button", screen, whatsapp_button_x, whatsapp_button_y,
                                whatsapp_button_width,
                                whatsapp_button_height, whatsapp_button_img)
        self.components["whatsapp_button"] = whatsapp_button2

        # Telegram Button
        telegram_button_x = 8.5 / 20
        telegram_button_y = 2 / 4
        telegram_button_width = 1 / 3
        telegram_button_height = 1 / 4
        telegram_button_img = pygame.image.load('assets/img/telegram.png')
        telegram_button2 = ImageButton("telegram_button", screen, telegram_button_x, telegram_button_y,
                                      telegram_button_width,
                                      telegram_button_height, telegram_button_img)
        self.components["telegram_button"] = telegram_button2

        # return button
        return_button_x = 17 / 20
        return_button_y = 17 / 20
        return_button_width = 1 / 10
        return_button_height = 1 / 10
        return_button__img = pygame.image.load('assets/img/exit_btn.png')
        return_button2 = ImageButton("return_button", screen, return_button_x, return_button_y,
                                    return_button_width,
                                    return_button_height, return_button__img)
        self.components["return_button"] = return_button2



        # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["roomID"] = self.input_data["roomID"]
            self.output_data["score_board"] = self.input_data["score_board"]
            self.output_data["username"] = self.input_data["username"]
            self.output_data["prev_page"] = self.name
            if triggered_component in [self.components["twitter_button"]]:
                print("open twitter")
            if triggered_component in [self.components["ig_button"]]:
                print("open instagram")
            if triggered_component in [self.components["whatsapp_button"]]:
                print("open whatsapp")
            if triggered_component in [self.components["telegram_button"]]:
                print("open telegram")
            if triggered_component in [self.components["return_button"]]:
                print("go back to game session")



