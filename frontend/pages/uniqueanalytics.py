from assets.components import *
from page import *


class UniqueAnalyticsPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "uniqueanalytics"
        self.input_data = {
            "analytics": [],
            "roomID": ""
        }
        self.output_data = {
            "current_page": self.name,
            "roomID": self.input_data["roomID"],
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        # assign output data
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
                                   "Analytics")
        self.components["text_display"] = text_display

        # analytics list
        relative_x = 1 / 5
        relative_y = 1 / 6
        relative_width = 0.6
        text_relative_height = 1 / 10
        shown_relative_width = 3 / 5
        shown_relative_height = 3 / 5
        text_list = self.input_data["analytics"]

        selectable_text_list = SelectableTextList("selectable_text_list", screen, relative_x,
                                                  relative_y, relative_width,
                                                  text_relative_height, shown_relative_width, shown_relative_height,
                                                  text_list, single_select=True, active_color="white")
        self.components["selectable_text_list"] = selectable_text_list
        self.layers.append(selectable_text_list)

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
            if triggered_component in [self.components["export_button"]]:
                print("export csv")
            if triggered_component in [self.components["exit_button"]]:
                self.name = "analyticsselect"
