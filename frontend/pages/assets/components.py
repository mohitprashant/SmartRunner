import pygame

'''
Parent class of every component on the screen
string name - name of the component
float relative_x - x position of the component relative to the screen width
float relative_y - y position of the component relative to the screen height
float relative_width - width of the component relative to the screen width
float relative_height - height of the component relative to the screen height
pygame.Surface screen - screen for the component to be put on
'''


class Component:
    # Component constructor
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height):
        self.name = name

        self.screen = screen  # screen component is on
        self.screen_width = screen.get_width()  # screen width
        self.screen_height = screen.get_height()  # screen height
        self.display_screen = self.screen.get_abs_parent()
        self.display_screen_width = self.display_screen.get_width()
        self.display_screen_height = self.display_screen.get_height()

        self.relative_x = relative_x  # relative x position
        self.relative_display_x = relative_x
        self.relative_y = relative_y  # relative y position
        self.relative_display_y = relative_y
        self.relative_width = relative_width  # relative width
        self.relative_display_width = relative_width
        self.relative_height = relative_height  # relative height
        self.relative_display_height = relative_height

        self.x = int(self.screen_width * relative_x)  # x position of component after scaling
        self.display_x = int(self.display_screen_width * self.relative_display_x)
        self.y = int(self.screen_height * relative_y)  # y position of component after scaling
        self.display_y = int(self.display_screen_height * self.relative_display_y)
        self.width = int(self.display_screen_width * relative_width)  # width of component after scaling
        self.display_width = int(self.screen_width * self.relative_display_width)
        self.height = int(self.screen_height * relative_height)  # height of component after scaling
        self.display_height = int(self.display_screen_height * self.relative_display_height)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.display_rect = pygame.Rect(self.display_x, self.display_y, self.display_width, self.display_height)

        self.on_display = True
        self.is_surface = False
        self.mouse_function = False  # Can component interact with mouse
        self.scrollable = False  # Can component be scrolled
        self.keyboard_function = False  # Can component interact with keyboard
        self.expandable = False  # Can component be expanded

    # blit component onto screen
    def draw(self):
        self.screen.blit(self.screen, (self.x, self.y))

    # resize component when screen is resized
    # new dimensions and coordinates are rescaled with relative position/dimensions
    # child class may have other variables that needs to be resized
    def resize(self, new_screen):
        self.screen = new_screen
        self.screen_width = new_screen.get_width()
        self.screen_height = new_screen.get_height()
        if self.on_display:
            self.display_screen = self.screen.get_abs_parent()
            self.display_screen_width = self.display_screen.get_width()
            self.display_screen_height = self.display_screen.get_height()

        self.x = int(self.screen_width * self.relative_x)
        self.y = int(self.screen_height * self.relative_y)
        self.display_x = int(self.display_screen_width * self.relative_display_x)
        self.display_y = int(self.display_screen_height * self.relative_display_y)
        self.width = int(self.screen_width * self.relative_width)
        self.height = int(self.screen_height * self.relative_height)
        self.display_width = int(self.display_screen_width * self.relative_display_width)
        self.display_height = int(self.display_screen_height * self.relative_display_height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.display_rect = pygame.Rect(self.display_x, self.display_y, self.display_width, self.display_height)

    # behavior of the component on event
    # returns True if response from system is expected
    def trigger(self, event):
        return False




# create an image object from an image
'''
class for Image Object component
same parameters as parent class Component except image
pygame.Surface image - the image to be put on the surface
'''


class ImageDisplay(Component):
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height, image):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height)
        self.image = image  # image used for button
        self.scaled_image = pygame.transform.scale(image, (self.width, self.height))

    # draw the button on the screen
    def draw(self):
        self.screen.blit(self.scaled_image, (self.x, self.y))

    # additional variables to resize not covered by parent resize
    def resize(self, new_screen):
        super().resize(new_screen)
        self.scaled_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect.x = self.x  # initialize button x-coordinates
        self.rect.y = self.y  # initialize button y-coordinates


# create a button from an image
'''
class for button component
same parameters as parent class ImageObject
additional trigger function for clicking of button
'''


class ImageButton(ImageDisplay):
    # button constructor
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height, image):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height, image)
        self.mouse_function = True
        self.clicked = False  # initialize if button is clicked to false

    # return true if button is clicked
    def trigger(self, event):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.display_rect.collidepoint(pos):  # when mouse is on top of button
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1 and not self.clicked:  # new left click and not held beforehand
                    action = True  # trigger action
                    self.clicked = True  # prevent multiple input by holding click

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # when left click is let go
                self.clicked = False  # set click to false

        return action


# button with single color
class ColorButton(ImageButton):
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height, color="black"):
        width = relative_width * screen.get_width()
        height = relative_height * screen.get_height()
        self.image_surface = pygame.Surface((width, height))
        self.image_surface.fill(color)
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height, self.image_surface)


class ToggleButton(ImageButton):
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height, image, toggle_image,
                 toggled=False):
        if toggled:
            super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height, toggle_image)
        else:
            super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height, image)
        self.original_image = image
        self.toggle_image = toggle_image
        self.toggled = toggled


    # return true if button is clicked
    def trigger(self, event):

        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.display_rect.collidepoint(pos):  # when mouse is on top of button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not self.clicked:  # new left click and not held beforehand
                    if self.toggled:
                        self.image = self.original_image
                        self.toggled = False
                    else:
                        self.image = self.toggle_image
                        self.toggled = True

                    self.clicked = True  # prevent multiple input by holding click
                    action = True
                    self.resize(self.screen)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # when left click is let go
                self.clicked = False  # set click to false
        return action


# add background for page
'''
class for background component
same parameters as parent class Component except image
relative_x and relative_y set to 0 so background starts from top left corner of screen
relative_width and relative_height set to 1 so background covers the whole screen

pygame.Surface image - the image used to make the button
'''


class Background(Component):
    # background constructor
    def __init__(self, name, screen, image, relative_x=0, relative_y=0, relative_width=1, relative_height=1):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height)
        self.image = image
        self.scaled_image = pygame.transform.scale(image, (self.width, self.height))

    # blit component onto screen
    def draw(self):
        self.screen.blit(self.scaled_image, (self.x, self.y))

    # additional variables to resize not covered by parent resize
    def resize(self, new_screen):
        super().resize(new_screen)
        self.scaled_image = pygame.transform.scale(self.image, (self.width, self.height))


class ComponentSurface(Component):
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height, display_screen, on_display=True):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height)

        self.on_display = on_display
        self.display_screen = display_screen
        self.display_screen_width = display_screen.get_width()
        self.display_screen_height = display_screen.get_height()

        self.components = {}
        self.components_og_pos_size = {}
        self.components_shown_og_pos_size = {}
        self.display_components = {}
        self.shown_display_components = {}

        self.surface = pygame.Surface((self.width, self.height))

        self.is_surface = True
        self.mouse_function = True
        self.keyboard_function = True
        self.triggered_component_list = []
        self.navigation_surface = True

    # todo might be useless
    def add_component(self, component):
        self.components[component.name] = component
        # get all original rel pos and size
        component_pos_size = {"rel_x": component.relative_x, "rel_y": component.relative_y,
                              "rel_width": component.relative_width, "rel_height": component.relative_height}
        self.components_og_pos_size[component.name] = component_pos_size
        # part for scrollable surface
        if component.scrollable:
            component_shown_pos_size = {"rel_x": component.relative_shown_x, "rel_y": component.relative_shown_y,
                                        "rel_width": component.relative_shown_width,
                                        "rel_height": component.relative_shown_height}
            self.components_shown_og_pos_size[component.name] = component_shown_pos_size

    # todo might be useless
    def remove_component(self, component_name):
        if component_name in self.components:
            if self.components[component_name].scrollable:
                self.components_shown_og_pos_size.pop(component_name)
            self.components_og_pos_size.pop(component_name)
            self.components.pop(component_name)

    # update each component's display size and position on the screen
    # this is to make mouse pos match component pos since mouse pos use display as reference
    def update(self):
        for component in self.components.values():

            component.relative_display_x = self.relative_display_x + \
                                           component.relative_x * self.relative_display_width

            component.relative_display_y = self.relative_display_y + \
                                           component.relative_y * self.relative_display_height

            component.relative_display_width = self.components_og_pos_size[component.name]["rel_width"] \
                                               * self.relative_display_width

            component.relative_display_height = self.components_og_pos_size[component.name]["rel_height"] \
                                                * self.relative_display_height
            component.display_x = int(self.display_screen_width * component.relative_display_x)
            component.display_y = int(self.display_screen_height * component.relative_display_y)
            component.display_width = int(self.display_screen_width * component.relative_display_width)
            component.display_height = int(self.display_screen_height * component.relative_display_height)

            component.display_rect = pygame.Rect(component.display_x, component.display_y,
                                                 component.display_width, component.display_height)

            if component.scrollable:
                component.relative_shown_display_x = self.relative_display_x + \
                                                     self.components_shown_og_pos_size[component.name]["rel_x"] \
                                                     * self.relative_display_width

                component.relative_shown_display_y = self.relative_display_y + \
                                                     self.components_shown_og_pos_size[component.name]["rel_y"] \
                                                     * self.relative_display_height

                component.relative_shown_display_width = self.components_shown_og_pos_size[component.name]["rel_width"] \
                                                         * self.relative_display_width

                component.relative_shown_display_height = self.components_shown_og_pos_size[component.name][
                                                              "rel_height"] \
                                                          * self.relative_display_height
                component.shown_display_x = int(self.display_screen_width * component.relative_shown_display_x)
                component.shown_display_y = int(self.display_screen_height * component.relative_shown_display_y)
                component.shown_display_width = int(self.display_screen_width * component.relative_shown_display_width)
                component.shown_display_height = int(self.display_screen_height *
                                                     component.relative_shown_display_height)

                component.shown_display_rect = pygame.Rect(component.shown_display_x, component.shown_display_y,
                                                           component.shown_display_width,
                                                           component.shown_display_height)

    def draw(self):
        self.update()
        for component in self.components.values():
            component.draw()
        self.screen.blit(self.surface, (self.x, self.y))

    def trigger(self, event):
        action = False
        self.triggered_component_list.clear()
        # get mouse position
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # check mouseover and clicked conditions
            if self.display_rect.collidepoint(pos):  # when mouse is on top of button
                for component in self.components.values():
                    if component.trigger(event):
                        self.triggered_component_list.append(component)
                        action = True


        else:
            for component in self.components.values():
                if component.trigger(event):
                    self.triggered_component_list.append(component)
                    action = True
        return action

    def resize(self, new_screen):
        super().resize(new_screen)
        self.surface = pygame.Surface((self.width, self.height))  # surface of scrollable
        if self.on_display:
            self.display_screen = self.screen.get_abs_parent()
            self.display_screen_width = self.display_screen.get_width()
            self.display_screen_height = self.display_screen.get_height()
        self.set_display_screen(self.display_screen)
        for component in self.components.values():
            component.resize(self.surface)
        self.update()

    def set_display_screen(self, display_screen):
        for component in self.components.values():
            if component.is_surface:
                component.display_screen = display_screen
                component.set_display_screen(display_screen)


# add a scrollable component on screen
class ScrollableComponentSurface(ComponentSurface):
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height,
                 relative_shown_width, relative_shown_height, display_screen, on_display=True, scroll_axis_y=True):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height, display_screen, on_display)

        # display dimensions
        self.relative_shown_x = self.relative_x
        self.relative_shown_y = self.relative_y
        self.shown_x = self.x
        self.shown_display_x = self.shown_x
        self.shown_y = self.y
        self.shown_display_y = self.shown_y
        self.relative_shown_display_x = self.relative_display_x
        self.relative_shown_display_y = self.relative_display_y
        self.relative_shown_width = relative_shown_width
        self.relative_shown_display_width = relative_shown_width
        self.relative_shown_height = relative_shown_height
        self.relative_shown_display_height = relative_shown_height
        self.shown_width = int(relative_shown_width * screen.get_width())
        self.shown_display_width = self.shown_width
        self.shown_height = int(relative_shown_height * screen.get_height())
        self.shown_display_height = self.shown_height
        self.shown_rect = pygame.Rect(self.shown_x, self.shown_y, self.shown_width, self.shown_height)
        self.shown_display_rect = self.shown_rect = pygame.Rect(self.shown_display_x, self.shown_display_y,
                                                                self.shown_display_width, self.shown_display_height)
        self.shown_surface = pygame.Surface((self.shown_width, self.shown_height))

        self.scroll_axis_y = scroll_axis_y  # axis of scrolling

        self.scroll_relative_x = 0
        self.scroll_relative_y = 0
        self.scroll_x = 0  # x position of surface within display
        self.scroll_y = 0  # y position of surface within display

        self.scrollable = True

    # blit component onto screen
    def draw(self):
        self.update()
        for component in self.components.values():
            component.draw()
        self.shown_surface.blit(self.surface, (self.scroll_x, self.scroll_y))
        self.screen.blit(self.shown_surface, (self.shown_x, self.shown_y))

    # additional variables to resize not covered by parent resize
    def resize(self, new_screen):
        super().resize(new_screen)

        self.scroll_x = int(self.scroll_relative_x * self.screen_width)
        self.scroll_y = int(self.scroll_relative_y * self.screen_height)
        self.shown_x = int(self.relative_shown_x * self.screen_width)
        self.shown_display_x = int(self.relative_shown_display_x * self.display_screen_width)
        self.shown_y = int(self.relative_shown_y * self.screen_height)
        self.shown_display_y = int(self.relative_shown_display_y * self.display_screen_height)
        self.shown_width = int(self.relative_shown_width * self.screen_width)
        self.shown_display_width = int(self.relative_shown_display_width * self.display_screen_width)
        self.shown_height = int(self.relative_shown_height * self.screen_height)
        self.shown_display_height =int(self.relative_shown_display_height * self.display_screen_height)
        self.shown_rect = pygame.Rect(self.shown_x, self.shown_y, self.shown_width, self.shown_height)
        self.shown_display_rect = pygame.Rect(self.shown_display_x, self.shown_display_y, self.shown_display_width,
                                              self.shown_display_height)
        self.shown_surface = pygame.Surface((self.shown_width, self.shown_height))


# mouse controlled scrollable surface
class MouseScrollableSurface(ScrollableComponentSurface):

    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height,
                 relative_shown_width, relative_shown_height, display_screen, on_display=True,
                 scroll_axis_y=True, relative_scroll_length=1 / 8):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height,
                         relative_shown_width, relative_shown_height, display_screen, on_display, scroll_axis_y)

        self.relative_scroll_length = relative_scroll_length  # scroll length per wheel tick

        if self.scroll_axis_y:
            self.scroll_length = self.relative_scroll_length * self.height
            self.relative_display_scroll_length = relative_scroll_length * self.relative_height
        else:
            self.scroll_length = self.relative_scroll_length * self.width
            self.relative_display_scroll_length = relative_scroll_length * self.relative_width

    def trigger(self, event):
        action = False
        self.triggered_component_list.clear()
        # get mouse position
        pos = pygame.mouse.get_pos()
        # when mouse is on top of button
        if event.type == pygame.MOUSEBUTTONDOWN:
            # check mouseover and clicked conditions
            if self.shown_display_rect.collidepoint(pos):
                if event.button == 4:  # wheel roll up
                    if self.scroll_axis_y:
                        # top most position
                        if self.scroll_relative_y + self.relative_display_scroll_length >= 0:
                            self.scroll_relative_y = 0
                            self.relative_y = self.scroll_relative_y + self.relative_shown_y
                            self.relative_display_y = self.relative_shown_display_y + self.scroll_relative_y
                        else:
                            self.scroll_relative_y += self.relative_display_scroll_length
                            self.relative_y += self.relative_display_scroll_length
                            self.relative_display_y += self.relative_display_scroll_length
                    else:
                        if self.scroll_relative_x + self.relative_display_scroll_length >= 0:
                            self.scroll_relative_x = 0
                            self.relative_x = self.scroll_relative_x + self.relative_shown_x
                            self.relative_display_x = self.relative_shown_display_x + self.scroll_relative_x
                        else:
                            self.scroll_relative_x += self.relative_display_scroll_length
                            self.relative_x += self.relative_display_scroll_length
                            self.relative_display_x += self.relative_display_scroll_length

                elif event.button == 5:  # wheel roll down
                    if self.scroll_axis_y:
                        current_y = self.scroll_relative_y - self.relative_display_scroll_length
                        min_y = self.relative_shown_height - self.relative_height
                        min_display_y = self.relative_shown_display_y - self.relative_display_height +\
                                        self.relative_shown_display_height
                        if current_y <= min_y:
                            self.scroll_relative_y = min_y
                            self.relative_y = self.relative_shown_y + min_y
                            self.relative_display_y = min_display_y
                        else:
                            self.scroll_relative_y -= self.relative_display_scroll_length
                            self.relative_y -= self.relative_display_scroll_length
                            self.relative_display_y -= self.relative_display_scroll_length
                    else:
                        current_x = self.scroll_relative_x - self.relative_display_scroll_length
                        max_x = self.relative_shown_width - self.relative_width
                        min_display_x = self.relative_shown_display_x - self.relative_display_width + \
                                        self.relative_shown_display_width
                        if current_x <= max_x:
                            self.scroll_relative_x = max_x
                            self.relative_x = self.relative_shown_x + max_x
                            self.relative_display_x = min_display_x
                        else:
                            self.scroll_relative_x -= self.relative_display_scroll_length
                            self.relative_x -= self.relative_display_scroll_length
                            self.relative_display_x -= self.relative_display_scroll_length
                else:
                    for component in self.components.values():
                        if component.trigger(event):
                            self.triggered_component_list.append(component)
                            action = True

                self.resize(self.screen)

        else:
            for component in self.components.values():
                if component.trigger(event):
                    self.triggered_component_list.append(component)
                    action = True

        return action

    # additional variables to resize not covered by parent resize
    def resize(self, new_screen):
        super().resize(new_screen)
        if self.scroll_axis_y:
            self.scroll_length = int(self.relative_display_scroll_length * new_screen.get_height())
        else:
            self.scroll_length = int(self.relative_display_scroll_length * new_screen.get_width())


# display text on screen
class TextDisplay(Component):
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height,
                 text, font_file=None, font_color=pygame.Color("black")):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height)

        # font initialization
        self.font_file = font_file
        self.font_size = int(self.height * 4 / 3)  # font to height pixel ratio = 4:3 so we get font size from height
        self.text_font = pygame.font.Font(font_file, self.font_size)
        self.font_color = font_color
        self.text = text
        self.text_surface = self.text_font.render(self.text, True, self.font_color)

        # make sure text surface fits in dimensions aka reduce font size until width fits
        while self.text_surface.get_width() >= self.width:
            self.font_size -= 1
            self.text_font = pygame.font.Font(font_file, self.font_size)
            self.text_surface = self.text_font.render(self.text, True, self.font_color)
        self.display_width = self.text_surface.get_width()
        self.display_rect = pygame.Rect(self.x, self.y, self.display_width, self.height)

    # blit component onto screen
    def draw(self):
        self.screen.blit(self.text_surface, (self.x, self.y))

    # additional variables to resize not covered by parent resize
    def resize(self, new_screen):
        super().resize(new_screen)

        self.font_size = int(self.height * 4 / 3)  # resize font size

        self.text_font = pygame.font.Font(self.font_file, self.font_size)
        self.text_surface = self.text_font.render(self.text, True, self.font_color)  # resize font surface
        while self.text_surface.get_width() >= self.width:
            self.font_size -= 1
            self.text_font = pygame.font.Font(self.font_file, self.font_size)
            self.text_surface = self.text_font.render(self.text, True, self.font_color)
        self.display_width = self.text_surface.get_width()
        self.display_rect = pygame.Rect(self.x, self.y, self.display_width, self.height)  # resize display rect


class TextButton(TextDisplay):

    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height,
                 text, font_file=None, font_color=pygame.Color("black")):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height,
                         text, font_file=font_file, font_color=font_color)
        self.mouse_function = True
        self.clicked = False  # initialize if button is clicked to false

    # return true if button is clicked
    def trigger(self, event):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.display_rect.collidepoint(pos):  # when mouse is on top of button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not self.clicked:  # new left click and not held beforehand
                    action = True  # trigger action
                    self.clicked = True  # prevent multiple input by holding click

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # when left click is let go
                self.clicked = False  # set click to false

        return action


class TextboxButton(TextButton):
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height,
                 text, font_file=None, font_color=pygame.Color("black"),
                 back_color="white", relative_border_width=0):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height,
                         text, font_file, font_color)

        self.font_size = int(self.height)  # font size height = 3/4 pixel height
        self.text_font = pygame.font.Font(font_file, self.font_size)  # create pygame FONT
        self.font_color = font_color  # font color
        self.text_offset = int(self.height / 8)  # height offset so text is in middle
        self.text_surface = self.text_font.render(self.text, True, self.font_color)

        self.relative_border_width = relative_border_width
        self.border_width = relative_border_width * self.height
        self.back_color = back_color
        self.display_width = self.width
        self.display_rect = pygame.Rect(self.x, self.y, self.display_width, self.height)

    def draw(self):
        pygame.draw.rect(self.screen, self.back_color, self.rect, self.border_width)
        self.screen.blit(self.text_surface, (self.x + self.text_offset, self.y+self.text_offset))

    def resize(self, new_screen):
        super().resize(new_screen)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.x = self.x
        self.rect.y = self.y

        self.font_size = int(self.height)
        self.text_font = pygame.font.Font(self.font_file, self.font_size)
        self.text_offset = int(self.height / 8)
        self.text_surface = self.text_font.render(self.text, True, self.font_color)  # resize font surface

        self.border_width = int(self.relative_border_width * self.height)
        self.display_width = self.width
        self.display_rect = pygame.Rect(self.x, self.y, self.display_width, self.height)




class SelectableTextButton(TextboxButton):
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height,
                 text, font_file=None, font_color=pygame.Color("black"), active_color="dodgerblue",
                 passive_color="white", border_width=0):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height,
                         text, font_file, font_color, passive_color, border_width)
        self.border_width = border_width
        self.active_color = active_color
        self.passive_color = passive_color
        self.back_color = passive_color

        self.active = False

    def trigger(self, event):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # when mouse hovers over TextInput and click, TextInput is activated
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.display_rect.collidepoint(pos):
                    if self.active:
                        self.active = False
                        self.back_color = self.passive_color
                    else:
                        self.active = True
                        self.back_color = self.active_color
                    action = True
        return action

    def resize(self, new_screen):
        super().resize(new_screen)
        self.display_width = int(self.screen_width * self.relative_display_width)
        self.display_rect = pygame.Rect(self.display_x, self.display_y, self.display_width, self.display_height)

class SelectableTextButtonD(TextboxButton):
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height, text,
                active=False, active_color = "dodgerblue", passive_color = "white", active_font_color = "white", passive_font_color = "black",
                relative_border_width=0, font_file=None):
        if active:
            font_color = active_font_color
            back_color = active_color
        else:
            font_color = passive_font_color
            back_color = passive_color
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height, text, font_file, font_color, back_color, relative_border_width)
        self.relative_border_width = relative_border_width
        self.active_color = active_color
        self.passive_color = passive_color
        self.active_font_color = active_font_color
        self.passive_font_color = passive_font_color
        self.back_color = back_color
        self.font_color = font_color
        self.active = active
        self.display_rect = pygame.Rect(self.x, self.y, self.display_width, self.height)
        self.fill_rect = pygame.Surface((self.display_width,self.height))
        self.fill_rect.fill(back_color)

    def trigger(self, event):
        # get mouse position
        pos = pygame.mouse.get_pos()
        # when mouse hovers over TextInput and click, TextInput is activated
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if "analytics_by_" in self.name:
                    if not self.display_rect.collidepoint(pos): # inactive
                        self.active = False
                        self.font_color = self.passive_font_color
                        self.text_surface = self.text_font.render(self.text, True, self.font_color)
                        self.back_color = self.passive_color
                    else: # active
                        self.active = True
                        self.font_color = self.active_font_color
                        self.text_surface = self.text_font.render(self.text, True, self.font_color)
                        self.back_color = self.active_color
                        print("\n=>",self.name,self.active)
                        return True
        return False

    def resize(self, new_screen):
        super().resize(new_screen)
        self.display_width = int(self.screen_width * self.relative_display_width)
        self.display_rect = pygame.Rect(self.display_x, self.display_y, self.display_width, self.display_height)


class SingleSelectableTextButton(SelectableTextButton):
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height,
                 text, font_file=None, font_color=pygame.Color("black"), active_color="dodgerblue",
                 passive_color="white", border_width=0):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height,
                         text, font_file, font_color, active_color, passive_color, border_width)

    def trigger(self, event):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # when mouse hovers over TextInput and click, TextInput is activated
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.display_rect.collidepoint(pos):
                    self.active = True
                    self.back_color = self.active_color
                else:
                    self.active = False
                    self.back_color = self.passive_color
                action = True
        return action


class SelectableTextList(MouseScrollableSurface):
    def __init__(self, name, screen, relative_x, relative_y, relative_width, text_relative_height,
                 relative_shown_width, relative_shown_height, text_list, display_screen, on_display=True,
                 single_select=True, font_file=None,
                 font_color=pygame.Color("black"), active_color="dodgerblue", passive_color="white", border_width=0):
        self.text_list = text_list
        self.list_size = len(text_list)
        if len(text_list) == 0:
            relative_height = text_relative_height
        else:
            # height of scroll surface is sum of text height
            relative_height = text_relative_height * self.list_size
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height,
                         relative_shown_width, relative_shown_height, display_screen, on_display)
        self.navigation_surface = False
        self.single_select = single_select
        self.text_relative_x = 0
        self.text_relative_y = 0
        if self.list_size==0:
            self.text_relative_height = 1
            self.text_relative_width = 1
            selectable_text = SingleSelectableTextButton("Nobody's here!", self.surface, self.text_relative_x,
                                                         self.text_relative_y, self.text_relative_width,
                                                         self.text_relative_height, "Nobody's here!", font_file, font_color,
                                                         active_color, passive_color, border_width)
            self.add_component(selectable_text)
        else:
            self.text_relative_height = 1 / self.list_size
            self.text_relative_width = 1
            # for each text, add a selectable text into scrollable
            for text in text_list:
                if self.single_select:
                    selectable_text = SingleSelectableTextButton(text, self.surface, self.text_relative_x,
                                                                 self.text_relative_y, self.text_relative_width,
                                                                 self.text_relative_height, text, font_file, font_color,
                                                                 active_color, passive_color, border_width)
                else:
                    selectable_text = SelectableTextButton(text, self.surface, self.text_relative_x, self.text_relative_y,
                                                           self.text_relative_width, self.text_relative_height, text,
                                                           font_file, font_color, active_color, passive_color, border_width)
                # add y into scrollable
                self.add_component(selectable_text)
                # update y of next text
                self.text_relative_y = self.text_relative_y + self.text_relative_height

            if self.single_select:
                self.selected_text = ""
            else:
                self.selected_text = []

    def trigger(self, event):
        super().trigger(event)

        if self.single_select:
            self.selected_text = ""
        else:
            self.selected_text = []
        for selectable_text in self.components.values():
            if selectable_text.active:
                if self.single_select:
                    self.selected_text = selectable_text.text
                else:
                    self.selected_text.append(selectable_text.text)


class TextboxButtonList(MouseScrollableSurface):
    def __init__(self, name, screen, relative_x, relative_y, relative_width, text_relative_height,
                 relative_shown_width, relative_shown_height, text_list, display_screen, on_display=True,
                 font_file=None,font_color=pygame.Color("black"), back_color="white",
                 border_width=0):
        self.text_list = text_list
        self.list_size = len(text_list)
        if len(text_list) ==0:
            relative_height = text_relative_height
        else:
        # height of scroll surface is sum of text height
            relative_height = text_relative_height * self.list_size
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height,
                         relative_shown_width, relative_shown_height, display_screen, on_display)
        self.text_relative_x = 0
        self.text_relative_y = 0
        if self.list_size == 0:

            self.text_relative_height = 1
            self.text_relative_width = 1
            textbox_button = TextboxButton("Empty!", self.surface, self.text_relative_x, self.text_relative_y,
                                           self.text_relative_width, self.text_relative_height, "Empty!", font_file,
                                           font_color, back_color, border_width)
            self.add_component(textbox_button)

        else:
            self.text_relative_height = 1 / self.list_size
            self.text_relative_width = 1
            # for each text, add a selectable text into scrollable
            for text in text_list:
                textbox_button = TextboxButton(text, self.surface, self.text_relative_x, self.text_relative_y,
                                               self.text_relative_width, self.text_relative_height, text, font_file,
                                               font_color, back_color, border_width)
                # add y into scrollable
                self.add_component(textbox_button)
                # update y of next text
                self.text_relative_y = self.text_relative_y + self.text_relative_height


class ExpandButton(ComponentSurface):
    # fixed shown width and height to 1 single textbox
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height, relative_expand_x,
                 relative_expand_y, relative_expand_width, relative_expand_height, display_screen, on_display=True):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height, display_screen, on_display)


        self.original_relative_x = self.relative_x
        self.original_relative_y = self.relative_y
        self.original_relative_width = self.relative_width
        self.original_relative_height = self.relative_height

        self.relative_expand_x = relative_expand_x
        self.relative_expand_y = relative_expand_y
        self.relative_expand_width = relative_expand_width
        self.relative_expand_height = relative_expand_height

        self.button = ColorButton(name + "_button", self.surface, 0, 0, 1, 1, "white")
        self.add_component(self.button)

        self.expandable_surface = ComponentSurface(name + "_expandable_surface", self.surface, 0, 0, 1, 1,
                                                   display_screen, False)


        self.clicked = False
        # can be expanded
        self.expandable = True
        self.expanded = False

    def expand(self):
        self.relative_x = self.relative_expand_x
        self.relative_y = self.relative_expand_y
        self.relative_width = self.relative_expand_width
        self.relative_height = self.relative_expand_height
        self.relative_display_x = self.relative_x
        self.relative_display_y = self.relative_y
        self.relative_display_width = self.relative_width
        self.relative_display_height = self.relative_height
        self.resize(self.screen)
        self.add_component(self.expandable_surface)
        self.remove_component(self.button.name)
        self.resize(self.screen)
        self.expanded = True

    def collapse(self):
        self.relative_x = self.original_relative_x
        self.relative_y = self.original_relative_y
        self.relative_width = self.original_relative_width
        self.relative_height = self.original_relative_height
        self.relative_display_x = self.relative_x
        self.relative_display_y = self.relative_y
        self.relative_display_width = self.relative_width
        self.relative_display_height = self.relative_height
        self.resize(self.screen)
        self.add_component(self.button)
        self.remove_component(self.expandable_surface.name)
        self.resize(self.screen)
        self.expanded = False

    def trigger(self, event):
        action = False

        if self.expanded:
            super().trigger(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # new left click and not held beforehand
                # get mouse position
                pos = pygame.mouse.get_pos()
                # check mouseover and clicked conditions
                if self.display_rect.collidepoint(pos):
                    if not self.clicked:  # when mouse is on top of button
                        if not self.expanded:
                            self.expand()

                        self.clicked = True  # prevent multiple input by holding click
                else:  # when mouse is not on top of button
                    if self.expanded:
                        self.expandable_surface.trigger(event)
                        self.collapse()
                        self.expanded = False

                self.resize(self.screen)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # when left click is let go
                self.clicked = False  # set click to false

        return action

    def resize(self, new_screen):
        super().resize(new_screen)




# dropdown
class DropdownTextSelect(ExpandButton):
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height,
                 text_list, prompt, num_expand_text, display_screen, single_select=True, on_display=True, font_file=None,
                 font_color="black", active_color="dodgerblue", passive_color="white", border_width=0):
        relative_expand_height = (num_expand_text+1) * relative_height
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height, relative_x,
                         relative_y, relative_width, relative_expand_height, display_screen, on_display)

        self.navigation_surface = False
        relative_text_height = 1 / (num_expand_text + 1)
        selectable_text_list_relative_height = 1 - relative_text_height

        self.prompt = prompt
        self.selected_text = prompt
        self.button = TextboxButton(name + "_button", self.surface, 0, 0,
                                    1, 1, self.selected_text, font_file, font_color)
        self.remove_component(self.button.name)
        self.add_component(self.button)

        self.selected_textbox = TextboxButton(name+"_selected_text_display", self.expandable_surface.surface, 0, 0,
                                                 1, relative_text_height, self.selected_text, font_file, font_color)
        self.expandable_surface.add_component(self.selected_textbox)

        self.selectable_text_list = SelectableTextList(name+"_selectable_text_list", self.expandable_surface.surface, 0,
                                                       relative_text_height, 1, relative_text_height, 1,
                                                       selectable_text_list_relative_height, text_list, display_screen,
                                                       False,single_select=single_select, font_file=font_file,
                                                       font_color=font_color,
                                                       active_color=active_color, passive_color=passive_color,
                                                       border_width=border_width)
        self.expandable_surface.add_component(self.selectable_text_list)

    def trigger(self, event):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        if self.expanded:
            self.triggered_component_list.clear()
            # get mouse position

            if event.type == pygame.MOUSEBUTTONDOWN:
                # check mouseover and clicked conditions
                if self.display_rect.collidepoint(pos):  # when mouse is on top of button
                    for component in self.components.values():
                        if component.trigger(event):
                            self.triggered_component_list.append(component)
                            action = True
                        if component.name == self.expandable_surface.name:

                            for expandable_component in component.components.values():

                                if expandable_component.name == self.selectable_text_list.name:
                                    for selectable_text in expandable_component.components.values():
                                        if selectable_text.active:
                                            self.button.text = selectable_text.text
            else:
                for component in self.components.values():
                    if component.trigger(event):
                        self.triggered_component_list.append(component)
                        action = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # new left click and not held beforehand

                if not self.expanded:

                    # check mouseover and clicked conditions
                    if self.display_rect.collidepoint(pos):
                        if not self.clicked:  # when mouse is on top of button
                            self.expand()

                        self.clicked = True  # prevent multiple input by holding click
                else:  # when mouse is not on top of button
                    if not self.selected_textbox.display_rect.collidepoint(pos):
                        self.expandable_surface.trigger(event)
                        self.collapse()
                        self.expanded = False

                self.resize(self.screen)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # when left click is let go
                self.clicked = False  # set click to false

        return action

#dropdown that changes with user input
class DynamicDropdownTextSelect(ExpandButton):
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height,
                 text_list, prompt, num_expand_text, display_screen, single_select=True, on_display=True, font_file=None,
                 font_color="black", active_color="dodgerblue", passive_color="white", border_width=0):
        relative_expand_height = (num_expand_text+1) * relative_height
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height, relative_x,
                         relative_y, relative_width, relative_expand_height, display_screen, on_display)

        self.navigation_surface = False
        relative_text_height = 1 / (num_expand_text + 1)
        selectable_text_list_relative_height = 1 - relative_text_height

        self.prompt = prompt
        self.selected_text = prompt
        self.button = TextboxButton(name + "_button", self.surface, 0, 0,
                                    1, 1, self.selected_text, font_file, font_color)
        self.remove_component(self.button.name)
        self.add_component(self.button)

        self.selected_textbox = TextboxButton(name+"_selected_text_display", self.expandable_surface.surface, 0, 0,
                                                 1, relative_text_height, self.selected_text, font_file, font_color)
        self.expandable_surface.add_component(self.selected_textbox)

        self.selectable_text_list = SelectableTextList(name+"_selectable_text_list", self.expandable_surface.surface, 0,
                                                       relative_text_height, 1, relative_text_height, 1,
                                                       selectable_text_list_relative_height, text_list, display_screen,
                                                       False,single_select=single_select, font_file=font_file,
                                                       font_color=font_color,
                                                       active_color=active_color, passive_color=passive_color,
                                                       border_width=border_width)
        self.expandable_surface.add_component(self.selectable_text_list)

    def trigger(self, event):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        if self.expanded:
            self.navigation_surface = True
            self.triggered_component_list.clear()
            # get mouse position

            if event.type == pygame.MOUSEBUTTONDOWN:
                # check mouseover and clicked conditions
                if self.display_rect.collidepoint(pos):  # when mouse is on top of button
                    for component in self.components.values():
                        if component.trigger(event):
                            self.triggered_component_list.append(component)
                            action = True
                        if component.name == self.expandable_surface.name:

                            for expandable_component in component.components.values():

                                if expandable_component.name == self.selectable_text_list.name:
                                    for selectable_text in expandable_component.components.values():
                                        if selectable_text.active:
                                            self.button.text = selectable_text.text
            else:
                for component in self.components.values():
                    if component.trigger(event):
                        self.triggered_component_list.append(component)
                        action = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # new left click and not held beforehand

                if not self.expanded:

                    # check mouseover and clicked conditions
                    if self.display_rect.collidepoint(pos):
                        if not self.clicked:  # when mouse is on top of button
                            self.expand()

                        self.clicked = True  # prevent multiple input by holding click
                else:  # when mouse is not on top of button
                    if not self.selected_textbox.display_rect.collidepoint(pos):
                        self.expandable_surface.trigger(event)
                        self.collapse()
                        self.expanded = False

                self.resize(self.screen)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # when left click is let go
                self.clicked = False  # set click to false

        return action
# add textInput to screen
'''
class for textInput component
same parameters as parent class Component with some additional parameters

color - color of textbox when it is active/selected
color passive_color - color of textbox when it is passive/deselected
string font_file - directory file path to font_file - default none
color font_color - color of text - default black
float relative_border_width - set boarder width relative to textbox height - default none
'''


class TextInput(Component):
    # textbox constructor
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height, active_color="gray80",
                 passive_color="white", font_file=None, font_color=pygame.Color("black"), relative_border_width=0):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height)

        self.active = False
        self.input = ""
        self.active_color = pygame.Color(active_color)  # color of TextInput when it is selected
        self.passive_color = pygame.Color(passive_color)  # color of TextInput when it is deselected
        self.color = passive_color  # default color is passive

        self.font_file = font_file  # font file to be used
        self.font_size = int(self.height)  # font size height = 3/4 pixel height
        self.text_font = pygame.font.Font(font_file, self.font_size)  # create pygame FONT
        self.font_color = font_color  # font color
        self.text_offset = int(self.height / 8)  # height offset so text is in middle
        self.display_text = self.input  # text that is displayed
        self.text_surface = self.text_font.render(self.display_text, True, self.font_color)
        self.max_text_width = self.width - (2 * self.text_offset)  # maximum text length to fit

        self.relative_border_width = relative_border_width  # scale border width of TextInput box
        self.border_width = relative_border_width * self.height  # set border width

        self.mouse_function = True  # can be clicked
        self.keyboard_function = True  # react to keystrokes
        self.hold_return = False  # variable to prevent holding RETURN

    # blit component onto screen
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, self.border_width)
        self.text_surface = self.text_font.render(self.input, True, self.font_color)

        # slice display text until it fits within Textbox
        char_hidden = 0
        while self.text_surface.get_width() >= self.max_text_width:
            self.display_text = self.input[char_hidden:]
            self.text_surface = self.text_font.render(self.display_text, True, self.font_color)
            char_hidden += 1

        self.screen.blit(self.text_surface, (self.x + self.text_offset, self.y + self.text_offset))

    # returns True if RETURN is keyed while TextInput is active
    def trigger(self, event):

        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # when mouse hovers over TextInput and click, TextInput is activated
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.display_rect.collidepoint(pos):
                    self.active = True
                    self.color = self.active_color
                else:
                    self.active = False
                    self.color = self.passive_color

        # when TextInput is activated, add key pressed into input
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.input = self.input[:-1]
                elif event.key == pygame.K_TAB:
                    pass
                elif event.key == pygame.K_RETURN:
                    if not self.hold_return:
                        self.hold_return = True
                        action = True
                else:
                    self.input += event.unicode

        # prevent multiple returns while holding the RETURN key
        if event.type == pygame.KEYUP:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.hold_return = False

        return action

    # additional variables to resize not covered by parent resize
    def resize(self, new_screen):
        super().resize(new_screen)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.x = self.x
        self.rect.y = self.y

        self.font_size = int(self.height)
        self.text_font = pygame.font.Font(self.font_file, self.font_size)
        self.text_offset = int(self.height / 8)
        self.max_text_width = self.width - (2 * self.text_offset)

        self.border_width = int(self.relative_border_width * self.height)
