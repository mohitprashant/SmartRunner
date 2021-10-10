import pygame
from assets.components import *
from page import *


class TopicLeaderboardPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "topic_leaderboard"
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

        # Player Score display
        player_score_display_x = 1 / 4
        player_score_display_y = 1 / 4
        player_score_display_width = 1 / 2
        player_score_display_height = 1 / 4
        player_score_text ="player score"
        player_score_display = TextDisplay("player_score_display", screen, player_score_display_x, player_score_display_y, player_score_display_width,
                              player_score_display_height,player_score_text)
        self.components["player_score_display"] = player_score_display


        #Share button
        share_button_x = 7 / 10
        share_button_y = 2 / 3
        share_button_width = 1 / 4
        share_button_height = 1 / 5
        share_button__img = pygame.image.load('assets/img/exit_btn.png')
        share_button = ImageButton("share_button", screen, share_button_x, share_button_y,
                             share_button_width,
                             share_button_height, share_button__img)
        self.components["share_button"] = share_button

        #return button
        return_button_x = 1 / 20
        return_button_y = 2 / 3
        return_button_width = 1 / 4
        return_button_height = 1 / 5
        return_button__img = pygame.image.load('assets/img/exit_btn.png')
        return_button = ImageButton("return_button", screen, return_button_x, return_button_y,
                                   return_button_width,
                                   return_button_height, return_button__img)
        self.components["return_button"] = return_button

    #how do the page react to events?
    #score display should retrieve data from backend
    #share and return button to link to other pages
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            if triggered_component in ["player_score_display", "share_button", "return_button"]:
                return self.data
            else:
                print("entry failed")
