from assets.components import *
from page import *


class CreateAccountPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "login"
        self.input_data = {
        }
        self.output_data = {
            "current_page": self.name,
            "username": "",
            "password": "",
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/Backgrounds/loginbg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background


        username_image_rel_x = 0.30
        username_image_rel_y = 0.49
        username_image_rel_width = 0.18
        username_image_rel_height = 1 / 9
        username_image_img = pygame.image.load('assets/Backgrounds/username.png')
        username_image_box = ImageDisplay("username_image_box", screen, username_image_rel_x, username_image_rel_y,
                                       username_image_rel_width, username_image_rel_height,username_image_img)
        self.components["username_image_box"] = username_image_box

        password_image_rel_x = 0.30
        password_image_rel_y = 0.59
        password_image_rel_width = 0.18
        password_image_rel_height = 1 / 9
        password_image_img = pygame.image.load('assets/Backgrounds/password.png')
        password_image_box = ImageDisplay("password_image_box", screen, password_image_rel_x, password_image_rel_y,
                                      password_image_rel_width, password_image_rel_height, password_image_img)
        self.components["password_image_box"] = password_image_box


        #new acc creation
        create_acc_button_rel_x = 0.57
        create_acc_button_rel_y = 0.7
        create_acc_button_rel_width = 0.18
        create_acc_button_rel_height = 1 / 8
        create_acc_button_img = pygame.image.load('assets/Buttons/btn_createacct.png')
        create_acc_button = ImageButton("create_acc_button", screen, create_acc_button_rel_x, create_acc_button_rel_y,
                                        create_acc_button_rel_width,
                                        create_acc_button_rel_height, create_acc_button_img)
        self.components["create_acc_button"] = create_acc_button

        # username text input box
        username_input_rel_x = 1 / 2
        username_input_rel_y = 1 / 2
        username_input_rel_width = 1 / 4
        username_input_rel_height = 1 / 14
        username_input_box = TextInput("username_input_box", screen, username_input_rel_x, username_input_rel_y,
                                     username_input_rel_width, username_input_rel_height)
        self.components["username_input_box"] = username_input_box

        # password text input box
        password_input_rel_x = 1 / 2
        password_input_rel_y = 3 / 5
        password_input_rel_width = 1 / 4
        password_input_rel_height = 1 / 14
        password_input_box = TextInput("password_input_box", screen, password_input_rel_x, password_input_rel_y,
                                     password_input_rel_width, password_input_rel_height)
        self.components["password_input_box"] = password_input_box

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            # if triggered_component in [self.components["sign_in_button"]]:
            #     print("check input value against database")
            #     self.name = "main_menu"
            if triggered_component in [self.components["create_acc_button"]]:
                print("Put new user info in database")
                self.output_data["username"] = self.components["username_input_box"].input
                self.output_data["password"] = self.components["password_input_box"].input
                self.name = "login"