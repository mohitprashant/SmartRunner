from assets.components import *
from page import *
import sys
sys.path.insert(1, '../../backend/database')
import RoomManager

class ManageRoomsPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "managerooms"
        self.input_data = {
            "username":"",
            "roomname_list": [],
            "roomid_dict":{}
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "username": "",
            "roomID": "",
            "exit": False
        }


    # set all component variables on input screen
    def set_components(self, screen):
        self.name = "managerooms"

        # change back navigation every time page changes
        if self.input_data["prev_page"] != self.name:
            self.output_data["back_navigation"] = self.input_data["prev_page"]

        # background
        bg_img = pygame.image.load('assets/Backgrounds/roombg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # room list image
        list_image_rel_x = 0.145
        list_image_rel_y = 0.1
        list_image_rel_width = 0.8
        list_image_rel_height = 0.7
        list_img = pygame.image.load('assets/Backgrounds/scrollable.png')
        roomslist_image = ImageDisplay("roomslist_image", screen, list_image_rel_x, list_image_rel_y,
                                           list_image_rel_width,
                                           list_image_rel_height, list_img)
        self.components["roomslist_image"] = roomslist_image

        # room list
        relative_x = 0.25
        relative_y = 0.2
        relative_width = 0.55
        text_relative_height = 0.1
        shown_relative_width = 0.55
        shown_relative_height = 0.5
        text_list = self.input_data["roomname_list"]

        selectable_text_list = SelectableTextList("selectable_text_list", screen, relative_x,
                                                  relative_y, relative_width,
                                                  text_relative_height, shown_relative_width, shown_relative_height,
                                                  text_list, screen, single_select=True)
        self.components["selectable_text_list"] = selectable_text_list
        self.layers.append(selectable_text_list)

        # rooms header
        header_image_rel_x = 0.38
        header_image_rel_y = 0.02
        header_image_rel_width = 0.25
        header_image_rel_height = 0.15
        header_img = pygame.image.load('assets/Backgrounds/rooms.png')
        roomheader_image = ImageDisplay("roomheader_image", screen, header_image_rel_x, header_image_rel_y,
                                             header_image_rel_width,
                                             header_image_rel_height, header_img)
        self.components["roomheader_image"] = roomheader_image

        # delete button
        delete_button_rel_x = 0.8
        delete_button_rel_y = 4 / 5
        delete_button_rel_width = 1 / 7
        delete_button_rel_height = 1 / 7
        delete_button_img = pygame.image.load('assets/Buttons/btn_delete.png')
        delete_button = ImageButton("delete_button", screen, delete_button_rel_x, delete_button_rel_y,
                                      delete_button_rel_width,
                                      delete_button_rel_height, delete_button_img)
        self.components["delete_button"] = delete_button

        # join button
        join_button_rel_x = 3 / 7
        join_button_rel_y = 4 / 5
        join_button_rel_width = 1 / 7
        join_button_rel_height = 1 / 7
        join_button_img = pygame.image.load('assets/Buttons/btn_start.png')
        join_button = ImageButton("join_button", screen, join_button_rel_x, join_button_rel_y,
                                   join_button_rel_width,
                                   join_button_rel_height, join_button_img)
        self.components["join_button"] = join_button

        # back button
        exit_button_rel_x = 1 / 15
        exit_button_rel_y = 4 / 5
        exit_button_rel_width = 1 / 7
        exit_button_rel_height = 1 / 7
        exit_button_img = pygame.image.load('assets/Buttons/btn_back.png')
        exit_button = ImageButton("exit_button", screen, exit_button_rel_x, exit_button_rel_y,
                                   exit_button_rel_width,
                                   exit_button_rel_height, exit_button_img)
        self.components["exit_button"] = exit_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["username"] = self.input_data["username"]
            self.output_data["mode_toggle"] = False
            self.output_data["toggled"] = False
            self.output_data["custom_quiz_selection"] = "Select Custom Quiz"
            self.output_data["player_status"] = []
            self.output_data["join_host"] = ""


            if triggered_component in [self.components["exit_button"]]:
                self.name = "room_tab"
            if triggered_component in [self.components["selectable_text_list"]]:
                room_name= triggered_component.selected_text
                self.output_data["roomID"]=self.input_data["roomid_dict"][room_name]
                print(self.output_data["roomID"])
            if triggered_component in [self.components["join_button"]]:
                # RoomManager.set_room_activity_status("300236", False)
                self.name = "hostroom"

            if triggered_component in [self.components["delete_button"]]:
                RoomManager.delete_room(self.output_data["username"],self.output_data["roomID"])
                print("delete room", self.output_data["roomID"], "from database")


