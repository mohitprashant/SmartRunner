import sys
import pathlib
sys.path.insert(0, '../../backend/account')
sys.path.insert(1, '../../frontend/pages')

import AccountManager

from assets.components import *
from page import *

curr_dir = str(pathlib.Path(__file__).parent.resolve()) + '/'


class LoginPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "login"
        self.input_data = {
        }
        self.output_data = {
            "current_page": self.name,
            "username": "",
            "password": "",
            "error_check":"",
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        # background
        bg_img = pygame.image.load(curr_dir + 'assets/Backgrounds/loginbg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        signin_image_rel_x = 0.2
        signin_image_rel_y = 0.05
        signin_image_rel_width = 0.6
        signin_image_rel_height = 0.4
        signin_image_img = pygame.image.load(curr_dir + 'assets/Backgrounds/sign_in.png')
        signin_image_box = ImageDisplay("username_image_box", screen, signin_image_rel_x, signin_image_rel_y,
                                        signin_image_rel_width, signin_image_rel_height, signin_image_img)
        self.components["signin_image_box"] = signin_image_box

        username_image_rel_x = 0.30
        username_image_rel_y = 0.49
        username_image_rel_width = 0.18
        username_image_rel_height = 1 / 9
        username_image_img = pygame.image.load(curr_dir + 'assets/Backgrounds/username.png')
        username_image_box = ImageDisplay("username_image_box", screen, username_image_rel_x, username_image_rel_y,
                                          username_image_rel_width, username_image_rel_height, username_image_img)
        self.components["username_image_box"] = username_image_box

        password_image_rel_x = 0.30
        password_image_rel_y = 0.59
        password_image_rel_width = 0.18
        password_image_rel_height = 1 / 9
        password_image_img = pygame.image.load(curr_dir + 'assets/Backgrounds/password.png')
        password_image_box = ImageDisplay("password_image_box", screen, password_image_rel_x, password_image_rel_y,
                                          password_image_rel_width, password_image_rel_height, password_image_img)
        self.components["password_image_box"] = password_image_box

        # username text input box
        username_input_rel_x = 1 / 2
        username_input_rel_y = 0.5
        username_input_rel_width = 1 / 4
        username_input_rel_height = 1 / 14
        username_input_box = TextInput("username_input_box", screen, username_input_rel_x, username_input_rel_y,
                                       username_input_rel_width, username_input_rel_height)
        self.components["username_input_box"] = username_input_box

        # password text input box
        password_input_rel_x = 1 / 2
        password_input_rel_y = 0.6
        password_input_rel_width = 1 / 4
        password_input_rel_height = 1 / 14
        password_input_box = TextInput("password_input_box", screen, password_input_rel_x, password_input_rel_y,
                                       password_input_rel_width, password_input_rel_height)
        self.components["password_input_box"] = password_input_box

        if self.output_data["error_check"] == True:
            error_display_rel_x = 0.4
            error_display_rel_y = 0.39
            error_display_rel_width = 1 / 4
            error_display_rel_height = 1 / 14
            error_display_text = "Invalid input!"
            error_display_box = TextDisplay("error_display_box", screen, error_display_rel_x, error_display_rel_y,
                                            error_display_rel_width, error_display_rel_height, error_display_text)
            self.components["error_display_box"] = error_display_box

        exit_button_rel_x = 0.5
        exit_button_rel_y = 0.7
        exit_button_rel_width = 0.1
        exit_button_rel_height = 0.11
        exit_button_img = pygame.image.load(curr_dir + 'assets/Buttons/btn_back.png')
        exit_button = ImageButton("exit_button", screen, exit_button_rel_x, exit_button_rel_y,
                                  exit_button_rel_width, exit_button_rel_height, exit_button_img)
        self.components["exit_button"] = exit_button

        # user signs ins
        sign_in_button_rel_x = 0.62
        sign_in_button_rel_y = 0.7
        sign_in_button_rel_width = 1 / 8
        sign_in_button_rel_height = 0.1111
        sign_in_button_img = pygame.image.load(curr_dir + 'assets/Buttons/btn_signin.png')
        sign_in_button = ImageButton("sign_in_button", screen, sign_in_button_rel_x, sign_in_button_rel_y,
                                     sign_in_button_rel_width, sign_in_button_rel_height, sign_in_button_img)
        self.components["sign_in_button"] = sign_in_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]

            if triggered_component in [self.components["sign_in_button"]]:
                self.output_data["username"] = self.components["username_input_box"].input
                self.output_data["password"] = self.components["password_input_box"].input
                login_check = AccountManager.login(self.output_data["username"],self.output_data["password"])

                if login_check != None:
                    self.name = "main_menu"
                else:
                    self.output_data["error_check"] = True

            if triggered_component in [self.components["exit_button"]]:
                self.name = "welcome_screen"
