from assets.components import *
from page import *


class AnalyticsSelectPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "analyticsselect"
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

        # all-time analytics button
        alltime_button_rel_x = 11 / 15
        alltime_button_rel_y = 4 / 5
        alltime_button_rel_width = 1 / 7
        alltime_button_rel_height = 1 / 7
        alltime_button_img = pygame.image.load('assets/img/blob.png')
        alltime_button = ImageButton("alltime_button", screen, alltime_button_rel_x, alltime_button_rel_y, alltime_button_rel_width,
                              alltime_button_rel_height, alltime_button_img)
        self.components["alltime_button"] = alltime_button

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
            if triggered_component in ["alltime_button"]:
                print("navigate to alltime analytics")
            if triggered_component in ["exit_button"]:
                print("return to host room")
            #add triggered component for scrollable single select
