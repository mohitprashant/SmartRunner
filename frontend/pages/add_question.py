import pygame
from assets.components import *
from page import *
import sys
sys.path.insert(1, '../../backend/database')
import QuestionManager
import uuid


class AddQuestionPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "add_question"
        self.input_data = {
            "roomID": "",
            "username": "",
            "toggled": "",
            "custom_quiz_selection": "",
            "custom_question_selection": "",
            "prev_page": ""
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "room_ID": "",
            "username": "",
            "question_id": "",
            "description":"",
            "difficulty_level":"",
            "correct_option": "",
            "wrong1":"",
            "wrong2":"",
            "wrong3":"",
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
                                           header_image_rel_y, header_image_rel_width,
                                           header_image_rel_height, header_img)
        self.components["addquestions_header"] = addquestions_header

        question_image_rel_x = 0.18
        question_image_rel_y = 0.27
        question_image_rel_width = 0.2
        question_image_rel_height = 1 / 9
        question_image_img = "Description"
        question_image_box = TextDisplay("question_image_box", screen, question_image_rel_x, question_image_rel_y,
                                         question_image_rel_width, question_image_rel_height, question_image_img)
        self.components["question_image_box"] = question_image_box

        question_input_rel_x = 0.4
        question_input_rel_y = 0.25
        question_input_rel_width = 0.5
        question_input_rel_height = 1 / 12
        question_input_box = TextInput("question_input_box", screen, question_input_rel_x, question_input_rel_y,
                                       question_input_rel_width, question_input_rel_height)
        self.components["question_input_box"] = question_input_box

        difficulty_level_image_rel_x = 0.13
        difficulty_level_image_rel_y = 0.37
        difficulty_level_image_rel_width = 1 / 4
        difficulty_level_image_rel_height = 1 / 8
        difficulty_level_image_img = "Difficulty Level"
        difficulty_level_image_box = TextDisplay("difficulty_level_image_box", screen, difficulty_level_image_rel_x,
                                                 difficulty_level_image_rel_y, difficulty_level_image_rel_width,
                                                 difficulty_level_image_rel_height, difficulty_level_image_img)
        self.components["difficulty_level_image_box"] = difficulty_level_image_box

        difficulty_input_rel_x = 0.4
        difficulty_input_rel_y = 0.35
        difficulty_input_rel_width = 0.15
        difficulty_input_rel_height = 1 / 12
        difficulty_input_box = TextInput("difficulty_input_box", screen, difficulty_input_rel_x, difficulty_input_rel_y,
                                         difficulty_input_rel_width, difficulty_input_rel_height)
        self.components["difficulty_input_box"] = difficulty_input_box

        option_image_rel_x = 0.23
        option_image_rel_y = 0.46
        option_image_rel_width = 1 / 7
        option_image_rel_height = 1 / 8
        option_image_img = "Options"
        option_image_box = TextDisplay("option_image_box", screen, option_image_rel_x, option_image_rel_y,
                                       option_image_rel_width, option_image_rel_height, option_image_img)
        self.components["option_image_box"] = option_image_box

        correct_image_rel_x = 0.13
        correct_image_rel_y = 0.66
        correct_image_rel_width = 1 / 4
        correct_image_rel_height = 1 / 8
        correct_image_img = "Correct Option"
        correct_image_box = TextDisplay("correct_image_box", screen, correct_image_rel_x, correct_image_rel_y,
                                        correct_image_rel_width, correct_image_rel_height, correct_image_img)
        self.components["correct_image_box"] = correct_image_box

        option1_input_rel_x = 0.4
        option1_input_rel_y = 0.45
        option1_input_rel_width = 0.15
        option1_input_rel_height = 1 / 12
        option1_input_box = TextInput("option1_input_box", screen, option1_input_rel_x, option1_input_rel_y,
                                      option1_input_rel_width, option1_input_rel_height)
        self.components["option1_input_box"] = option1_input_box

        option2_input_rel_x = 0.57
        option2_input_rel_y = 0.45
        option2_input_rel_width = 0.15
        option2_input_rel_height = 1 / 12
        option2_input_box = TextInput("option2_input_box", screen, option2_input_rel_x, option2_input_rel_y,
                                      option2_input_rel_width, option2_input_rel_height)
        self.components["option2_input_box"] = option2_input_box

        option3_input_rel_x = 0.4
        option3_input_rel_y = 0.55
        option3_input_rel_width = 0.15
        option3_input_rel_height = 1 / 12
        option3_input_box = TextInput("option3_input_box", screen, option3_input_rel_x, option3_input_rel_y,
                                      option3_input_rel_width, option3_input_rel_height)
        self.components["option3_input_box"] = option3_input_box

        option4_input_rel_x = 0.57
        option4_input_rel_y = 0.55
        option4_input_rel_width = 0.15
        option4_input_rel_height = 1 / 12
        option4_input_box = TextInput("option4_input_box", screen, option4_input_rel_x, option4_input_rel_y,
                                      option4_input_rel_width, option4_input_rel_height)
        self.components["option4_input_box"] = option4_input_box

        correct_option_rel_x = 0.4
        correct_option_rel_y = 0.65
        correct_option_rel_width = 0.5
        correct_option_rel_height = 1 / 12
        correct_option_text_list = ["A", "B", "C", "D"]
        prompt = "Select one"
        num_expand_text = 3
        correct_option = DropdownTextSelect("correct_option", screen, correct_option_rel_x, correct_option_rel_y,
                                            correct_option_rel_width, correct_option_rel_height,
                                            correct_option_text_list, prompt, num_expand_text, screen)
        self.components["correct_option"] = correct_option
        self.layers.append(correct_option)

        # return button
        return_button2_x = 1 / 15
        return_button2_y = 17 / 20
        return_button2_width = 1 / 7
        return_button2_height = 1 / 7
        return_button2__img = pygame.image.load('assets/Buttons/btn_back.png')
        return_button2 = ImageButton("return_button2", screen, return_button2_x, return_button2_y, return_button2_width,
                                     return_button2_height, return_button2__img)
        self.components["return_button2"] = return_button2

        # confirm button
        confirm_button2_x = 16 / 20
        confirm_button2_y = 17 / 20
        confirm_button2_width = 1 / 7
        confirm_button2_height = 1 / 7
        confirm_button2__img = pygame.image.load('assets/Buttons/btn_confirm.png')
        confirm_button2 = ImageButton("confirm_button2", screen, confirm_button2_x, confirm_button2_y,
                                      confirm_button2_width, confirm_button2_height, confirm_button2__img)
        self.components["confirm_button2"] = confirm_button2

    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["roomID"] = self.input_data["roomID"]
            self.output_data["username"] = self.input_data["username"]
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["custom_quiz_selection"] = self.input_data["custom_quiz_selection"]
            self.output_data["custom_question_selection"] = self.input_data["custom_question_selection"]
            self.output_data["toggled"] = self.input_data["toggled"]
            self.output_data["selected_question"] = self.input_data["selected_question"]

            if triggered_component in [self.components["confirm_button2"]]:
                self.output_data["description"] = self.components["question_input_box"].input
                self.output_data["difficulty_level"] = self.components["difficulty_input_box"].input

                if self.components["correct_option"].button.text == "A":
                    self.output_data["correct_option"] = self.components["option1_input_box"].input
                    self.output_data["wrong1"], self.output_data["wrong2"], self.output_data["wrong3"] = self.components["option2_input_box"].input, self.components["option3_input_box"].input, self.components["option4_input_box"].input
                elif self.components["correct_option"].button.text == "B":
                    self.output_data["correct_option"] = self.components["option2_input_box"].input
                    self.output_data["wrong1"], self.output_data["wrong2"], self.output_data["wrong3"] = self.components["option1_input_box"].input, self.components["option3_input_box"].input, self.components["option4_input_box"].input
                elif self.components["correct_option"].button.text == "C":
                    self.output_data["correct_option"] = self.components["option3_input_box"].input
                    self.output_data["wrong1"], self.output_data["wrong2"], self.output_data["wrong3"] = self.components["option1_input_box"].input, self.components["option2_input_box"].input, self.components["option4_input_box"].input
                elif self.components["correct_option"].button.text == "D":
                    self.output_data["correct_option"] = self.components["option4_input_box"].input
                    self.output_data["wrong1"], self.output_data["wrong2"], self.output_data["wrong3"] = self.components["option1_input_box"].input, self.components["option2_input_box"].input, self.components["option3_input_box"].input

                question = {
                    "Description": self.output_data["description"],
                    "Difficulty_level": int(self.output_data["difficulty_level"]),
                    "Correct": self.output_data["correct_option"],
                    "Wrong_1": self.output_data["wrong1"],
                    "Wrong_2": self.output_data["wrong2"],
                    "Wrong_3": self.output_data["wrong3"],
                    "question_id": str(uuid.uuid4())
                }
                QuestionManager.add_custom_questions(self.output_data["roomID"],
                                                     self.output_data["custom_quiz_selection"], [question])
                self.name = "question_select"
            if triggered_component in [self.components["return_button2"]]:
                print("go back to question select")
                self.name = "question_select"
