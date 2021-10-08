from assets.components import *
from page import *


class SinglePlayerPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "singleplayer"
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
        start_button_rel_x = 3 / 7
        start_button_rel_y = 4 / 5
        start_button_rel_width = 1 / 7
        start_button_rel_height = 1 / 7
        start_button_img = pygame.image.load('assets/img/start_btn.png')
        start_button = ImageButton("start_button", screen, start_button_rel_x, start_button_rel_y, start_button_rel_width,
                              start_button_rel_height, start_button_img)
        self.components["start_button"] = start_button

        # back button
        exit_button_rel_x = 1 / 15
        exit_button_rel_y = 4 / 5
        exit_button_rel_width = 1 / 7
        exit_button_rel_height = 1 / 7
        exit_button_img = pygame.image.load('assets/img/exit_btn.png')
        exit_button = ImageButton("exit_button", screen, exit_button_rel_x, exit_button_rel_y,
                                   exit_button_rel_width,
                                   exit_button_rel_height, exit_button_img)
        self.components["exit_button"] = exit_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            if triggered_component in [self.components["start_button"]]:
                #pass in scrollable select inputs
                print("start game session")
            if triggered_component in [self.components["exit_button"]]:
                print("return to main menu")

