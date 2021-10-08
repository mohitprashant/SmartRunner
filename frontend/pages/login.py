from assets.components import *
from page import *


class LoginPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "login"
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



        # component surface
        component_surface_rel_width = 0.8
        component_surface_rel_height = 0.8
        component_surface_rel_x = 0.1
        component_surface_rel_y = 0.1
        display_rel_width = 0.8
        display_rel_height = 0.4

        component_surface = MouseScrollableSurface("component_surface", screen, component_surface_rel_x,
                                                   component_surface_rel_y, component_surface_rel_width,
                                                   component_surface_rel_height, screen, display_rel_width, display_rel_height)
        self.components["component_surface"] = component_surface



        # surface_background
        surface_bg_img = pygame.image.load('assets/img/background2.jpg')
        surface_background = Background("surface_background", component_surface.surface, surface_bg_img)
        component_surface.add_component(surface_background)

        # start button
        start_button_rel_x = 0
        start_button_rel_y = 0
        start_button_rel_width = 0.5
        start_button_rel_height = 1/3
        start_button_img = pygame.image.load('assets/img/start_btn.png')
        # start_button = ImageButton("start_button", component_surface.surface, start_button_rel_x, start_button_rel_y,
        #                            start_button_rel_width, start_button_rel_height, start_button_img)
        # component_surface.add_component(start_button)

        # self.components["start_button"] = start_button
        #
        # username text input box
        username_input_rel_x = 2 / 3
        username_input_rel_y = 3 / 4
        username_input_rel_width = 1 / 3
        username_input_rel_height = 1 / 4
        username_input_box = TextInput("username_input_box", component_surface.surface, username_input_rel_x,
                                       username_input_rel_y, username_input_rel_width, username_input_rel_height)
        component_surface.add_component(username_input_box)
        #
        # # password text input box
        # password_input_rel_x = 1 / 2
        # password_input_rel_y = 3 / 5
        # password_input_rel_width = 1 / 3
        # password_input_rel_height = 1 / 16
        # password_input_box = TextInput("password_input_box", screen, password_input_rel_x, password_input_rel_y,
        #                              password_input_rel_width, password_input_rel_height)
        # self.components["password_input_box"] = password_input_box

        test_rel_x = 0 / 2
        test_rel_y = 0 / 2
        test_rel_width = 1 / 2
        test_rel_height = 1 / 10
        test_text = "test text"
        test_select_text = SelectableTextButton("test_select_text", component_surface.surface, test_rel_x, test_rel_y, test_rel_width,
                                                test_rel_height, test_text)
        component_surface.add_component(test_select_text)

        component_surface_2 = ComponentSurface("component_surface2", component_surface.surface, component_surface_rel_x,
                                               component_surface_rel_y, component_surface_rel_width,
                                               component_surface_rel_height, screen)
        component_surface.add_component(component_surface_2)

        start_button2 = ImageButton("start_button2", component_surface_2.surface, start_button_rel_x, start_button_rel_y,
                                   start_button_rel_width, start_button_rel_height, start_button_img)
        component_surface_2.add_component(start_button2)

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            if triggered_component.name in ["start_button", "username_input_box", "password_input_box"]:
                self.data["username"] = self.components["username_input_box"].input
                self.data["password"] = self.components["password_input_box"].input
                # using placeholder for now
                if self.data["username"] == "username" and self.data["password"] == "password":
                    return self.data
                else:
                    print("login failed")
            if triggered_component.name == "component_surface":
                for surface_triggered_component in triggered_component.triggered_component_list:
                    print(surface_triggered_component.name)
                    if surface_triggered_component.name == "component_surface2":
                        for surface_triggered_component2 in surface_triggered_component.triggered_component_list:
                            print(surface_triggered_component2.relative_display_x)
                            print(surface_triggered_component2.relative_display_y)
                            print(surface_triggered_component2.relative_display_width)
                            print(surface_triggered_component2.relative_display_height)
