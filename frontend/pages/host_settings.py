import pygame
from assets.components import *
from page import *


class HostSettingsPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "host_settings"
        self.input_data = {
            "roomID": "",
            "username": "",
            "custom_quiz_selection":""
            # "room_password": ""
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "room_ID": "",
            "username": "",
            # "room_password": "",
            "Toggle_Host": False,
            "gametypeselection": "",
            "custom_quiz_selection": "",
            "exit": False
        }


    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/img/sky.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # toggle test
        toggle_rel_x = 9/20
        toggle_rel_y = 1/20
        toggle_rel_width = 1 / 10
        toggle_rel_height = 1 / 10
        toggle_image = pygame.image.load('assets/img/save_btn.png')
        toggle_image2 = pygame.image.load('assets/img/load_btn.png')
        toggle = ToggleButton("toggle", screen, toggle_rel_x, toggle_rel_y, toggle_rel_width, toggle_rel_height,
                              toggle_image, toggle_image2)
        self.components["toggle"] = toggle


        # Player Score display
        JoinAsHost_display_x = 1 / 20
        JoinAsHost_display_y = 3 / 40
        JoinAsHost_display_width = 1 / 3
        JoinAsHost_display_height = 1 / 3
        JoinAsHost_text = "Join game as a Host"
        JoinAsHost_display = TextDisplay("JoinAsHost_display", screen, JoinAsHost_display_x,
                                             JoinAsHost_display_y, JoinAsHost_display_width,
                                             JoinAsHost_display_height, JoinAsHost_text)
        self.components["JoinAsHost_display"] = JoinAsHost_display

        mode_toggle_rel_x = 9 / 20
        mode_toggle_rel_y = 15 / 40
        mode_toggle_rel_width = 3 / 10
        mode_toggle_rel_height = 1 / 10
        mode_toggle_image = pygame.image.load('assets/img/save_btn.png')
        mode_toggle_image2 = pygame.image.load('assets/img/load_btn.png')
        mode_toggle = ToggleButton("mode_toggle", screen, mode_toggle_rel_x, mode_toggle_rel_y, mode_toggle_rel_width, mode_toggle_rel_height,
                              mode_toggle_image, mode_toggle_image2)
        self.components["mode_toggle"] = mode_toggle

        # Player Score display
        Mode_display_x = 3 / 20
        Mode_display_y = 15 / 40
        Mode_display_width = 1 / 5
        Mode_display_height = 1 / 3
        Mode_text = "Mode: "
        Mode_display = TextDisplay("Mode_display", screen, Mode_display_x,
                                         Mode_display_y, Mode_display_width,
                                         Mode_display_height, Mode_text)
        self.components["Mode_display"] = Mode_display

        # # Subject dropdown
        # #need to change to dropdown
        # subject_dropdown_x = 1 / 20
        # subject_dropdown_y = 1 / 4
        # subject_dropdown_width = 1 / 4
        # subject_dropdown_height = 1 / 8
        # subject_dropdown_img = pygame.image.load('assets/img/restart_btn.png')
        # subject_dropdown = ImageButton("subject_dropdown", screen, subject_dropdown_x, subject_dropdown_y,
        #                                  subject_dropdown_width,
        #                                  subject_dropdown_height, subject_dropdown_img)
        # self.components["subject_dropdown"] = subject_dropdown
        #
        # # Topic room button
        # #need to change to dropdown
        # topic_dropdown_x = 7 / 20
        # topic_dropdown_y = 1 / 4
        # topic_dropdown_width = 1 / 4
        # topic_dropdown_height = 1 / 8
        # topic_dropdown_img = pygame.image.load('assets/img/load_btn.png')
        # topic_dropdown = ImageButton("topic_dropdown", screen, topic_dropdown_x, topic_dropdown_y,
        #                                topic_dropdown_width,
        #                                topic_dropdown_height, topic_dropdown_img)
        # self.components["topic_dropdown"] = topic_dropdown
        #
        # # Difficulty button
        # #need to change to dropdown
        # difficulty_dropdown_x = 13 / 20
        # difficulty_dropdown_y = 1 / 4
        # difficulty_dropdown_width = 1 / 4
        # difficulty_dropdown_height = 1 / 8
        # difficulty_dropdown_img = pygame.image.load('assets/img/exit_btn.png')
        # difficulty_dropdown_button = ImageButton("difficulty_dropdown_button", screen, difficulty_dropdown_x, difficulty_dropdown_y,
        #                                  difficulty_dropdown_width,
        #                                  difficulty_dropdown_height, difficulty_dropdown_img)
        # self.components["difficulty_dropdown_button"] = difficulty_dropdown_button

        # global qns button
        # global_question_button_x = 5 / 20
        # global_question_button_y = 7 / 16
        # global_question_button_width = 0.55
        # global_question_button_height = 1 / 8
        # global_question_text = "From database"
        # global_question_button = TextboxButton("global_question_button", screen, global_question_button_x, global_question_button_y,
        #                                global_question_button_width,
        #                                global_question_button_height, global_question_text)
        # self.components["global_question_button"] = global_question_button

        # Custom Quiz Dropdown
        # need to change to dropdown
        #If Clicked on add new qn, go to a different screen
        custom_quiz_button_x = 9 / 20
        custom_quiz_button_y = 4 / 8
        custom_quiz_button_width = 0.3
        custom_quiz_button_height = 1 / 10
        custom_quiz_text = self.input_data["custom_quiz_selection"]
        custom_quiz_button = TextboxButton("custom_quiz_button", screen, custom_quiz_button_x,
                                                 custom_quiz_button_y,
                                                 custom_quiz_button_width,
                                                 custom_quiz_button_height, custom_quiz_text)
        self.components["custom_quiz_button"] = custom_quiz_button


        # return button
        return_button_x = 17 / 20
        return_button_y = 17 / 20
        return_button_width = 1 / 10
        return_button_height = 1 / 10
        return_button__img = pygame.image.load('assets/img/exit_btn.png')
        return_button = ImageButton("return_button", screen, return_button_x, return_button_y,
                                    return_button_width,
                                    return_button_height, return_button__img)
        self.components["return_button"] = return_button

        # confirm button
        # confirm_button_x = 17 / 20
        # confirm_button_y = 17 / 20
        # confirm_button_width = 1 / 10
        # confirm_button_height = 1 / 10
        # confirm_button__img = pygame.image.load('assets/img/save_btn.png')
        # confirm_button = ImageButton("confirm_button", screen, confirm_button_x, confirm_button_y,
        #                             confirm_button_width,
        #                             confirm_button_height, confirm_button__img)
        # self.components["confirm_button"] = confirm_button

        # how do the page react to events?
        # each button should link to a new screen
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["roomID"] = self.input_data["roomID"]
            self.output_data["username"] = self.input_data["username"]
            self.output_data["prev_page"] = self.output_data["current_page"]
            if triggered_component in [self.components["mode_toggle"]]:
                if triggered_component.toggled:
                    self.output_data["gametypeselection"] = "custom_questions"
                    self.output_data["Toggle_Host"] = True
                else:
                    self.output_data["gametypeselection"]="global_questions"
            if triggered_component in [self.components["custom_quiz_button"]]:
                # self.output_data["gametypeselection"]="custom_questions"
                self.name = "custom_select"
            if triggered_component in [self.components["return_button"]]:
                # self.output_data["custom_quiz_selection"] = self.input_data["custom_quiz_selection"]
                self.name = "hostroom"
            if triggered_component in [self.components["toggle"]]:
                print("hello")
                if triggered_component.toggled:
                    self.output_data["Toggle_Host"] = True
                    print("True")
