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
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height):
        self.name = name
        self.relative_x = relative_x
        self.relative_y = relative_y
        self.relative_width = relative_width
        self.relative_height = relative_height
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.x = int(self.screen_width * relative_x)
        self.y = int(self.screen_height * relative_y)
        self.width = int(self.screen_width * relative_width)
        self.height = int(self.screen_height * relative_height)
        self.mouse_function = False
        self.keyboard_function = False

    def draw(self):
        self.screen.blit(self.screen, self.color, self.rect, self.border_width)

    def resize(self, new_screen):
        self.screen = new_screen
        self.screen_width = new_screen.get_width()
        self.screen_height = new_screen.get_height()
        self.x = int(self.screen_width * self.relative_x)
        self.y = int(self.screen_height * self.relative_y)
        self.width = int(self.screen_width * self.relative_width)
        self.height = int(self.screen_height * self.relative_height)

    def trigger(self, event):
        return False


# create a button from an image
'''
class for button component
same parameters as parent class Component except image
pygame.Surface image - the image used to make the button
'''


class Button(Component):
    # button constructor
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height, image):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height)
        self.image = image  # image used for button
        self.scaled_image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = self.scaled_image.get_rect()  # initialize image as rect in pygame
        self.rect.x = self.x  # initialize button x-coordinates
        self.rect.y = self.y  # initialize button y-coordinates
        self.mouse_function = True
        self.clicked = False  # initialize if button is clicked to false

    # draw the button on the screen
    def draw(self):
        self.screen.blit(self.scaled_image, self.rect)

    # return true if button is clicked
    def trigger(self, event):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):  # when mouse is on top of button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not self.clicked:  # new left click and not held beforehand
                    action = True  # trigger action
                    self.clicked = True  # prevent multiple input by holding click

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # when left click is let go
                self.clicked = False  # set click to false

        return action

    def resize(self, new_screen):
        super().resize(new_screen)
        self.scaled_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.scaled_image.get_rect()  # initialize image as rect in pygame
        self.rect.x = self.x  # initialize button x-coordinates
        self.rect.y = self.y  # initialize button y-coordinates


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

    def draw(self):
        self.screen.blit(self.scaled_image, (self.x, self.y))

    def resize(self, new_screen):
        super().resize(new_screen)
        self.scaled_image = pygame.transform.scale(self.image, (self.width, self.height))


# add textbox to screen
'''
class for textbox component
same parameters as parent class Component with some additional parameters

color - color of textbox when it is active/selected
color passive_color - color of textbox when it is passive/deselected
string font_file - directory file path to font_file - default none
color font_color - color of text - default black
float relative_border_width - set boarder width relative to textbox height - default none
'''


class Textbox(Component):
    # textbox constructor
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height, active_color="gray80",
                 passive_color="white", font_file=None, font_color=pygame.Color("black"), relative_border_width=0):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.active = False
        self.input = ""
        self.active_color = pygame.Color(active_color)
        self.passive_color = pygame.Color(passive_color)
        self.color = passive_color

        self.font_file = font_file
        self.font_size = int(self.height)
        self.text_font = pygame.font.Font(font_file, self.font_size)
        self.font_color = font_color
        self.text_offset = int(self.height / 8)
        self.display_text = self.input
        self.text_surface = self.text_font.render(self.display_text, True, self.font_color)
        self.max_text_width = self.width - (2 * self.text_offset)

        self.relative_border_width = relative_border_width
        self.border_width = relative_border_width * self.height

        self.mouse_function = True
        self.keyboard_function = True
        self.hold_return = False

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, self.border_width)
        self.text_surface = self.text_font.render(self.input, True, self.font_color)

        char_hidden = 0
        while self.text_surface.get_width() >= self.max_text_width:
            self.display_text = self.input[char_hidden:]
            self.text_surface = self.text_font.render(self.display_text, True, self.font_color)
            char_hidden += 1

        self.screen.blit(self.text_surface, (self.x + self.text_offset, self.y + self.text_offset))

    def trigger(self, event):

        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(pos):
                    self.active = True
                    self.color = self.active_color
                else:
                    self.active = False
                    self.color = self.passive_color

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.input = self.input[:-1]
                    print(self.input + "|")
                elif event.key == pygame.K_TAB:
                    pass
                elif event.key == pygame.K_RETURN:
                    if not self.hold_return:
                        self.hold_return = True
                        action = True
                else:
                    self.input += event.unicode
                    print(self.input + "|")

        if event.type == pygame.KEYUP:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.hold_return = False

        return action

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


class Scrollable(Component):
    def __init__(self, name, screen, relative_x, relative_y, relative_width,
                 relative_height, image, scroll_axis="y", scroll_factor=0):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height)

        self.surface = pygame.Surface((self.width, self.height))
        self.rect = self.surface.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.mouse_function = True

        self.active = False

        self.image = image
        self.display_image = image
        self.scroll_axis = scroll_axis
        image_ratio = image.get_width()/image.get_height()
        if self.scroll_axis == "y":
            self.image_width = self.width
            self.image_height = int(self.width / image_ratio)
        else:
            self.image_height = self.height
            self.image_width = int(self.height * image_ratio)
        self.scaled_image = pygame.transform.scale(image, (self.image_width, self.image_height))
        self.display_image = pygame.transform.scale(image, (self.image_width, self.image_height))
        self.display_image_x = 0
        self.display_image_y = 0

    def draw(self):
        self.surface.blit(self.display_image, (self.display_image_x, self.display_image_y))
        self.screen.blit(self.surface, (self.x, self.y))
        pass

    def trigger(self, event):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):  # when mouse is on top of button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # wheel roll up
                    if self.scroll_axis == "y":
                        self.display_image.scroll(0, 10)
                        self.display_image_y += 10
                    else:
                        self.display_image.scroll(10, 0)
                        self.display_image_x += 10
                    print("scrolled up")
                elif event.button == 5:  # wheel roll down
                    if self.scroll_axis == "y":
                        self.display_image.scroll(0, -10)
                        self.display_image_y -= 10
                    else:
                        self.display_image.scroll(-10, 0)
                        self.display_image_x -= 10
                    print("scrolled down")
                print(self.display_image_x, self.display_image_y)

        pass

    def resize(self):
        pass
