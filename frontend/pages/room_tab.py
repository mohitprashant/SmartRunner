import pygame
from assets.components import *
from page import *


class RoomTabPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "room_tab"
        self.input_data = {
            "username": ""
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "username": "",
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/Backgrounds/roombg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # Create a Room button
        create_room_button_x = 1 / 20
        create_room_button_y = 3/7
        create_room_button_width = 1 / 4
        create_room_button_height = 1 / 5
        create_room_button_img = pygame.image.load('assets/Buttons/btn_createroom.png')
        create_room_button = ImageButton("create_room_button", screen, create_room_button_x, create_room_button_y, create_room_button_width,
                              create_room_button_height, create_room_button_img)
        self.components["create_room_button"] = create_room_button

        # picture display - sun to be replaced with a create room image
        # create_room_image_rel_x = 1 / 20
        # create_room_image_rel_y = 3 / 7
        # create_room_rel_width = 1 / 4
        # create_room_rel_height = 1 / 5
        # create_room_img = pygame.image.load('assets/img/sun.png')
        # create_room_box = ImageDisplay("create_room_box", screen, create_room_image_rel_x, create_room_image_rel_y,
        #                                create_room_rel_width, create_room_rel_height, create_room_img)
        # self.components["create_room_box"] = create_room_box

        # Manage Room button
        manage_room_button_x = 15 / 40
        manage_room_button_y = 3/7
        manage_room_button_width = 1 / 4
        manage_room_button_height = 1 / 5
        manage_room_button__img = pygame.image.load('assets/Buttons/btn_manageroom.png')
        manage_room_button = ImageButton("manage_room_button",screen, manage_room_button_x, manage_room_button_y,
                                      manage_room_button_width,
                                      manage_room_button_height, manage_room_button__img)
        self.components["manage_room_button"] = manage_room_button

        # picture display - sun to be replaced with a manage room image
        # manage_room_rel_x = 15 / 40
        # manage_room_rel_y = 3 / 7
        # manage_room_rel_width = 1 / 4
        # manage_room_rel_height = 1 / 5
        # manage_room_img = pygame.image.load('assets/img/sun.png')
        # manage_room_box = ImageDisplay("manage_room_box", screen, manage_room_rel_x, manage_room_rel_y,
        #                               manage_room_rel_width, manage_room_rel_height, manage_room_img)
        # self.components["manage_room_box"] = manage_room_box

        # Join room button
        join_room_button_x = 7 / 10
        join_room_button_y = 3/7
        join_room_button_width = 1 / 4
        join_room_button_height = 1 / 5
        join_room_button_img = pygame.image.load('assets/Buttons/btn_joinroom.png')
        join_room_button = ImageButton("join_room_button", screen, join_room_button_x, join_room_button_y,
                             join_room_button_width,
                             join_room_button_height, join_room_button_img)
        self.components["join_room_button"] = join_room_button

        # picture display - sun to be replaced with a join room image
        # join_room_rel_x = 7 / 10
        # join_room_rel_y = 3 / 7
        # join_room_rel_width = 1 / 4
        # join_room_rel_height = 1 / 5
        # join_room_img = pygame.image.load('assets/img/sun.png')
        # join_room_box = ImageDisplay("join_room_box", screen, join_room_rel_x, join_room_rel_y,
        #                                join_room_rel_width, join_room_rel_height, join_room_img)
        # self.components["join_room_box"] = join_room_box

        # return button
        return_button_x = 17 / 20
        return_button_y = 1 / 20
        return_button_width = 1 / 10
        return_button_height = 1 / 10
        return_button__img = pygame.image.load('assets/Buttons/btn_back.png')
        return_button = ImageButton("return_button", screen, return_button_x, return_button_y,
                                    return_button_width,
                                    return_button_height, return_button__img)
        self.components["return_button"] = return_button


    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["username"] = self.input_data["username"]
            if triggered_component in [self.components["create_room_button"]]:
                self.name = "room_creation"
            elif triggered_component in [self.components["manage_room_button"]]:
                self.name = "managerooms"
            elif triggered_component in [self.components["join_room_button"]]:
                self.name = "join_room"
            elif triggered_component in [self.components["return_button"]]:
                self.name = "main_menu"
            else:
                print("entry failed")