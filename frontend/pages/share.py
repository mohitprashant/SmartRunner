import pygame
from assets.components import *
from page import *


class SharePage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "share"
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

        #Include Room password Toggle
        #Need to change it to toggle
        roompassword_toggle_x = 9 / 20
        roompassword_toggle_y = 1 / 20
        roompassword_toggle_width = 1 / 10
        roompassword_toggle_height = 1 / 10
        roompassword_toggle_img = pygame.image.load('assets/img/start_btn.png')
        roompassword_toggle = ImageButton("roompassword", screen, roompassword_toggle_x, roompassword_toggle_y,
                                         roompassword_toggle_width,
                                         roompassword_toggle_height, roompassword_toggle_img)
        self.components["roompassword"] = roompassword_toggle

        # Room Password display
        diplay_roompassword_display_x = 1 / 20
        diplay_roompassword_display_y = 3 / 40
        diplay_roompassword_display_width = 1 / 3
        diplay_roompassword_display_height = 1 / 3
        diplay_roompassword_text = "Include Room Password"
        diplay_roompassword_display = TextDisplay("diplay_roompassword_display", screen, diplay_roompassword_display_x,
                                             diplay_roompassword_display_y, diplay_roompassword_display_width,
                                             diplay_roompassword_display_height, diplay_roompassword_text)
        self.components["diplay_roompassword_display"] = diplay_roompassword_display

        # Twitter Button
        twitter_button_x = 3 / 20
        twitter_button_y = 1 / 4
        twitter_button_width = 1 / 4
        twitter_button_height = 1 / 8
        twitter_button_img = pygame.image.load('assets/img/restart_btn.png')
        twitter_button = ImageButton("twitter_button", screen, twitter_button_x, twitter_button_y,
                                         twitter_button_width,
                                         twitter_button_height, twitter_button_img)
        self.components["twitter_button"] = twitter_button

        # IG Button
        ig_button_x = 10 / 20
        ig_button_y = 1 / 4
        ig_button_width = 1 / 4
        ig_button_height = 1 / 8
        ig_button_img = pygame.image.load('assets/img/restart_btn.png')
        ig_button = ImageButton("ig_button", screen, ig_button_x, ig_button_y,
                                     ig_button_width,
                                     ig_button_height, ig_button_img)
        self.components["ig_button"] = ig_button


        # whatsapp Button
        whatsapp_button_x = 3 / 20
        whatsapp_button_y = 2 / 4
        whatsapp_button_width = 1 / 4
        whatsapp_button_height = 1 / 8
        whatsapp_button_img = pygame.image.load('assets/img/restart_btn.png')
        whatsapp_button = ImageButton("whatsapp_button", screen, whatsapp_button_x, whatsapp_button_y,
                                whatsapp_button_width,
                                whatsapp_button_height, whatsapp_button_img)
        self.components["whatsapp_button"] = whatsapp_button

        # Telegram Button
        telegram_button_x = 10 / 20
        telegram_button_y = 2 / 4
        telegram_button_width = 1 / 4
        telegram_button_height = 1 / 8
        telegram_button_img = pygame.image.load('assets/img/restart_btn.png')
        telegram_button = ImageButton("telegram_button", screen, telegram_button_x, telegram_button_y,
                                      telegram_button_width,
                                      telegram_button_height, telegram_button_img)
        self.components["telegram_button"] = telegram_button

        # return button
        return_button_x = 17 / 20
        return_button_y = 17 / 20
        return_button_width = 1 / 10
        return_button_height = 1 / 10
        return_button__img = pygame.image.load('assets/img/exit_btn.png')
        return_button = ImageButton("return_button", screen, return_button_x, return_button_y,
                                    return_button_width,
                                    return_button_height, return_button__img)
        self.components["return_button"] = return_button



        # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            if triggered_component in ["twitter_button", "ig_button", "whatsapp_button", "telegram_button","return_button"]:
                return self.data
            else:
                print("entry failed")

