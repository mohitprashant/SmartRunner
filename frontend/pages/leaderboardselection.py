from assets.components import *
from page import *


class LeadSelectPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "leadselect"
        self.input_data = {
            "leaderboardlist": []
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "username": "",
            "password": "",
            "topic_leaderboard_ID": "",
            "back_navigation": "",
            "exit": False
        }


    # set all component variables on input screen
    def set_components(self, screen):
        self.name = "leadselect"

        # change back navigation every time page changes
        if self.input_data["prev_page"] != self.name:
            self.output_data["back_navigation"] = self.input_data["prev_page"]

        # background
        bg_img = pygame.image.load('assets/Backgrounds/leaderboards.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # leaderboard list image
        list_image_rel_x = 0.145
        list_image_rel_y = 0.1
        list_image_rel_width = 0.8
        list_image_rel_height = 0.7
        list_img = pygame.image.load('assets/Backgrounds/scrollable.png')
        leaderboardlist_image = ImageDisplay("leaderboardlist_image", screen, list_image_rel_x, list_image_rel_y,
                                       list_image_rel_width,
                                       list_image_rel_height, list_img)
        self.components["leaderboardlist_image"] = leaderboardlist_image

        # leaderboard list
        relative_x = 0.25
        relative_y = 0.2
        relative_width = 0.55
        text_relative_height = 0.1
        shown_relative_width = 0.55
        shown_relative_height = 0.5
        text_list = self.input_data["leaderboardlist"]

        textbox_button_list = TextboxButtonList("textbox_button_list", screen, relative_x,
                                                  relative_y, relative_width,
                                                  text_relative_height, shown_relative_width, shown_relative_height,
                                                  text_list, screen)
        self.components["textbox_button_list"] = textbox_button_list
        self.layers.append(textbox_button_list)

        # leaderboards header
        header_image_rel_x = 0.38
        header_image_rel_y = 0.02
        header_image_rel_width = 0.25
        header_image_rel_height = 0.15
        header_img = pygame.image.load('assets/Backgrounds/leaderboards.png')
        leaderboardheader_image = ImageDisplay("leaderboardheader_image", screen, header_image_rel_x, header_image_rel_y,
                                        header_image_rel_width,
                                        header_image_rel_height, header_img)
        self.components["leaderboardheader_image"] = leaderboardheader_image

        # back button
        exit_button_rel_x = 1 / 15
        exit_button_rel_y = 4 / 5
        exit_button_rel_width = 1 / 7
        exit_button_rel_height = 1 / 7
        exit_button_img = pygame.image.load('assets/Buttons/btn_back.png')
        exit_button = ImageButton("exit_button", screen, exit_button_rel_x, exit_button_rel_y,
                                   exit_button_rel_width,
                                   exit_button_rel_height, exit_button_img)
        self.components["exit_button"] = exit_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            if triggered_component in [self.components["exit_button"]]:
                self.name = "main_menu"
            if triggered_component in [self.components["textbox_button_list"]]:
                for tc in triggered_component.triggered_component_list:
                    self.output_data["topic_leaderboard_ID"] = tc.text
                self.name = "topic_leaderboard"
