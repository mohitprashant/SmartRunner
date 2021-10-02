from assets.components import *
from page import *


class PlayerRoomPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "playerroom"
        self.data = {
            "current_page": self.name,
            "roomID": "Room ID",
            "ready_status": False,
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/img/sky.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background


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
        roomID_button_rel_x = 11 / 15
        roomID_button_rel_y = 1 / 15
        roomID_button_rel_width = 1 / 7
        roomID_button_rel_height = 1 / 7
        roomID_button = TextButton("roomID_button", screen, roomID_button_rel_x, roomID_button_rel_y,
                                      roomID_button_rel_width,
                                      roomID_button_rel_height, self.data["roomID"])
        self.components["roomID_button"] = roomID_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            if triggered_component in ["exit_button"]:
                print("return to join room")
            if triggered_component in ["start_button"]:
                self.data["ready_status"] = True
                print("Player ready")
            if triggered_component in ["roomID_button"]:
                print("navigate to share screen")
