from assets.components import *
from page import *


class PlayerRoomPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "playerroom"
        self.input_data = {
            "player_status": [],
            "roomID": ""
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "roomID": "",
            "ready_status": False,
            "exit": False
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
        text_list = self.input_data["player_status"]

        selectable_text_list = SelectableTextList("selectable_text_list", screen, relative_x,
                                                  relative_y, relative_width,
                                                  text_relative_height, shown_relative_width, shown_relative_height,
                                                  text_list, screen, single_select=True, active_color="white")
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

        # room ID button
        roomID_button_rel_x = 0.8
        roomID_button_rel_y = 1 / 15
        roomID_button_rel_width = 1 / 7
        roomID_button_rel_height = 1 / 7
        text = self.input_data["roomID"]
        roomID_button = TextButton("roomID_button", screen, roomID_button_rel_x, roomID_button_rel_y,
                                   roomID_button_rel_width,
                                   roomID_button_rel_height, text)
        self.components["roomID_button"] = roomID_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            if triggered_component in [self.components["exit_button"]]:
                self.name = "join_room"
            if triggered_component in [self.components["start_button"]]:
                self.output_data["ready_status"] = True
                print("Player ready")
            if triggered_component in [self.components["roomID_button"]]:
                self.name = "share"
