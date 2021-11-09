import pygame.cursors

from assets.components import *
from page import *


class SinglePlayerPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "singleplayer"
        self.input_data = {
            "back_navigation": "",
            "subjectlist": [],
            "topiclist": [],
            "difficultylist": [],
            "subjectselection": "",
            "prev_page": ""

        }
        self.output_data = {
            "back_navigation": "",
            "current_page": self.name,
            "prev_page": "",
            "username": "",
            "password": "",
            "exit": False,
            "subjectselection": "",
            "topicselection": "",
            "difficultyselection": ""
        }


    # set all component variables on input screen
    def set_components(self, screen):
        self.name = "singleplayer"

        # change back navigation every time page changes
        if self.input_data["prev_page"] != self.name:
            self.output_data["back_navigation"] = self.input_data["prev_page"]

        # background
        bg_img = pygame.image.load('assets/Backgrounds/singleplayerbg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # start button
        start_button_rel_x = 3 / 7
        start_button_rel_y = 4 / 5
        start_button_rel_width = 1 / 7
        start_button_rel_height = 1 / 7
        start_button_img = pygame.image.load('assets/Buttons/btn_start.png')
        start_button = ImageButton("start_button", screen, start_button_rel_x, start_button_rel_y, start_button_rel_width,
                              start_button_rel_height, start_button_img)
        self.components["start_button"] = start_button

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

        # difficulty list
        difficultylist_rel_x = 1 / 7
        difficultylist_rel_y = 5 / 10
        difficultylist_rel_width = 5 / 7
        difficultylist_rel_height = 1 / 10
        difficultylist_text_list = self.input_data["difficultylist"]
        prompt = "Select Difficulty"
        num_expand_text = 3
        difficultylist = DropdownTextSelect("difficultylist", screen, difficultylist_rel_x, difficultylist_rel_y,
                                            difficultylist_rel_width,
                                            difficultylist_rel_height, difficultylist_text_list, prompt,
                                            num_expand_text, screen)
        self.components["difficultylist"] = difficultylist
        self.layers.append(difficultylist)

        # topic list
        topiclist_rel_x = 1 / 7
        topiclist_rel_y = 3 / 10
        topiclist_rel_width = 5 / 7
        topiclist_rel_height = 1 / 10
        topiclist_text_list = self.input_data["topiclist"][self.input_data["subjectselection"]]
        prompt = "Select Topic"
        num_expand_text = 3
        topiclist = DropdownTextSelect("topiclist", screen, topiclist_rel_x, topiclist_rel_y,
                                       topiclist_rel_width,
                                       topiclist_rel_height, topiclist_text_list, prompt, num_expand_text, screen)
        self.components["topiclist"] = topiclist
        self.layers.append(topiclist)

        # subject list
        subjectlist_rel_x = 1 / 7
        subjectlist_rel_y = 1 / 10
        subjectlist_rel_width = 5 / 7
        subjectlist_rel_height = 1 / 10
        subjectlist_text_list = self.input_data["subjectlist"]
        prompt = "Select Subject"
        num_expand_text = 3
        subjectlist = DropdownTextSelect("subjectlist", screen, subjectlist_rel_x, subjectlist_rel_y,
                                         subjectlist_rel_width,
                                         subjectlist_rel_height, subjectlist_text_list, prompt, num_expand_text, screen)
        self.components["subjectlist"] = subjectlist
        self.layers.append(subjectlist)

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            if triggered_component in [self.components["start_button"]]:
                self.output_data["prev_page"] = self.output_data["current_page"]
                print("start game session")

            if triggered_component in [self.components["exit_button"]]:
                self.output_data["prev_page"] = self.output_data["current_page"]
                self.name = "main_menu"
            if triggered_component in [self.components["subjectlist"]]:
                if self.components["subjectlist"].button.text!= "Select Subject":
                    self.input_data["subjectselection"] = self.components["subjectlist"].button.text
                    print(self.components["subjectlist"].button.text)



