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
            "room_password": ""
        }
        self.output_data = {
            "current_page": self.name,
            "room_ID": self.input_data["roomID"],
            "username": self.input_data["username"],
            "room_password": self.input_data["room_password"],
            "Toggle_Host": "",
            "exit": False
        }


    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/img/sky.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        #Join as Host Toggle
        JoinAsHost_toggle_x = 9 / 20
        JoinAsHost_toggle_y = 1 / 20
        JoinAsHost_toggle_width = 1 / 10
        JoinAsHost_toggle_height = 1 / 10
        JoinAsHost_toggle_img = pygame.image.load('assets/img/start_btn.png')
        JoinAsHost_toggle_img2 = pygame.image.load('assets/img/exit_btn.png')
        JoinAsHost_toggle = ToggleButton("JoinAsHost_toggle", screen, JoinAsHost_toggle_x, JoinAsHost_toggle_y,
                                         JoinAsHost_toggle_width,
                                         JoinAsHost_toggle_height, JoinAsHost_toggle_img, JoinAsHost_toggle_img2)
        self.components["JoinAsHost_toggle"] = JoinAsHost_toggle
        # print("toggle")

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
        global_question_button_x = 5 / 20
        global_question_button_y = 7 / 16
        global_question_button_width = 1 / 2
        global_question_button_height = 1 / 8
        global_question_text = "From database"
        global_question_button = TextboxButton("global_question_button", screen, global_question_button_x, global_question_button_y,
                                       global_question_button_width,
                                       global_question_button_height, global_question_text)
        self.components["global_question_button"] = global_question_button

        # Custom Quiz Dropdown
        # need to change to dropdown
        #If Clicked on add new qn, go to a different screen
        custom_quiz_button_x = 5 / 20
        custom_quiz_button_y = 5 / 8
        custom_quiz_button_width = 1 / 2
        custom_quiz_button_height = 1 / 8
        custom_quiz_text = "Custom Questions"
        custom_quiz_button = TextboxButton("custom_quiz_button", screen, custom_quiz_button_x,
                                                 custom_quiz_button_y,
                                                 custom_quiz_button_width,
                                                 custom_quiz_button_height, custom_quiz_text)
        self.components["custom_quiz_button"] = custom_quiz_button


        # return button
        return_button_x = 1 / 20
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
            if triggered_component in [self.components["global_question_button"]]:
                self.name = "singleplayer"
            if triggered_component in [self.components["custom_quiz_button"]]:
                self.name = "custom_select"
            if triggered_component in [self.components["return_button"]]:
                self.name = "hostroom"
            # if triggered_component in [self.components["JoinAsHost_toggle"]]:
            #     self.output_data["Toggle_Host"] = self.components["JoinAsHost_toggle"].input
            #     self.name = "hostroom"

    # # go button
        # go_button_x = 12 / 20
        # go_button_y = 41 / 64
        # go_button_width = 1 / 10
        # go_button_height = 1 / 10
        # go_button__img = pygame.image.load('assets/img/exit_btn.png')
        # go_button = ImageButton("go_button", screen, go_button_x, go_button_y,
        #                             go_button_width,
        #                             go_button_height, go_button__img)
        # self.components["go_button"] = go_button

