from assets.components import *
from page import *
import sys
import game_play
sys.path.insert(1, '../../backend/database')
import RoomManager


class PlayerRoomPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "playerroom"
        self.input_data = {
            "player_status": [],
            "username": "",
            "roomID": ""
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "roomID": "",
            "username": "",
            "readystatus": False,
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        self.name = "playerroom"

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
                                        list_image_rel_width, list_image_rel_height, list_img)
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
        self.layers.append(selectable_text_list)

        # player status header
        header_image_rel_x = 0.22
        header_image_rel_y = 0.02
        header_image_rel_width = 0.4
        header_image_rel_height = 0.15
        header_img = pygame.image.load('assets/Backgrounds/playerstatus.png')
        playerheader_image = ImageDisplay("playerheader_image", screen, header_image_rel_x, header_image_rel_y,
                                          header_image_rel_width, header_image_rel_height, header_img)
        self.components["playerheader_image"] = playerheader_image

        # exit button
        exit_button_rel_x = 1 / 15
        exit_button_rel_y = 4 / 5
        exit_button_rel_width = 1 / 7
        exit_button_rel_height = 1 / 7
        exit_button_img = pygame.image.load('assets/Buttons/btn_back.png')
        exit_button = ImageButton("exit_button", screen, exit_button_rel_x, exit_button_rel_y,
                                  exit_button_rel_width, exit_button_rel_height, exit_button_img)
        self.components["exit_button"] = exit_button

        # start button
        start_button_rel_x = 3 / 7
        start_button_rel_y = 4 / 5
        start_button_rel_width = 1 / 7
        start_button_rel_height = 1 / 7
        start_button_img = pygame.image.load('assets/Buttons/btn_ready.png')
        start_button = ImageButton("start_button", screen, start_button_rel_x, start_button_rel_y,
                                   start_button_rel_width, start_button_rel_height, start_button_img)
        self.components["start_button"] = start_button

        # room ID image
        roomID_image_rel_x = 0.78
        roomID_image_rel_y = 0.03
        roomID_image_rel_width = 0.17
        roomID_image_rel_height = 1 / 7
        btn_img = pygame.image.load('assets/Buttons/btn_plain.png')
        roomID_image = ImageDisplay("roomID_image", screen, roomID_image_rel_x, roomID_image_rel_y,
                                    roomID_image_rel_width, roomID_image_rel_height, btn_img)
        self.components["roomID_image"] = roomID_image

        # room ID button
        roomID_button_rel_x = 0.8
        roomID_button_rel_y = 1 / 15
        roomID_button_rel_width = 1 / 7
        roomID_button_rel_height = 1 / 7
        text = self.input_data["roomID"]
        roomID_button = TextButton("roomID_button", screen, roomID_button_rel_x, roomID_button_rel_y,
                                   roomID_button_rel_width, roomID_button_rel_height, text)
        self.components["roomID_button"] = roomID_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        self.output_data["roomID"] = self.input_data["roomID"]
        self.output_data["prev_page"] = self.output_data["current_page"]
        self.output_data["username"] = self.input_data["username"]
        self.output_data["player_status"] = []
        self.output_data["mode_toggle"] = "None"
        self.output_data["toggled"] = "None"
        self.output_data["custom_quiz_selection"] = "None"
        self.output_data["playertype"] = "client"
        self.output_data["join_host"] = ""
        self.output_data["questions"] = []
        self.output_data["answers"] = []
        self.output_data["join_host"] = ""
        self.output_data["topicselection"] = ""
        self.output_data["subjectselection"] = ""
        self.output_data["ready_status"] = ""

        for triggered_component in triggered_component_list:

            if triggered_component in [self.components["exit_button"]]:
                self.name = "join_room"
            if triggered_component in [self.components["start_button"]]:
                if self.output_data["readystatus"]:
                    self.output_data["readystatus"] = False
                    RoomManager.set_member_status(self.output_data["roomID"], self.output_data["username"], 0)
                else:
                    self.output_data["readystatus"] = True
                    RoomManager.set_member_status(self.output_data["roomID"], self.output_data["username"], 1)
            if triggered_component in [self.components["roomID_button"]]:
                self.name = "share"
