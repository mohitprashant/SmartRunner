from assets.components import *
from page import *


class WelcomeScreenPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "login"
        self.input_data = {
        }
        self.output_data = {
            "current_page": self.name,
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/Backgrounds/loginbg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        sign_in_button_rel_x = 0.55
        sign_in_button_rel_y = 0.7
        sign_in_button_rel_width = 0.18
        sign_in_button_rel_height = 1 / 8
        sign_in_button_img = pygame.image.load('assets/Buttons/btn_signin.png')
        sign_in_button = ImageButton("sign_in_button", screen, sign_in_button_rel_x, sign_in_button_rel_y,
                                   sign_in_button_rel_width,
                                   sign_in_button_rel_height, sign_in_button_img)
        self.components["sign_in_button"] = sign_in_button

        create_acc_button_rel_x = 0.3
        create_acc_button_rel_y = 0.7
        create_acc_button_rel_width = 0.18
        create_acc_button_rel_height = 1 / 8
        create_acc_button_img = pygame.image.load('assets/Buttons/btn_createacct.png')
        create_acc_button = ImageButton("create_acc_button", screen, create_acc_button_rel_x, create_acc_button_rel_y,
                                        create_acc_button_rel_width,
                                        create_acc_button_rel_height, create_acc_button_img)
        self.components["create_acc_button"] = create_acc_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            if triggered_component in [self.components["sign_in_button"]]:
                self.name = "login"
            if triggered_component in [self.components["create_acc_button"]]:
                self.name = "create_account"