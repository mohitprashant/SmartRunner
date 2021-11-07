import pygame
from assets.components import *
from page import *


class QuestionSelectPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "question_select"
        self.input_data = {
            "roomID": "",
            "username": "",
            # "room_password": "",
            "custom_question_selection": [],
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "room_ID": "",
            "username": "",
            # "room_password": "",
            "custom_question_selection": "",
            "exit": False
        }



    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/Backgrounds/background.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # custom_quiz_display_x = 10 / 20
        # custom_quiz_display_y = 7/8
        # custom_quiz_display_width = 1 / 2
        # custom_quiz_display_height = 1 / 4
        # custom_quiz_display_text = "Custom Questions"
        # custom_quiz_display = TextDisplay("custom_questions", screen, custom_quiz_display_x, custom_quiz_display_y,
        #                                    custom_quiz_display_width,
        #                                    custom_quiz_display_height, custom_quiz_display_text)
        # self.components["custom_questions"] = custom_quiz_display
        # print("displayed")

        # # player list
        # relative_x = 4 / 20
        # relative_y = 7 / 40
        # relative_width = 0.8
        # text_relative_height = 8/ 10
        # shown_relative_width = 6 / 10
        # shown_relative_height = 3 / 5
        # custom_questions_whole = MouseScrollableSurface("custom_questions_whole", screen, relative_x,
        #                                                    relative_y, relative_width,
        #                                                    text_relative_height, shown_relative_width,
        #                                                    shown_relative_height,
        #                                                    screen)
        # # create surface
        # self.components["custom_questions_whole"] = custom_questions_whole
        # self.layers.append(custom_questions_whole)

        list_image_rel_x = 0.095
        list_image_rel_y = 0.1
        list_image_rel_width = 0.8
        list_image_rel_height = 0.7
        list_img = pygame.image.load('assets/Backgrounds/scrollable.png')
        analyticslist_image = ImageDisplay("analyticslist_image", screen, list_image_rel_x, list_image_rel_y,
                                           list_image_rel_width,
                                           list_image_rel_height, list_img)
        self.components["analyticslist_image"] = analyticslist_image

        # SelectableTextList
        relative_x = 0.2
        relative_y = 0.2
        relative_width = 0.55
        text_relative_height = 0.1
        shown_relative_width = 0.55
        shown_relative_height = 0.5
        # relative_x = 4/20
        # relative_y = 7/40
        # relative_width = 0.8
        # text_relative_height = 8/10
        # shown_relative_width = 6 / 10
        # shown_relative_height = 0.6
        custom_questions_list = self.input_data["custom_question_selection"]
        # print(self.input_data.keys())
        # print(custom_questions_list)

        custom_questions = SelectableTextList("custom_questions", screen, relative_x,
                                                   relative_y, relative_width,
                                                   text_relative_height, shown_relative_width, shown_relative_height,
                                                   custom_questions_list, screen, single_select=False, active_color="blue")

        self.components["custom_questions"] = custom_questions
        #custom_questions_whole.add_component(custom_questions)
        self.layers.append(custom_questions)

        # return button
        return_button2_x = 1 / 20
        return_button2_y = 17 / 20
        return_button2_width = 1 / 10
        return_button2_height = 1 / 10
        return_button2__img = pygame.image.load('assets/Buttons/btn_back.png')
        return_button2 = ImageButton("return_button2", screen, return_button2_x, return_button2_y,
                                    return_button2_width,
                                    return_button2_height, return_button2__img)
        self.components["return_button2"] = return_button2

        # # confirm button
        # confirm_button2_x = 17 / 20
        # confirm_button2_y = 17 / 20
        # confirm_button2_width = 1 / 10
        # confirm_button2_height = 1 / 10
        # confirm_button2__img = pygame.image.load('assets/img/save_btn.png')
        # confirm_button2 = ImageButton("confirm_button2", screen, confirm_button2_x, confirm_button2_y,
        #                             confirm_button2_width,
        #                             confirm_button2_height, confirm_button2__img)
        # self.components["confirm_button2"] = confirm_button2

        # confirm button
        add_question_button2_x = 0.78
        add_question_button2_y = 13 / 20
        add_question_button2_width = 1 / 10
        add_question_button2_height = 1 / 10
        add_question_button2__img = pygame.image.load('assets/Buttons/btn_add.png')
        add_question_button2 = ImageButton("add_question_button2", screen, add_question_button2_x, add_question_button2_y,
                                      add_question_button2_width,
                                      add_question_button2_height, add_question_button2__img)
        self.components["add_question_button2"] = add_question_button2

        # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["roomID"] = self.input_data["roomID"]
            self.output_data["username"] = self.input_data["username"]
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["custom_question_selection"] = self.input_data["custom_question_selection"]
            #self.output_data["room_password"] = self.input_data["room_password"]
            if triggered_component in [self.components["return_button2"]]:
                self.name = "custom_select"
            if triggered_component in [self.components["add_question_button2"]]:
                self.name = "add_question"
            # if triggered_component in [self.components["confirm_button2"]]:
            #     print("Go to game session")