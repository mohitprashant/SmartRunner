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
            "custom_quiz_selection":"",
            "back_navigation": "",
            "toggled":"",
            "mode_toggle": ""
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "room_ID": "",
            "username": "",
            "gametypeselection": "",
            "custom_quiz_selection": "",
            "back_navigation":"",
            "exit": False
        }


    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/Backgrounds/settingsbg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # toggle test
        toggle_rel_x = 9/20
        toggle_rel_y = 0.06
        toggle_rel_width = 1 / 11
        toggle_rel_height = 1 / 11
        toggle_image = pygame.image.load('assets/Buttons/btn_togglenotpressed.png')
        toggle_image2 = pygame.image.load('assets/Buttons/btn_togglepressed.png')
        toggle = ToggleButton("toggle", screen, toggle_rel_x, toggle_rel_y, toggle_rel_width, toggle_rel_height,
                              toggle_image, toggle_image2, self.input_data["toggled"])
        self.components["toggle"] = toggle


        # Player Score display
        JoinAsHost_display_x = 2 / 20
        JoinAsHost_display_y = 2 / 40
        JoinAsHost_display_width = 1 / 3
        JoinAsHost_display_height = 1 / 7
        JoinAsHost_text = pygame.image.load('assets/Backgrounds/joinhost.png')
        JoinAsHost_display = ImageDisplay("JoinAsHost_display", screen, JoinAsHost_display_x,
                                             JoinAsHost_display_y, JoinAsHost_display_width,
                                             JoinAsHost_display_height, JoinAsHost_text)
        self.components["JoinAsHost_display"] = JoinAsHost_display

        mode_toggle_rel_x = 0.44
        mode_toggle_rel_y = 11 / 40
        mode_toggle_rel_width = 3 / 10
        mode_toggle_rel_height = 0.23
        mode_toggle_image = pygame.image.load('assets/Backgrounds/globalquestions.png')
        mode_toggle_image2 = pygame.image.load('assets/Backgrounds/fromcustomquiz.png')
        mode_toggle = ToggleButton("mode_toggle", screen, mode_toggle_rel_x, mode_toggle_rel_y, mode_toggle_rel_width, mode_toggle_rel_height,
                              mode_toggle_image, mode_toggle_image2,self.input_data["mode_toggle"])
        self.components["mode_toggle"] = mode_toggle

        # Player Score display
        Mode_display_x = 0.22
        Mode_display_y = 14 / 40
        Mode_display_width = 2/10
        Mode_display_height = 1 / 7
        Mode_text =  pygame.image.load('assets/Backgrounds/mode.png')
        Mode_display = ImageDisplay("Mode_display", screen, Mode_display_x,
                                         Mode_display_y, Mode_display_width,
                                         Mode_display_height, Mode_text)
        self.components["Mode_display"] = Mode_display

        if self.input_data["mode_toggle"] == True:
            self.output_data["gametypeselection"] = "Custom Quiz"
            print("Custom Quiz_component")
            # room ID image
            custom_quiz_image_rel_x = 9 / 20
            custom_quiz_image_rel_y = 4/8
            custom_quiz_image_rel_width = 0.3
            custom_quiz_image_rel_height = 1 / 10
            custom_quiz_img = pygame.image.load('assets/Buttons/btn_plain.png')
            custom_quiz_image = ImageDisplay("custom_quiz_image", screen, custom_quiz_image_rel_x,
                                                   custom_quiz_image_rel_y,
                                                   custom_quiz_image_rel_width,
                                                   custom_quiz_image_rel_height, custom_quiz_img)
            self.components["custom_quiz_image"] = custom_quiz_image

            #If Clicked on add new qn, go to a different screen
            custom_quiz_button_x = 0.47
            custom_quiz_button_y = 0.52
            custom_quiz_button_width = 0.28
            custom_quiz_button_height = 1 / 11
            custom_quiz_text = self.input_data["custom_quiz_selection"]
            custom_quiz_button = TextButton("custom_quiz_button", screen, custom_quiz_button_x,
                                                     custom_quiz_button_y,
                                                     custom_quiz_button_width,
                                                     custom_quiz_button_height, custom_quiz_text)
            self.components["custom_quiz_button"] = custom_quiz_button

        # return button
        return_button_x = 1/15
        return_button_y = 4/5
        return_button_width = 1 / 7
        return_button_height = 1 / 7
        return_button__img = pygame.image.load('assets/Buttons/btn_back.png')
        return_button = ImageButton("return_button", screen, return_button_x, return_button_y,
                                    return_button_width,
                                    return_button_height, return_button__img)
        self.components["return_button"] = return_button


        # each button should link to a new screen
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["back_navigation"]=self.output_data["prev_page"]
            # print("back nav", self.output_data["back_navigation"])
            self.output_data["roomID"] = self.input_data["roomID"]
            self.output_data["username"] = self.input_data["username"]
            if self.input_data["mode_toggle"] == True:
                if triggered_component in [self.components["custom_quiz_button"]]:
                    self.name = "custom_select"
            if triggered_component in [self.components["mode_toggle"]]:
                if triggered_component.toggled:
                    self.input_data["mode_toggle"] = True
                    self.output_data["gametypeselection"]="Custom Quiz"
                    pygame.display.flip()
                    print("Custom Quiz")
                else:
                    self.input_data["mode_toggle"] = False
                    self.output_data["gametypeselection"]="Global Questions"
                    pygame.display.flip()
                    print("Global Questions")
            if triggered_component in [self.components["return_button"]]:
                if self.input_data["back_navigation"] == "hostroom":
                    if self.output_data["gametypeselection"] == "Custom Quiz":
                        print("Use Custom Questions")
                        self.output_data["custom_quiz_selection"]= self.input_data["custom_quiz_selection"]
                    else:
                        # self.output_data["custom_quiz_selection"]= self.input_data["custom_quiz_selection"]
                        print("Use Global Questions")
                    self.name ="hostroom"

            if triggered_component in [self.components["toggle"]]:
                print("hello")
                if triggered_component.toggled:
                    # self.output_data["toggle_password"] = True
                    self.input_data["toggled"] = True
                    print("Join room as host")
                else:
                    self.input_data["toggled"] = False
                    print("False")

