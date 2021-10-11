from assets.components import *
from page import *


class JoinRoomPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "join_room"
        self.input_data = {
            "username": "",
            # "roomID": "",
            # "room_password": ""
        }
        self.output_data = {
            "current_page": self.name,
            "username": self.input_data["username"],
            "roomID": "",
            "room_password": "",
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/img/sky.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background


        # picture display - sun to be replaced with a game image
        game_image_rel_x = 1 / 10
        game_image_rel_y = 1 / 2
        game_image_rel_width = 1 / 3
        game_image_rel_height = 1 / 5
        game_image_img = pygame.image.load('assets/img/sun.png')
        game_image_box = ImageDisplay("game_image_box", screen, game_image_rel_x, game_image_rel_y,
                                       game_image_rel_width, game_image_rel_height,game_image_img)
        self.components["game_image_box"] = game_image_box

        # confirm roomid and password
        room_confirm_button_rel_x = 7 / 10
        room_confirm_button_rel_y = 3 / 4
        room_confirm_button_rel_width = 1 / 8
        room_confirm_button_rel_height = 1 / 8
        room_confirm_button_img = pygame.image.load('assets/img/start_btn.png')
        room_confirm_button = ImageButton("room_confirm_button", screen, room_confirm_button_rel_x, room_confirm_button_rel_y,
                                   room_confirm_button_rel_width,
                                   room_confirm_button_rel_height, room_confirm_button_img)
        self.components["room_confirm_button"] = room_confirm_button


        # go back
        back_button_rel_x = 41 / 80
        back_button_rel_y = 3 / 4
        back_button_rel_width = 1 / 8
        back_button_rel_height = 1 / 8
        back_button_img = pygame.image.load('assets/img/start_btn.png')
        back_button = ImageButton("back_button", screen, back_button_rel_x, back_button_rel_y,
                                        back_button_rel_width,
                                        back_button_rel_height, back_button_img)
        self.components["back_button"] = back_button

        # room ID text input box
        roomID_input_rel_x = 1 / 2
        roomID_input_rel_y = 1 / 2
        roomID_input_rel_width = 1 / 3
        roomID_input_rel_height = 1 / 16
        roomID_input_box = TextInput("roomID_input_box", screen, roomID_input_rel_x, roomID_input_rel_y,
                                     roomID_input_rel_width, roomID_input_rel_height)
        self.components["roomID_input_box"] = roomID_input_box

        # password text input box
        password_input_rel_x = 1 / 2
        password_input_rel_y = 3 / 5
        password_input_rel_width = 1 / 3
        password_input_rel_height = 1 / 16
        password_input_box = TextInput("password_input_box", screen, password_input_rel_x, password_input_rel_y,
                                     password_input_rel_width, password_input_rel_height)
        self.components["password_input_box"] = password_input_box

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            if triggered_component in [self.components["room_confirm_button"]]:
                self.output_data["roomID"] = self.components["roomID_input_box"].input
                self.output_data["room_password"] = self.components["password_input_box"].input
                print("input value")
                self.name = "hostroom"
            elif triggered_component in [self.components["back_button"]]:
                self.name = "room_tab"
            else:
                print("login failed")

            #
            # if triggered_component in ["room_confirm_button", "roomID_input_box", "password_input_box"]:
            #     self.data["roomID"] = self.components["roomID_input_box"].input
            #     self.data["password"] = self.components["password_input_box"].input
            #     # using placeholder for now
            #     if self.data["roomID"] == "1234" and self.data["password"] == "hello":
            #         return self.data
            #     else:
            #         print("entry failed")