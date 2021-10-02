from assets.components import *
from page import *


class UniqueAnalyticsPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "uniqueanaytics"
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

        # export button
        export_button_rel_x = 11 / 15
        export_button_rel_y = 4 / 5
        export_button_rel_width = 1 / 7
        export_button_rel_height = 1 / 7
        export_button_img = pygame.image.load('assets/img/load_btn.png')
        export_button = ImageButton("export_button", screen, export_button_rel_x, export_button_rel_y, export_button_rel_width,
                              export_button_rel_height, export_button_img)
        self.components["export_button"] = export_button

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
            if triggered_component in ["export_button"]:
                print("export csv")
            if triggered_component in ["exit_button"]:
                print("return to analytics selection")
            #add triggered component for scrollable display
