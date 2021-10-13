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
        bg_img = pygame.image.load('assets/img/sky.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background


        # picture display - sun to be replaced with a game introduction image
        home_image_rel_x = 1 / 10
        home_image_rel_y = 1 / 2
        home_image_rel_width = 1 / 3
        home_image_rel_height = 1 / 5
        home_image_img = pygame.image.load('assets/img/sun.png')
        home_image_box = ImageDisplay("home_image_box", screen, home_image_rel_x, home_image_rel_y,
                                       home_image_rel_width, home_image_rel_height,home_image_img)
        self.components["home_image_box"] = home_image_box

        # #user signs in
        # sign_in_button_rel_x = 7 / 10
        # sign_in_button_rel_y = 3 / 4
        # sign_in_button_rel_width = 1 / 8
        # sign_in_button_rel_height = 1 / 8
        # sign_in_button_img = pygame.image.load('assets/img/start_btn.png')
        # sign_in_button = ImageButton("sign_in_button", screen, sign_in_button_rel_x, sign_in_button_rel_y,
        #                            sign_in_button_rel_width,
        #                            sign_in_button_rel_height, sign_in_button_img)
        # self.components["sign_in_button"] = sign_in_button

        #new acc creation
        create_acc_button_rel_x = 7/10
        create_acc_button_rel_y = 3 / 4
        create_acc_button_rel_width = 1 / 8
        create_acc_button_rel_height = 1 / 8
        create_acc_button_img = pygame.image.load('assets/img/start_btn.png')
        create_acc_button = ImageButton("create_acc_button", screen, create_acc_button_rel_x, create_acc_button_rel_y,
                                        create_acc_button_rel_width,
                                        create_acc_button_rel_height, create_acc_button_img)
        self.components["create_acc_button"] = create_acc_button

        # username text input box
        username_input_rel_x = 1 / 2
        username_input_rel_y = 1 / 2
        username_input_rel_width = 1 / 3
        username_input_rel_height = 1 / 16
        username_input_box = TextInput("username_input_box", screen, username_input_rel_x, username_input_rel_y,
                                     username_input_rel_width, username_input_rel_height)
        self.components["username_input_box"] = username_input_box

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
            # if triggered_component in [self.components["sign_in_button"]]:
            #     print("check input value against database")
            #     self.name = "main_menu"
            if triggered_component in [self.components["create_acc_button"]]:
                print("Put new user info in database")
                self.output_data["username"] = self.components["username_input_box"].input
                self.output_data["password"] = self.components["password_input_box"].input
                self.name = "login"