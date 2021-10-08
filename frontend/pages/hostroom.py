from assets.components import *
from page import *


class HostRoomPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "hostroom"
        self.output_data = {
            "current_page": self.name,
            "exit": False
        }
        self.input_data = {
            "player_status": [],
            "roomID": "Room ID",
        }

    # set all component variables on input screen
    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/img/sky.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # text display
        relative_x = 0.22
        relative_y = 0.05
        relative_width = 0.45
        relative_height = 1 / 12
        text_display = TextDisplay("text_display", screen, relative_x, relative_y, relative_width, relative_height,
                                   "Player Status")
        self.components["text_display"] = text_display

        # player list
        relative_x = 0.05
        relative_y = 0.15
        relative_width = 0.8
        text_relative_height = 1 / 10
        shown_relative_width = 0.7
        shown_relative_height = 3 / 5
        text_list = ["1", "2", "3", "4", "5", "6", "7", "8"]

        selectable_text_list = SelectableTextList("selectable_text_list", screen, relative_x,
                                                  relative_y, relative_width,
                                                  text_relative_height, shown_relative_width, shown_relative_height,
                                                  text_list, single_select=True, active_color="white")
        self.components["selectable_text_list"] = selectable_text_list
        self.layers.append(selectable_text_list)

        # exit button
        exit_button_rel_x = 1 / 15
        exit_button_rel_y = 4 / 5
        exit_button_rel_width = 1 / 7
        exit_button_rel_height = 1 / 7
        exit_button_img = pygame.image.load('assets/img/exit_btn.png')
        exit_button = ImageButton("exit_button", screen, exit_button_rel_x, exit_button_rel_y,
                                   exit_button_rel_width,
                                   exit_button_rel_height, exit_button_img)
        self.components["exit_button"] = exit_button

        # start button
        start_button_rel_x = 3 / 7
        start_button_rel_y = 4 / 5
        start_button_rel_width = 1 / 7
        start_button_rel_height = 1 / 7
        start_button_img = pygame.image.load('assets/img/start_btn.png')
        start_button = ImageButton("start_button", screen, start_button_rel_x, start_button_rel_y,
                                   start_button_rel_width,
                                   start_button_rel_height, start_button_img)
        self.components["start_button"] = start_button

        # analytics button
        analytics_button_rel_x = 0.8
        analytics_button_rel_y = 3 / 5
        analytics_button_rel_width = 1 / 7
        analytics_button_rel_height = 1 / 7
        analytics_button_img = pygame.image.load('assets/img/blob.png')
        analytics_button = ImageButton("analytics_button", screen, analytics_button_rel_x, analytics_button_rel_y,
                                     analytics_button_rel_width,
                                     analytics_button_rel_height, analytics_button_img)
        self.components["analytics_button"] = analytics_button

        # settings button
        settings_button_rel_x = 0.8
        settings_button_rel_y = 4 / 5
        settings_button_rel_width = 1 / 7
        settings_button_rel_height = 1 / 7
        settings_button_img = pygame.image.load('assets/img/coin.png')
        settings_button = ImageButton("settings_button", screen, settings_button_rel_x, settings_button_rel_y,
                                       settings_button_rel_width,
                                       settings_button_rel_height, settings_button_img)
        self.components["settings_button"] = settings_button

        # room ID button
        roomID_button_rel_x = 0.8
        roomID_button_rel_y = 1 / 15
        roomID_button_rel_width = 1 / 7
        roomID_button_rel_height = 1 / 7
        roomID_button = TextButton("roomID_button", screen, roomID_button_rel_x, roomID_button_rel_y,
                                      roomID_button_rel_width,
                                      roomID_button_rel_height, self.input_data["roomID"])
        self.components["roomID_button"] = roomID_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            if triggered_component in [self.components["exit_button"]]:
                print("return to room selection")
            if triggered_component in [self.components["start_button"]]:
                print("navigate to game session")
            if triggered_component in [self.components["analytics_button"]]:
                print("navigate to analytics screen")
            if triggered_component in [self.components["settings_button"]]:
                print("navigate to host settings screen")
            if triggered_component in [self.components["roomID_button"]]:
                print("navigate to share screen")
            #add triggered component for scrollable single select

