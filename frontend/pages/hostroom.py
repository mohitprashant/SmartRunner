from assets.components import *
from page import *


class HostRoomPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "hostroom"
        self.input_data = {
            "player_status": [],
            "roomID": "",
            "username":""
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "roomID": "",
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        self.name = "hostroom"

        # change back navigation every time page changes
        if self.input_data["prev_page"] != self.name:
            self.output_data["back_navigation"] = self.input_data["prev_page"]

        # background
        bg_img = pygame.image.load('assets/Backgrounds/roombg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # player list image
        list_image_rel_x = 0.045
        list_image_rel_y = 0.1
        list_image_rel_width = 0.8
        list_image_rel_height = 0.7
        list_img = pygame.image.load('assets/Backgrounds/scrollable.png')
        playerlist_image = ImageDisplay("playerlist_image", screen, list_image_rel_x, list_image_rel_y,
                                    list_image_rel_width,
                                    list_image_rel_height, list_img)
        self.components["playerlist_image"] = playerlist_image

        # player list
        relative_x = 0.15
        relative_y = 0.2
        relative_width = 0.55
        text_relative_height = 0.1
        shown_relative_width = 0.55
        shown_relative_height = 0.5
        text_list = self.input_data["player_status"]

        selectable_text_list = SelectableTextList("selectable_text_list", screen, relative_x,
                                                  relative_y, relative_width,
                                                  text_relative_height, shown_relative_width, shown_relative_height,
                                                  text_list, screen, single_select=True, active_color="white")
        self.components["selectable_text_list"] = selectable_text_list
        #self.layers.append(selectable_text_list)

        # player status header
        header_image_rel_x = 0.22
        header_image_rel_y = 0.02
        header_image_rel_width = 0.4
        header_image_rel_height = 0.15
        header_img = pygame.image.load('assets/Backgrounds/playerstatus.png')
        playerheader_image = ImageDisplay("playerheader_image", screen, header_image_rel_x, header_image_rel_y,
                                          header_image_rel_width,
                                          header_image_rel_height, header_img)
        self.components["playerheader_image"] = playerheader_image

        # exit button
        exit_button_rel_x = 1 / 15
        exit_button_rel_y = 4 / 5
        exit_button_rel_width = 1 / 7
        exit_button_rel_height = 1 / 7
        exit_button_img = pygame.image.load('assets/Buttons/btn_back.png')
        exit_button = ImageButton("exit_button", screen, exit_button_rel_x, exit_button_rel_y,
                                   exit_button_rel_width,
                                   exit_button_rel_height, exit_button_img)
        self.components["exit_button"] = exit_button

        # start button
        start_button_rel_x = 3 / 7
        start_button_rel_y = 4 / 5
        start_button_rel_width = 1 / 7
        start_button_rel_height = 1 / 7
        start_button_img = pygame.image.load('assets/Buttons/btn_start.png')
        start_button = ImageButton("start_button", screen, start_button_rel_x, start_button_rel_y,
                                   start_button_rel_width,
                                   start_button_rel_height, start_button_img)
        self.components["start_button"] = start_button


        # analytics button
        analytics_button_rel_x = 0.8
        analytics_button_rel_y = 3 / 5
        analytics_button_rel_width = 0.15
        analytics_button_rel_height = 1 / 7
        analytics_button_img = pygame.image.load('assets/Buttons/btn_analytics.png')
        analytics_button = ImageButton("analytics_button", screen, analytics_button_rel_x, analytics_button_rel_y,
                                     analytics_button_rel_width,
                                     analytics_button_rel_height, analytics_button_img)
        self.components["analytics_button"] = analytics_button

        # settings button
        settings_button_rel_x = 0.7
        settings_button_rel_y = 4 / 5
        settings_button_rel_width = 0.25
        settings_button_rel_height = 1 / 7
        settings_button_img = pygame.image.load('assets/Buttons/btn_hostsettings.png')
        settings_button = ImageButton("settings_button", screen, settings_button_rel_x, settings_button_rel_y,
                                       settings_button_rel_width,
                                       settings_button_rel_height, settings_button_img)
        self.components["settings_button"] = settings_button

        # room ID image
        roomID_image_rel_x = 0.78
        roomID_image_rel_y = 0.03
        roomID_image_rel_width = 0.17
        roomID_image_rel_height = 1 / 7
        btn_img = pygame.image.load('assets/Buttons/btn_plain.png')
        roomID_image = ImageDisplay("roomID_image", screen, roomID_image_rel_x, roomID_image_rel_y,
                                    roomID_image_rel_width,
                                    roomID_image_rel_height, btn_img)
        self.components["roomID_image"] = roomID_image

        # room ID button
        roomID_button_rel_x = 0.8
        roomID_button_rel_y = 1 / 15
        roomID_button_rel_width = 1 / 7
        roomID_button_rel_height = 1 / 7
        text= self.input_data["roomID"]
        roomID_button = TextButton("roomID_button", screen, roomID_button_rel_x, roomID_button_rel_y,
                                      roomID_button_rel_width,
                                      roomID_button_rel_height, text)
        self.components["roomID_button"] = roomID_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["username"] = self.input_data["username"]
            self.output_data["roomID"] = self.input_data["roomID"]
            self.output_data["player_status"] = self.input_data["player_status"]
            self.output_data["mode_toggle"] = self.input_data["mode_toggle"],
            self.output_data["toggled"]= self.input_data["toggled"],
            self.output_data["custom_quiz_selection"]= self.input_data["custom_quiz_selection"]
            if triggered_component in [self.components["exit_button"]]:
                self.name = "managerooms"
            if triggered_component in [self.components["start_button"]]:
                print("navigate to game session")
                #placeholder, stay on page
                self.name = "hostroom"
            if triggered_component in [self.components["analytics_button"]]:
                self.name = "analyticsselect"
            if triggered_component in [self.components["settings_button"]]:
                self.name = "host_settings"
            if triggered_component in [self.components["roomID_button"]]:
                self.name = "share"

