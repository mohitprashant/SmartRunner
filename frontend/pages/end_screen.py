import pygame
from assets.components import *
from page import *


class EndScreenPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "end_screen"
        self.input_data = {
            "score_board": [],
            "roomID": "Room ID",
        }
        self.output_data = {
            "current_page": self.name,
            "room_ID": self.input_data["roomID"],
            "score_board": self.input_data["score_board"],
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/img/sky.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

#relative_x, relative_y, relative_width, relative_height,relative_shown_width, relative_shown_height,
        # player list
        relative_x = 0.05
        relative_y = 0.15
        relative_width = 0.8
        text_relative_height = 1 / 10
        shown_relative_width = 6 / 10
        shown_relative_height = 3 / 5
        player_results = MouseScrollableSurface("player_results", screen, relative_x,
                                                  relative_y, relative_width,
                                                  text_relative_height, shown_relative_width, shown_relative_height,
                                                  screen)
        #create surface
        self.components["player_results"] = player_results
        self.layers.append(player_results)


        #SelectableTextList
        relative_x = 0.05
        relative_y = 0.15
        relative_width = 0.8
        text_relative_height = 1 / 10
        shown_relative_width = 0.7
        shown_relative_height = 3 / 5
        score_text_list = self.input_data["score_board"]
        # print(self.input_data.keys())
        # print(score_text_list)

        score_board_text_list = SelectableTextList("score_board_text_list", screen, relative_x,
                                                  relative_y, relative_width,
                                                  text_relative_height, shown_relative_width, shown_relative_height,
                                                  score_text_list, screen, single_select=True, active_color="white")

        self.components["score_board_text_list"] = score_board_text_list
        player_results.add_component(score_board_text_list)
        self.layers.append(score_board_text_list)


        # Player Score display
        # player_results_display_x = 1 / 4
        # player_results_display_y = 1 / 4
        # player_results_display_width = 1 / 2
        # player_results_display_height = 1 / 4
        # player_results_text ="Player 1: Score"
        # player_results_display = TextDisplay("player_results_display", screen, player_results_display_x, player_results_display_y, player_results_display_width,
        #                       player_results_display_height,player_results_text)
        # self.components["player_results_display"] = player_results_display


        # Share button
        share_button_x = 7 / 10
        share_button_y = 4 / 5
        share_button_width = 1 / 4
        share_button_height = 1 / 7
        share_button__img = pygame.image.load('assets/img/exit_btn.png')
        share_button = ImageButton("share_button", screen, share_button_x, share_button_y,
                             share_button_width,
                             share_button_height, share_button__img)
        self.components["share_button"] = share_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            if triggered_component in [self.components["share_button"]]:
                self.name = "share"
            # if triggered_component in [self.components["player_results"]]:
            #     print("store  in self.output_data[roomID] for sharing")
            else:
                print("entry failed")
