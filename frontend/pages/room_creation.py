from assets.components import *
from page import *


class RoomCreationPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "room_creation"
        self.input_data = {
            "username": "",
            # "roomID": "",
            # "room_password": ""
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "username": "",
            "roomID": "",
            "room_password": "",
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/Backgrounds/roombg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        roomID_image_rel_x = 0.2
        roomID_image_rel_y = 0.35
        roomID_image_rel_width = 1 / 5
        roomID_image_rel_height = 1 / 8
        roomID_image_img = pygame.image.load('assets/Backgrounds/roomid.png')
        roomID_image_box = ImageDisplay("roomID_image_box", screen, roomID_image_rel_x, roomID_image_rel_y,
                                          roomID_image_rel_width, roomID_image_rel_height, roomID_image_img)
        self.components["roomID_image_box"] = roomID_image_box

        password_image_rel_x = 0.2
        password_image_rel_y = 0.47
        password_image_rel_width = 1 / 5
        password_image_rel_height = 1 / 8
        password_image_img = pygame.image.load('assets/Backgrounds/password.png')
        password_image_box = ImageDisplay("password_image_box", screen, password_image_rel_x, password_image_rel_y,
                                          password_image_rel_width, password_image_rel_height, password_image_img)
        self.components["password_image_box"] = password_image_box

        # confirm roomid and password
        room_confirm_button_rel_x = 0.5
        room_confirm_button_rel_y = 0.6
        room_confirm_button_rel_width = 0.18
        room_confirm_button_rel_height = 1 / 7
        room_confirm_button_img = pygame.image.load('assets/Buttons/btn_createroom.png')
        room_confirm_button = ImageButton("room_confirm_button", screen, room_confirm_button_rel_x, room_confirm_button_rel_y,
                                   room_confirm_button_rel_width,
                                   room_confirm_button_rel_height, room_confirm_button_img)
        self.components["room_confirm_button"] = room_confirm_button


        # go back
        back_button_rel_x = 1/15
        back_button_rel_y = 4/5
        back_button_rel_width = 1 / 7
        back_button_rel_height = 1 / 7
        back_button_img = pygame.image.load('assets/Buttons/btn_back.png')
        back_button = ImageButton("back_button", screen, back_button_rel_x, back_button_rel_y,
                                        back_button_rel_width,
                                        back_button_rel_height, back_button_img)
        self.components["back_button"] = back_button


        # room ID text input box
        roomID_input_rel_x = 0.43
        roomID_input_rel_y = 0.36
        roomID_input_rel_width = 1 / 4
        roomID_input_rel_height = 1 / 14
        roomID_input_box = TextInput("roomID_input_box", screen, roomID_input_rel_x, roomID_input_rel_y,
                                     roomID_input_rel_width, roomID_input_rel_height)
        self.components["roomID_input_box"] = roomID_input_box

        # password text input box
        password_input_rel_x = 0.43
        password_input_rel_y = 0.49
        password_input_rel_width = 0.25
        password_input_rel_height = 1 / 14
        password_input_box = TextInput("password_input_box", screen, password_input_rel_x, password_input_rel_y,
                                     password_input_rel_width, password_input_rel_height)
        self.components["password_input_box"] = password_input_box

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["username"] = self.input_data["username"]
            if triggered_component in [self.components["room_confirm_button"]]:
                self.output_data["roomID"] = self.components["roomID_input_box"].input
                self.output_data["room_password"] = self.components["password_input_box"].input
                print("input value")
                self.name = "hostroom"
            elif triggered_component in [self.components["back_button"]]:
                self.name = "room_tab"
            else:
                print("login failed")

