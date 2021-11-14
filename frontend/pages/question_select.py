import pygame
from assets.components import *
from page import *
import sys
sys.path.insert(1, '../../backend/database')
import QuestionManager


class QuestionSelectPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "question_select"
        self.input_data = {
            "roomID": "",
            "username": "",
            "toggled":"",
            "custom_quiz_selection": "",
            "custom_question_selection": []
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "room_ID": "",
            "username": "",
            "toggled":"",
            "custom_quiz_selection":"",
            "custom_question_selection": [],
            "exit": False
        }



    def set_components(self, screen):
        self.name = "question_select"

        # change back navigation every time page changes
        if self.input_data["prev_page"] != self.name:
            self.output_data["back_navigation"] = self.input_data["prev_page"]

        # background
        bg_img = pygame.image.load('assets/Backgrounds/settingsbg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        if self.input_data["custom_quiz_selection"]!="New Quiz":
            quiz_name_img_rel_x = 0.2
            quiz_name_img_rel_y = 0.03
            quiz_name_img_rel_width = 0.53
            quiz_name_img_rel_height = 0.15
            quiz_name_back_img = pygame.image.load('assets/Backgrounds/quizname.png')
            quiz_name_img = ImageDisplay("quiz_name_img", screen, quiz_name_img_rel_x, quiz_name_img_rel_y,
                                         quiz_name_img_rel_width,
                                         quiz_name_img_rel_height, quiz_name_back_img)
            self.components["quiz_name_img"] = quiz_name_img

            quiz_name_image_rel_x = 0.3
            quiz_name_image_rel_y = 0.054
            quiz_name_image_rel_width = 0.3
            quiz_name_image_rel_height = 0.1
            quiz_name_image_img = self.input_data["custom_quiz_selection"]
            quiz_name_image_box = TextDisplay("quiz_name_image_box", screen, quiz_name_image_rel_x,
                                              quiz_name_image_rel_y,
                                              quiz_name_image_rel_width, quiz_name_image_rel_height,
                                              quiz_name_image_img)
            self.components["quiz_name_image_box"] = quiz_name_image_box


            self.components.pop("new_quiz_name_img", None)
            self.components.pop("quiz_name_input_box", None)
        elif self.input_data["custom_quiz_selection"]=="New Quiz":
            new_quiz_name_img_rel_x = 0.05
            new_quiz_name_img_rel_y = 0.04
            new_quiz_name_img_rel_width = 0.3
            new_quiz_name_img_rel_height = 0.13
            new_quiz_name_back_img = pygame.image.load('assets/Backgrounds/enterquizname.png')
            new_quiz_name_img = ImageDisplay("new_quiz_name_img", screen, new_quiz_name_img_rel_x, new_quiz_name_img_rel_y,
                                         new_quiz_name_img_rel_width,
                                         new_quiz_name_img_rel_height, new_quiz_name_back_img)
            self.components["new_quiz_name_img"] = new_quiz_name_img

            quiz_name_input_rel_x = 0.37
            quiz_name_input_rel_y = 0.05
            quiz_name_input_rel_width = 0.5
            quiz_name_input_rel_height = 1 / 12
            quiz_name_input_box = TextInput("quiz_name_input_box", screen, quiz_name_input_rel_x, quiz_name_input_rel_y,
                                            quiz_name_input_rel_width, quiz_name_input_rel_height)
            self.components["quiz_name_input_box"] = quiz_name_input_box

            self.components.pop("quiz_name_image_box", None)
            self.components.pop("quiz_name_img", None)


        list_image_rel_x = 0.095
        list_image_rel_y = 0.25
        list_image_rel_width = 0.8
        list_image_rel_height = 0.6
        list_img = pygame.image.load('assets/Backgrounds/scrollable.png')
        questionselect_image = ImageDisplay("questionselect_image", screen, list_image_rel_x, list_image_rel_y,
                                           list_image_rel_width,
                                           list_image_rel_height, list_img)
        self.components["questionselect_image"] = questionselect_image

        # SelectableTextList
        relative_x = 0.2
        relative_y = 0.35
        relative_width = 0.55
        text_relative_height = 0.1
        shown_relative_width = 0.55
        shown_relative_height = 0.4
        custom_questions_list = self.input_data["question_list"]
        # print(self.input_data.keys())
        # print(custom_questions_list)

        custom_questions = SelectableTextList("custom_questions", screen, relative_x,
                                                   relative_y, relative_width,
                                                   text_relative_height, shown_relative_width, shown_relative_height,
                                                   custom_questions_list, screen, single_select=False, active_color="blue")

        self.components["custom_questions"] = custom_questions
        #custom_questions_whole.add_component(custom_questions)
        self.layers.append(custom_questions)

        custom_quiz_display_x = 6 / 20
        custom_quiz_display_y = 0.17
        custom_quiz_display_width = 1 / 3
        custom_quiz_display_height = 0.15
        custom_quiz_text = pygame.image.load('assets/Backgrounds/questions.png')
        custom_quiz_display = ImageDisplay("custom_quiz_display", screen, custom_quiz_display_x,
                                           custom_quiz_display_y, custom_quiz_display_width,
                                           custom_quiz_display_height, custom_quiz_text)
        self.components["custom_quiz_display"] = custom_quiz_display

        # return button
        return_button2_x = 1 / 15
        return_button2_y = 17/20
        return_button2_width = 1 / 7
        return_button2_height = 1 / 8
        return_button2__img = pygame.image.load('assets/Buttons/btn_back.png')
        return_button2 = ImageButton("return_button2", screen, return_button2_x, return_button2_y,
                                    return_button2_width,
                                    return_button2_height, return_button2__img)
        self.components["return_button2"] = return_button2

        # confirm button
        add_question_button2_x = 0.83
        add_question_button2_y = 10 / 20
        add_question_button2_width = 1 / 10
        add_question_button2_height = 1 / 10
        add_question_button2__img = pygame.image.load('assets/Buttons/btn_add.png')
        add_question_button2 = ImageButton("add_question_button2", screen, add_question_button2_x, add_question_button2_y,
                                      add_question_button2_width,
                                      add_question_button2_height, add_question_button2__img)
        self.components["add_question_button2"] = add_question_button2

        delete_question_button2_x = 0.83
        delete_question_button2_y = 13 / 20
        delete_question_button2_width = 1 / 10
        delete_question_button2_height = 1 / 10
        delete_question_button2__img = pygame.image.load('assets/Buttons/btn_deleteqn.png')
        delete_question_button2 = ImageButton("delete_question_button2", screen, delete_question_button2_x,
                                           delete_question_button2_y,
                                           delete_question_button2_width,
                                           delete_question_button2_height, delete_question_button2__img)
        self.components["delete_question_button2"] = delete_question_button2

        # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["roomID"] = self.input_data["roomID"]
            self.output_data["username"] = self.input_data["username"]
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["custom_quiz_selection"] = self.input_data["custom_quiz_selection"]
            self.output_data["custom_question_selection"] = self.input_data["custom_question_selection"]
            self.output_data["toggled"] = self.input_data["toggled"]
            self.output_data["correct_option"] = "Correct Option"
            self.output_data["selected_question"] = self.input_data["selected_question"]

            if triggered_component in [self.components["return_button2"]]:
                self.name = "custom_select"
            if triggered_component in [self.components["add_question_button2"]]:
                if self.input_data["custom_quiz_selection"] == "":
                    self.name = "question_select"
                elif self.input_data["custom_quiz_selection"] == "New Quiz":
                    self.input_data["custom_quiz_selection"] = self.components["quiz_name_input_box"].input
                    self.output_data["custom_quiz_selection"] = self.input_data["custom_quiz_selection"]
                    self.name = "add_question"
                else:
                    self.name = "add_question"

            if triggered_component in [self.components["custom_questions"]]:
                self.input_data["selected_question"] = self.input_data["retrieve_id"][triggered_component.selected_text[0]]
                self.output_data["selected_question"] = self.input_data["selected_question"]
                self.name = "question_select"
            if triggered_component in [self.components["delete_question_button2"]]:
                print(self.output_data["username"], self.output_data["roomID"],self.output_data["custom_quiz_selection"], self.output_data["selected_question"])
                QuestionManager.delete_custom_question(self.output_data["username"], self.output_data["roomID"],self.output_data["custom_quiz_selection"], self.output_data["selected_question"])
                print("delete question", self.output_data["selected_question"], "from database")
