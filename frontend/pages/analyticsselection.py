from assets.components import *
from page import *


class AnalyticsSelectPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "analyticsselect"
        self.input_data = {
            "analyticslist": [],
            "roomID": ""
        }
        self.output_data = {
            "current_page": self.name,
            "roomID": "",
            "analyticsID": "",
            "all_time": False,
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        #assign output data
        self.output_data["roomID"] = self.input_data["roomID"]

        # background
        bg_img = pygame.image.load('assets/img/sky.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # text display
        relative_x = 7 / 20
        relative_y = 1 / 11
        relative_width = 1 / 3
        relative_height = 1 / 12
        text_display = TextDisplay("text_display", screen, relative_x, relative_y, relative_width, relative_height,
                                   "Analytics List")
        self.components["text_display"] = text_display

        # analytics list
        relative_x = 1 / 5
        relative_y = 1 / 6
        relative_width = 3 / 5
        text_relative_height = 1 / 10
        shown_relative_width = 3 / 5
        shown_relative_height = 3 / 5
        text_list = self.input_data["analyticslist"]

        selectable_text_list = SelectableTextList("selectable_text_list", screen, relative_x,
                                                  relative_y, relative_width,
                                                  text_relative_height, shown_relative_width, shown_relative_height,
                                                  text_list, single_select=True)
        self.components["selectable_text_list"] = selectable_text_list
        self.layers.append(selectable_text_list)

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
            if triggered_component in [self.components["selectable_text_list"]]:
                print("store selection in self.output_data[analyticsID]")
                self.name = "uniqueanalytics"
                #use self.output_data["roomID"] to determine which room
            if triggered_component in [self.components["alltime_button"]]:
                print("navigate to alltime analytics")
                self.output_data["all_time"] = True
                self.name = "uniqueanalytics"
                #use self.output_data["all_time"] to navigate to alltime analytics
            if triggered_component in [self.components["exit_button"]]:
                self.name = "hostroom"
                #use self.output_data["roomID"] to select correct room

