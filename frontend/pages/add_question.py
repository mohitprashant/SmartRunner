import pygame
from assets.components import *
from page import *


class AddQuestionPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "add_question"
        self.input_data = {
            "roomID": "",
            "username": "",
            "custom_question_new": "",
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "room_ID": "",
            "username": "",
            "custom_question_new": "",
            "exit": False
        }



    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/Backgrounds/settingsbg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        header_image_rel_x = 6/20
        header_image_rel_y = 2/40
        header_image_rel_width = 1/3
        header_image_rel_height = 0.15
        header_img = pygame.image.load('assets/Backgrounds/addqn.png')
        addquestions_header = ImageDisplay("addquestions_header", screen, header_image_rel_x,
                                               header_image_rel_y,
                                               header_image_rel_width,
                                               header_image_rel_height, header_img)
        self.components["addquestions_header"] = addquestions_header

        question_image_rel_x = 0.1
        question_image_rel_y = 0.3
        question_image_rel_width = 1 / 4
        question_image_rel_height = 1 / 8
        question_image_img = pygame.image.load('assets/Backgrounds/username.png')
        question_image_box = ImageDisplay("question_image_box", screen, question_image_rel_x, question_image_rel_y,
                                          question_image_rel_width, question_image_rel_height, question_image_img)
        self.components["question_image_box"] = question_image_box

        options_image_rel_x = 0.1
        options_image_rel_y = 0.4
        options_image_rel_width = 1 / 4
        options_image_rel_height = 1 / 8
        options_image_img = pygame.image.load('assets/Backgrounds/password.png')
        options_image_box = ImageDisplay("options_image_box", screen, options_image_rel_x, options_image_rel_y,
                                          options_image_rel_width, options_image_rel_height, options_image_img)
        self.components["options_image_box"] = options_image_box


        question_input_rel_x = 0.4
        question_input_rel_y = 0.3
        question_input_rel_width = 0.4
        question_input_rel_height = 1 / 12
        question_input_box = TextInput("question_new", screen, question_input_rel_x, question_input_rel_y,
                                       question_input_rel_width, question_input_rel_height)
        self.components["question_new"] = question_input_box


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

        # SelectableTextList
        # relative_x = 1 / 20
        # relative_y = 3 / 20
        # relative_width = 0.8
        # text_relative_height = 1 / 10
        # shown_relative_width = 7 / 10
        # shown_relative_height = 3 / 5
        # # relative_x = 4/20
        # # relative_y = 7/40
        # # relative_width = 0.8
        # # text_relative_height = 8/10
        # # shown_relative_width = 6 / 10
        # # shown_relative_height = 0.6
        # selected_question = self.input_data["custom_question_selection"]
        # # print(self.input_data.keys())
        # # print(custom_questions_list)
        #
        # custom_questions = SelectableTextList("custom_questions", screen, relative_x,
        #                                            relative_y, relative_width,
        #                                            text_relative_height, shown_relative_width, shown_relative_height,
        #                                            selected_question, screen, single_select=False, active_color="blue")
        #
        # self.components["custom_questions"] = custom_questions
        # #custom_questions_whole.add_component(custom_questions)
        # self.layers.append(custom_questions)

        # return button
        return_button2_x = 1 / 15
        return_button2_y = 17 / 20
        return_button2_width = 1 / 7
        return_button2_height = 1 / 7
        return_button2__img = pygame.image.load('assets/Buttons/btn_back.png')
        return_button2 = ImageButton("return_button2", screen, return_button2_x, return_button2_y,
                                    return_button2_width,
                                    return_button2_height, return_button2__img)
        self.components["return_button2"] = return_button2

        # confirm button
        confirm_button2_x = 16 / 20
        confirm_button2_y = 17 / 20
        confirm_button2_width = 1 / 7
        confirm_button2_height = 1 / 7
        confirm_button2__img = pygame.image.load('assets/Buttons/btn_confirm.png')
        confirm_button2 = ImageButton("confirm_button2", screen, confirm_button2_x, confirm_button2_y,
                                    confirm_button2_width,
                                    confirm_button2_height, confirm_button2__img)
        self.components["confirm_button2"] = confirm_button2


        # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["roomID"] = self.input_data["roomID"]
            self.output_data["username"] = self.input_data["username"]
            self.output_data["prev_page"] = self.output_data["current_page"]
            # self.output_data["custom_question_selection"] = self.input_data["custom_question_selection"]
            if triggered_component in [self.components["confirm_button2"]]:
                print("Put new question in database")
                self.output_data["custom_question_new"] = self.components["question_new"].input
                print("question added")
            if triggered_component in [self.components["return_button2"]]:
                print("go back to question select")
                self.name = "question_select"