from assets.components import *
from page import *
import sys
sys.path.insert(1, '../../backend/account')
import AccountManager

class CreateAccountPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "create_account"
        self.input_data = {
        }
        self.output_data = {
            "current_page": self.name,
            "username": "",
            "password": "",
            "password1":"",
            "error_check":False,
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/Backgrounds/loginbg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background


        username_image_rel_x = 0.30
        username_image_rel_y = 0.4
        username_image_rel_width = 0.18
        username_image_rel_height = 1 / 9
        username_image_img = pygame.image.load('assets/Backgrounds/username.png')
        username_image_box = ImageDisplay("username_image_box", screen, username_image_rel_x, username_image_rel_y,
                                       username_image_rel_width, username_image_rel_height,username_image_img)
        self.components["username_image_box"] = username_image_box

        password_image_rel_x = 0.30
        password_image_rel_y = 0.5
        password_image_rel_width = 0.18
        password_image_rel_height = 1 / 9
        password_image_img = pygame.image.load('assets/Backgrounds/password.png')
        password_image_box = ImageDisplay("password_image_box", screen, password_image_rel_x, password_image_rel_y,
                                      password_image_rel_width, password_image_rel_height, password_image_img)
        self.components["password_image_box"] = password_image_box



        # username text input box
        username_input_rel_x = 1 / 2
        username_input_rel_y = 0.4
        username_input_rel_width = 1 / 4
        username_input_rel_height = 1 / 14
        username_input_box = TextInput("username_input_box", screen, username_input_rel_x, username_input_rel_y,
                                     username_input_rel_width, username_input_rel_height)
        self.components["username_input_box"] = username_input_box

        # password text input box
        password_input_rel_x = 1 / 2
        password_input_rel_y = 0.5
        password_input_rel_width = 1 / 4
        password_input_rel_height = 1 / 14
        password_input_box = TextInput("password_input_box", screen, password_input_rel_x, password_input_rel_y,
                                     password_input_rel_width, password_input_rel_height)
        self.components["password_input_box"] = password_input_box


        # password text input box
        password1_input_rel_x = 1 / 2
        password1_input_rel_y = 0.6
        password1_input_rel_width = 1 / 4
        password1_input_rel_height = 1 / 14
        password1_input_box = TextInput("password1_input_box", screen, password1_input_rel_x, password1_input_rel_y,
                                       password1_input_rel_width, password1_input_rel_height)
        self.components["password1_input_box"] = password1_input_box

        if self.output_data["error_check"] == True:
            error_display_rel_x = 0.4
            error_display_rel_y = 0.3
            error_display_rel_width = 1 / 4
            error_display_rel_height = 1 / 14
            error_display_text = "Invalid input!"
            error_display_box = TextDisplay("error_display_box", screen, error_display_rel_x, error_display_rel_y,
                                            error_display_rel_width, error_display_rel_height, error_display_text)
            self.components["error_display_box"] = error_display_box

        exit_button_rel_x = 0.5
        exit_button_rel_y = 0.7
        exit_button_rel_width = 0.1
        exit_button_rel_height = 1 / 8
        exit_button_img = pygame.image.load('assets/Buttons/btn_back.png')
        exit_button = ImageButton("exit_button", screen, exit_button_rel_x, exit_button_rel_y,
                                  exit_button_rel_width,
                                  exit_button_rel_height, exit_button_img)
        self.components["exit_button"] = exit_button

        # new acc creation
        create_acc_button_rel_x = 0.62
        create_acc_button_rel_y = 0.7
        create_acc_button_rel_width = 0.12
        create_acc_button_rel_height = 0.129
        create_acc_button_img = pygame.image.load('assets/Buttons/btn_createacct.png')
        create_acc_button = ImageButton("create_acc_button", screen, create_acc_button_rel_x, create_acc_button_rel_y,
                                        create_acc_button_rel_width,
                                        create_acc_button_rel_height, create_acc_button_img)
        self.components["create_acc_button"] = create_acc_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            if triggered_component in [self.components["create_acc_button"]]:
                print("Put new user info in database")
                self.output_data["username"] = self.components["username_input_box"].input
                self.output_data["password"] = self.components["password_input_box"].input
                self.output_data["password1"] = self.components["password1_input_box"].input
                print("password:",self.output_data["password"])
                print("password1:",self.output_data["password1"])
                create_acc_check = AccountManager.create_account_confirm_password(self.output_data["username"], self.output_data["password"],self.output_data["password1"])
                if create_acc_check != None:
                    self.name = "login"
                else:
                    self.output_data["error_check"] = True
                    print("Error")
            if triggered_component in [self.components["exit_button"]]:
                self.name="welcome_screen"


