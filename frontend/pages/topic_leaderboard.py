import pygame
from assets.components import *
from page import *


class TopicLeaderboardPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "topic_leaderboard"
        self.input_data = {
            "topic_leaderboard_ID": "",
            "topic_leaderboard": [],
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "topic_leaderboard_ID": self.input_data["topic_leaderboard_ID"],
            "topic_leaderboard": self.input_data["topic_leaderboard"],
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/img/sky.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # Player Score display
        player_score_display_x = 5 / 20
        player_score_display_y = 3 / 40
        player_score_display_width = 1 / 2
        player_score_display_height = 1 / 4
        player_score_text ="Topic Leaderboard"
        player_score_display = TextDisplay("Topic Leaderboard", screen, player_score_display_x, player_score_display_y, player_score_display_width,
                              player_score_display_height,player_score_text)
        self.components["player_score_display"] = player_score_display

        # player list
        relative_x = 4 / 20
        relative_y = 7 / 40
        relative_width = 0.8
        text_relative_height = 1 / 10
        shown_relative_width = 6 / 10
        shown_relative_height = 3 / 5
        topic_leaderboard_results = MouseScrollableSurface("topic_results", screen, relative_x,
                                                relative_y, relative_width,
                                                text_relative_height, shown_relative_width, shown_relative_height,
                                                screen)
        # create surface
        self.components["topic_results"] = topic_leaderboard_results
        self.layers.append(topic_leaderboard_results)

        # SelectableTextList
        relative_x = 4 / 20
        relative_y = 7 / 40
        relative_width = 0.8
        text_relative_height = 1 / 10
        shown_relative_width = 6 / 10
        shown_relative_height = 3 / 5
        score_text_list = self.input_data["topic_leaderboard"][self.input_data["topic_leaderboard_ID"]]
        # print(self.input_data.keys())
        # print(score_text_list)

        topic_board_text_list = SelectableTextList("topic_board_text_list", screen, relative_x,
                                                   relative_y, relative_width,
                                                   text_relative_height, shown_relative_width, shown_relative_height,
                                                   score_text_list, screen, single_select=True, active_color="white")

        self.components["topic_board_text_list"] = topic_board_text_list
        topic_leaderboard_results.add_component(topic_board_text_list)
        self.layers.append(topic_board_text_list)


        #Share button
        share_button_x = 7 / 10
        share_button_y = 8 / 10
        share_button_width = 1 / 4
        share_button_height = 1 / 6
        share_button__img = pygame.image.load('assets/img/exit_btn.png')
        share_button = ImageButton("share_button", screen, share_button_x, share_button_y,
                             share_button_width,
                             share_button_height, share_button__img)
        self.components["share_button"] = share_button

        #return button
        return_button_x = 1 / 20
        return_button_y = 8 / 10
        return_button_width = 1 / 4
        return_button_height = 1 / 6
        return_button__img = pygame.image.load('assets/img/start_btn.png')
        return_button = ImageButton("return_button", screen, return_button_x, return_button_y,
                                   return_button_width,
                                   return_button_height, return_button__img)
        self.components["return_button"] = return_button

    #how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.name
            if triggered_component in [self.components["share_button"]]:
                self.name = "share"
            if triggered_component in [self.components["return_button"]]:
                self.name = "leadselect"
            # if triggered_component in ["player_score_display", "share_button", "return_button"]:
            #     return self.data
