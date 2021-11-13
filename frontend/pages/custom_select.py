import pygame
from assets.components import *
from page import *
import sys
sys.path.insert(1, '../../backend/database')
import RoomManager


class CustomSelectPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "custom_select"
        self.input_data = {
            "roomID": "",
            "username": "",
            "toggled": "",
            "custom_quiz_selection": "",
            "custom_quizzes": ""
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "room_ID": "",
            "username": "",
            "toggled": "",
            "custom_quiz_selection":"",
            "exit": False
        }



    def set_components(self, screen):
        self.name = "custom_select"

        # change back navigation every time page changes
        if self.input_data["prev_page"] != self.name:
            self.output_data["back_navigation"] = self.input_data["prev_page"]

        # background
        bg_img = pygame.image.load('assets/Backgrounds/settingsbg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background


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
        # analytics list image

        list_image_rel_x = 0.095
        list_image_rel_y = 0.15
        list_image_rel_width = 0.8
        list_image_rel_height = 0.7
        list_img = pygame.image.load('assets/Backgrounds/scrollable.png')
        customselectlist_image = ImageDisplay("customselectlist_image", screen, list_image_rel_x, list_image_rel_y,
                                           list_image_rel_width,
                                           list_image_rel_height, list_img)
        self.components["customselectlist_image"] = customselectlist_image

        # relative_x = 0.2
        # relative_y = 0.25
        # relative_width = 0.55
        # text_relative_height = 0.1
        # shown_relative_width = 0.55
        # shown_relative_height = 0.45
        # text_list = self.input_data["custom_quizzes"]
        # textbox_button_list = TextboxButtonList("textbox_button_list", screen, relative_x,
        #                                         relative_y, relative_width,
        #                                         text_relative_height, shown_relative_width, shown_relative_height,
        #                                         text_list, screen)
        # self.components["textbox_button_list"] = textbox_button_list
        # self.layers.append(textbox_button_list)

        # SelectableTextList
        relative_x = 0.2
        relative_y = 0.25
        relative_width = 0.55
        text_relative_height = 0.1
        shown_relative_width = 0.55
        shown_relative_height = 0.5
        custom_quizzes = self.input_data["custom_quizzes"]

        custom_quizzes = SelectableTextList("custom_quizzes", screen, relative_x,
                                                   relative_y, relative_width,
                                                   text_relative_height, shown_relative_width, shown_relative_height,
                                                   custom_quizzes, screen, single_select=True, active_color="blue")

        self.components["custom_quizzes"] = custom_quizzes
        #custom_questions_whole.add_component(custom_questions)
        self.layers.append(custom_quizzes)

        custom_quiz_display_x = 6 / 20
        custom_quiz_display_y = 0.07
        custom_quiz_display_width = 1 / 3
        custom_quiz_display_height = 0.15
        custom_quiz_text = pygame.image.load('assets/Backgrounds/customquizzes.png')
        custom_quiz_display = ImageDisplay("custom_quiz_display", screen, custom_quiz_display_x,
                                           custom_quiz_display_y, custom_quiz_display_width,
                                           custom_quiz_display_height, custom_quiz_text)
        self.components["custom_quiz_display"] = custom_quiz_display

        # confirm and go back button
        confirm_button_x = 0.4
        confirm_button_y = 17 / 20
        confirm_button_width = 1 / 7
        confirm_button_height = 1 / 8
        confirm_button_img = pygame.image.load('assets/Buttons/btn_confirm.png')
        confirm_button = ImageButton("confirm_button", screen, confirm_button_x, confirm_button_y,
                                    confirm_button_width,
                                    confirm_button_height, confirm_button_img)
        self.components["confirm_button"] = confirm_button

        # edit quiz button
        edit_quiz_button_x = 0.83
        edit_quiz_button_y = 0.35
        edit_quiz_button_width = 0.1
        edit_quiz_button_height = 0.1
        edit_quiz_button_img = pygame.image.load('assets/Buttons/btn_twitter.png')
        edit_quiz_button = ImageButton("edit_quiz_button", screen, edit_quiz_button_x, edit_quiz_button_y,
                                      edit_quiz_button_width,
                                      edit_quiz_button_height, edit_quiz_button_img)
        self.components["edit_quiz_button"] = edit_quiz_button

        # add quiz button
        add_quiz_button_x = 0.83
        add_quiz_button_y = 0.5
        add_quiz_button_width = 0.1
        add_quiz_button2_height = 0.1
        add_quiz_button_img = pygame.image.load('assets/Buttons/btn_add.png')
        add_quiz_button = ImageButton("add_quiz_button", screen, add_quiz_button_x, add_quiz_button_y,
                                      add_quiz_button_width,
                                      add_quiz_button2_height, add_quiz_button_img)
        self.components["add_quiz_button"] = add_quiz_button

        delete_quiz_button_x = 0.83
        delete_quiz_button_y = 0.65
        delete_quiz_button_width = 1 / 10
        delete_quiz_button_height = 1 / 10
        delete_quiz_button_img = pygame.image.load('assets/Buttons/btn_deleteqn.png')
        delete_quiz_button = ImageButton("delete_quiz_button", screen, delete_quiz_button_x,
                                              delete_quiz_button_y,
                                              delete_quiz_button_width,
                                              delete_quiz_button_height, delete_quiz_button_img)
        self.components["delete_quiz_button"] = delete_quiz_button


        # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["roomID"] = self.input_data["roomID"]
            self.output_data["username"] = self.input_data["username"]
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["toggled"] = self.input_data["toggled"]
            self.output_data["custom_quiz_selection"] = self.input_data["custom_quiz_selection"]
            self.output_data["selected_question"] = ""
            self.output_data["mode_toggle"] = True
            if triggered_component in [self.components["custom_quizzes"]]:
                self.input_data["custom_quiz_selection"] = triggered_component.selected_text
                # if self.input_data["retrieve_id"][triggered_component.selected_text[0]]!= "Nobody's here!":
                if self.input_data["custom_quiz_selection"] != "Nobody's here!":
                    self.output_data["custom_quiz_selection"] = self.input_data["custom_quiz_selection"]
                    self.name = "question_select"
                else:
                    self.output_data["custom_quiz_selection"] = ""
                    self.name = "custom_select"
            if triggered_component in [self.components["confirm_button"]]:
                self.name = "host_settings"
            if triggered_component in [self.components["add_quiz_button"]]:
                self.input_data["custom_quiz_selection"] = "New Quiz"
                self.output_data["custom_quiz_selection"] = self.input_data["custom_quiz_selection"]
                self.name = "question_select"
            if triggered_component in [self.components["edit_quiz_button"]]:
                print("go question select")
                self.name = "question_select"
            if triggered_component in [self.components["delete_quiz_button"]]:
                # QuestionManager.delete_custom_question(self.output_data["username"], self.output_data["roomID"],self.output_data["custom_quiz_selection"],self.output_data["custom_question_selection"])
                print("delete quiz", self.output_data["custom_quiz_selection"], "from database")