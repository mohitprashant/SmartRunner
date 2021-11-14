from assets.components import *
from page import *


class AnalyticsSelectPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "analyticsselect"
        self.input_data = {
            "analyticslist": [],
            "username":"",
            "roomID": ""
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "roomID": "",
            "analyticsID": "",
            "username":"",
            "all_time": False,
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        self.name = "analyticsselect"

        # change back navigation every time page changes
        if self.input_data["prev_page"] != self.name:
            self.output_data["back_navigation"] = self.input_data["prev_page"]

        # assign output data
        self.output_data["roomID"] = self.input_data["roomID"]

        # background
        bg_img = pygame.image.load('assets/Backgrounds/analyticsbg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # analytics list image
        list_image_rel_x = 0.095
        list_image_rel_y = 0.1
        list_image_rel_width = 0.8
        list_image_rel_height = 0.7
        list_img = pygame.image.load('assets/Backgrounds/scrollable.png')
        analyticslist_image = ImageDisplay("analyticslist_image", screen, list_image_rel_x, list_image_rel_y,
                                           list_image_rel_width, list_image_rel_height, list_img)
        self.components["analyticslist_image"] = analyticslist_image

        # analytics list
        relative_x = 0.2
        relative_y = 0.2
        relative_width = 0.55
        text_relative_height = 0.1
        shown_relative_width = 0.55
        shown_relative_height = 0.5
        text_list = self.input_data["analyticslist"]

        textbox_button_list = TextboxButtonList("textbox_button_list", screen, relative_x, relative_y, relative_width,
                                                text_relative_height, shown_relative_width, shown_relative_height,
                                                text_list, screen)
        self.components["textbox_button_list"] = textbox_button_list
        self.layers.append(textbox_button_list)

        # player status header
        header_image_rel_x = 0.27
        header_image_rel_y = 0.02
        header_image_rel_width = 0.4
        header_image_rel_height = 0.15
        header_img = pygame.image.load('assets/Backgrounds/gamesessions.png')
        analyticsheader_image = ImageDisplay("analyticsheader_image", screen, header_image_rel_x, header_image_rel_y,
                                             header_image_rel_width, header_image_rel_height, header_img)
        self.components["analyticsheader_image"] = analyticsheader_image

        # back button
        exit_button_rel_x = 1 / 15
        exit_button_rel_y = 4 / 5
        exit_button_rel_width = 1 / 7
        exit_button_rel_height = 1 / 7
        exit_button_img = pygame.image.load('assets/Buttons/btn_back.png')
        exit_button = ImageButton("exit_button", screen, exit_button_rel_x, exit_button_rel_y,
                                  exit_button_rel_width, exit_button_rel_height, exit_button_img)
        self.components["exit_button"] = exit_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["username"] = self.input_data["username"]
            self.output_data["roomID"] = self.input_data["roomID"]
            self.output_data["player_status"] = []
            self.output_data["mode_toggle"] = self.input_data["mode_toggle"]
            self.output_data["toggled"] = self.input_data["toggled"]
            self.output_data["custom_quiz_selection"] = self.input_data["custom_quiz_selection"]
            self.output_data["join_host"] = self.input_data["join_host"]

            if triggered_component in [self.components["textbox_button_list"]]:
                for tc in triggered_component.triggered_component_list:
                    self.output_data["analyticsID"] = tc.text
                self.name = "uniqueanalytics"
            if triggered_component in [self.components["exit_button"]]:
                self.name = "hostroom"
