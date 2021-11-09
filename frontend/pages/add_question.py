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
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "room_ID": "",
            "username": "",
            "question_id": "",
            "description":"",
            "difficulty_level":"", #Need to change to int
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
                                               header_image_rel_y,
                                               header_image_rel_width,
                                               header_image_rel_height, header_img)
        self.components["addquestions_header"] = addquestions_header

        question_id_image_rel_x = 0.18
        question_id_image_rel_y = 0.25
        question_id_image_rel_width = 0.2
        question_id_image_rel_height = 1 / 9
        question_id_image_img = "Question ID"
        question_id_image_box = TextDisplay("question_id_image_box", screen, question_id_image_rel_x, question_id_image_rel_y,
                                         question_id_image_rel_width, question_id_image_rel_height, question_id_image_img)
        self.components["question_id_image_box"] = question_id_image_box

        question_id_input_rel_x = 0.4
        question_id_input_rel_y = 0.23
        question_id_input_rel_width = 0.15
        question_id_input_rel_height = 1 / 12
        question_id_input_box = TextInput("question_id_input_box", screen, question_id_input_rel_x, question_id_input_rel_y,
                                       question_id_input_rel_width, question_id_input_rel_height)
        self.components["question_id_input_box"] = question_id_input_box


        question_image_rel_x = 0.18
        question_image_rel_y = 0.35
        question_image_rel_width = 0.2
        question_image_rel_height = 1 / 9
        question_image_img = "Description"
        question_image_box = TextDisplay("question_image_box", screen, question_image_rel_x, question_image_rel_y,
                                          question_image_rel_width, question_image_rel_height, question_image_img)
        self.components["question_image_box"] = question_image_box

        question_input_rel_x = 0.4
        question_input_rel_y = 0.33
        question_input_rel_width = 0.5
        question_input_rel_height = 1 / 12
        question_input_box = TextInput("question_input_box", screen, question_input_rel_x, question_input_rel_y,
                                       question_input_rel_width, question_input_rel_height)
        self.components["question_input_box"] = question_input_box


        difficulty_level_image_rel_x = 0.13
        difficulty_level_image_rel_y = 0.45
        difficulty_level_image_rel_width = 1 / 4
        difficulty_level_image_rel_height = 1 / 8
        difficulty_level_image_img = "Difficulty Level"
        difficulty_level_image_box = TextDisplay("difficulty_level_image_box", screen, difficulty_level_image_rel_x, difficulty_level_image_rel_y,
                                         difficulty_level_image_rel_width, difficulty_level_image_rel_height, difficulty_level_image_img)
        self.components["difficulty_level_image_box"] = difficulty_level_image_box

        difficulty_input_rel_x = 0.4
        difficulty_input_rel_y = 0.43
        difficulty_input_rel_width = 0.15
        difficulty_input_rel_height = 1 / 12
        difficulty_input_box = TextInput("difficulty_input_box", screen, difficulty_input_rel_x, difficulty_input_rel_y,
                                       difficulty_input_rel_width, difficulty_input_rel_height)
        self.components["difficulty_input_box"] = difficulty_input_box

        correct_image_rel_x = 0.13
        correct_image_rel_y = 0.55
        correct_image_rel_width = 1 / 4
        correct_image_rel_height = 1 / 8
        correct_image_img = "Correct Option"
        correct_image_box = TextDisplay("correct_image_box", screen, correct_image_rel_x,
                                                 correct_image_rel_y,
                                                 correct_image_rel_width, correct_image_rel_height,
                                                 correct_image_img)
        self.components["correct_image_box"] = correct_image_box

        correct_input_rel_x = 0.4
        correct_input_rel_y = 0.53
        correct_input_rel_width = 0.15
        correct_input_rel_height = 1 / 12
        correct_input_box = TextInput("correct_input_box", screen, correct_input_rel_x, correct_input_rel_y,
                                         correct_input_rel_width, correct_input_rel_height)
        self.components["correct_input_box"] = correct_input_box

        wrong_image_rel_x = 0.13
        wrong_image_rel_y = 0.65
        wrong_image_rel_width = 1 / 4
        wrong_image_rel_height = 1 / 8
        wrong_image_img = "Wrong Options"
        wrong_image_box = TextDisplay("wrong_image_box", screen, wrong_image_rel_x,
                                        wrong_image_rel_y,
                                        wrong_image_rel_width, wrong_image_rel_height,
                                        wrong_image_img)
        self.components["wrong_image_box"] = wrong_image_box

        wrong_input_rel_x = 0.4
        wrong_input_rel_y = 0.63
        wrong_input_rel_width = 0.15
        wrong_input_rel_height = 1 / 12
        wrong_input_box = TextInput("wrong_input_box", screen, wrong_input_rel_x, wrong_input_rel_y,
                                      wrong_input_rel_width, wrong_input_rel_height)
        self.components["wrong_input_box"] = wrong_input_box

        wrong2_input_rel_x = 0.57
        wrong2_input_rel_y = 0.63
        wrong2_input_rel_width = 0.15
        wrong2_input_rel_height = 1 / 12
        wrong2_input_box = TextInput("wrong2_input_box", screen, wrong2_input_rel_x, wrong2_input_rel_y,
                                    wrong2_input_rel_width, wrong2_input_rel_height)
        self.components["wrong2_input_box"] = wrong2_input_box

        wrong3_input_rel_x = 0.74
        wrong3_input_rel_y = 0.63
        wrong3_input_rel_width = 0.15
        wrong3_input_rel_height = 1 / 12
        wrong3_input_box = TextInput("wrong3_input_box", screen, wrong3_input_rel_x, wrong3_input_rel_y,
                                    wrong3_input_rel_width, wrong3_input_rel_height)
        self.components["wrong3_input_box"] = wrong3_input_box

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
                self.output_data["question_id"] = self.components["question_id_input_box"].input
                self.output_data["description"] = self.components["question_input_box"].input
                self.output_data["difficulty_level"] = self.components["difficulty_input_box"].input
                self.output_data["correct_option"] = self.components["correct_input_box"].input
                self.output_data["wrong1"] = self.components["wrong_input_box"].input
                self.output_data["wrong2"] = self.components["wrong2_input_box"].input
                self.output_data["wrong3"] = self.components["wrong3_input_box"].input
                print("question added")
            if triggered_component in [self.components["return_button2"]]:
                print("go back to question select")
                self.name = "question_select"