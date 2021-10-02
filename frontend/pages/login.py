from assets.components import *
from page import *


class LoginPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "login"
        self.data = {
            "current_page": self.name,
            "username": "",
            "password": "",
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/img/sky.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # start button
        #from top left
        start_button_rel_x = 1 / 10
        start_button_rel_y = 1 / 2

        start_button_rel_width = 1 / 3
        start_button_rel_height = 1 / 5
        start_button_img = pygame.image.load('assets/img/start_btn.png')
        start_button = Button("start_button", screen, start_button_rel_x, start_button_rel_y, start_button_rel_width,
                              start_button_rel_height, start_button_img)
        self.components["start_button"] = start_button

        # username text input box
        username_input_rel_x = 1 / 2
        username_input_rel_y = 1 / 2
        username_input_rel_width = 1 / 3
        username_input_rel_height = 1 / 16
        username_input_box = Textbox("username_input_box", screen, username_input_rel_x, username_input_rel_y,
                                     username_input_rel_width, username_input_rel_height)
        self.components["username_input_box"] = username_input_box

        # password text input box
        password_input_rel_x = 1 / 2
        password_input_rel_y = 3 / 5
        password_input_rel_width = 1 / 3
        password_input_rel_height = 1 / 16
        password_input_box = Textbox("password_input_box", screen, password_input_rel_x, password_input_rel_y,
                                     password_input_rel_width, password_input_rel_height)
        self.components["password_input_box"] = password_input_box

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            if triggered_component in ["start_button", "username_input_box", "password_input_box"]:
                self.data["username"] = self.components["username_input_box"].input
                self.data["password"] = self.components["password_input_box"].input
                #using placeholder for now
                if self.data["username"] == "username" and self.data["password"] == "password":
                    return self.data
                else:
                    print("login failed")

