import pygame
from assets.components import *
from page import *


class EndScreenPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "end_screen"
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
        player_results_display_x = 1 / 4
        player_results_display_y = 1 / 4
        player_results_display_width = 1 / 2
        player_results_display_height = 1 / 4
        player_results_text ="Player 1: Score"
        player_results_display = TextDisplay("player_results_display", screen, player_results_display_x, player_results_display_y, player_results_display_width,
                              player_results_display_height,player_results_text)
        self.components["player_results_display"] = player_results_display


        # Share button
        share_button_x = 7 / 10
        share_button_y = 2 / 3
        share_button_width = 1 / 4
        share_button_height = 1 / 5
        share_button__img = pygame.image.load('assets/img/exit_btn.png')
        share_button = ImageButton("share_button", screen, share_button_x, share_button_y,
                             share_button_width,
                             share_button_height, share_button__img)
        self.components["share_button"] = share_button

    # how do the page react to events?
    #player score needs to be taken from backend
    #share button needs to link to share page
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            if triggered_component in ["player_score_display", "share_button"]:
                return self.data
            else:
                print("entry failed")
