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
        self.relative_x = relative_x                                # relative x position
        self.relative_y = relative_y                                # relative y position
        self.relative_width = relative_width                        # relative width
        self.relative_height = relative_height                      # relative height
        self.screen = screen                                        # screen component is on
        self.screen_width = screen.get_width()                      # screen width
        self.screen_height = screen.get_height()                    # screen height
        self.x = int(self.screen_width * relative_x)                # x position of component after scaling
        self.y = int(self.screen_height * relative_y)               # y position of component after scaling
        self.width = int(self.screen_width * relative_width)        # width of component after scaling
        self.height = int(self.screen_height * relative_height)     # height of component after scaling
        self.mouse_function = False                                 # Can component interact with mouse
        self.keyboard_function = False                              # Can component interact with keyboard

    # blit component onto screen
    def draw(self):
        self.screen.blit(self.screen, self.color, self.rect, self.border_width)

    # resize component when screen is resized
    # new dimensions and coordinates are rescaled with relative position/dimensions
    # child class may have other variables that needs to be resized
    def resize(self, new_screen):
        self.screen = new_screen
        self.screen_width = new_screen.get_width()
        self.screen_height = new_screen.get_height()
        self.x = int(self.screen_width * self.relative_x)
        self.y = int(self.screen_height * self.relative_y)
        self.width = int(self.screen_width * self.relative_width)
        self.height = int(self.screen_height * self.relative_height)

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
        self.image = image                          # image used for button
        self.scaled_image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = self.scaled_image.get_rect()    # initialize image as rect in pygame
        self.rect.x = self.x                        # initialize button x-coordinates
        self.rect.y = self.y                        # initialize button y-coordinates

    # draw the button on the screen
    def draw(self):
        self.screen.blit(self.scaled_image, self.rect)

    # additional variables to resize not covered by parent resize
    def resize(self, new_screen):
        super().resize(new_screen)
        self.scaled_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.scaled_image.get_rect()  # initialize image as rect in pygame
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
        if self.rect.collidepoint(pos):  # when mouse is on top of button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not self.clicked:  # new left click and not held beforehand
                    action = True  # trigger action
                    self.clicked = True  # prevent multiple input by holding click

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


class TextInput(Component):
    # textbox constructor
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height, active_color="gray80",
                 passive_color="white", font_file=None, font_color=pygame.Color("black"), relative_border_width=0):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.active = False
        self.input = ""
        self.active_color = pygame.Color(active_color)                  # color of TextInput when it is selected
        self.passive_color = pygame.Color(passive_color)                # color of TextInput when it is deselected
        self.color = passive_color                                      # default color is passive

        self.font_file = font_file                                      # font file to be used
        self.font_size = int(self.height)                               # font size height = 3/4 pixel height
        self.text_font = pygame.font.Font(font_file, self.font_size)    # create pygame FONT
        self.font_color = font_color                                    # font color
        self.text_offset = int(self.height / 8)                         # height offset so text is in middle
        self.display_text = self.input                                  # text that is displayed
        self.text_surface = self.text_font.render(self.display_text, True, self.font_color)
        self.max_text_width = self.width - (2 * self.text_offset)       # maximum text length to fit

        self.relative_border_width = relative_border_width              # scale border width of TextInput box
        self.border_width = relative_border_width * self.height         # set border width

        self.mouse_function = True                                      # can be clicked
        self.keyboard_function = True                                   # react to keystrokes
        self.hold_return = False                                        # variable to prevent holding RETURN

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
                if self.rect.collidepoint(pos):
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


# add a scrollable image on screen
class ScrollableImage(ImageDisplay):
    def __init__(self, name, screen, relative_x, relative_y, relative_width,
                 relative_height, image, scroll_axis_y=True):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height, image)

        self.surface = pygame.Surface((self.width, self.height))    # surface of scrollable
        self.rect = self.surface.get_rect()                         # rect of surface
        self.rect.x = self.x                                        # x position of surface
        self.rect.y = self.y                                        # y position of surface

        self.display_image = image                                  # image used
        self.scroll_axis_y = scroll_axis_y                          # axis of scrolling

        self.image_ratio = image.get_width()/image.get_height()     # original image ratio
        # scale image dimension based on scroll axis
        if self.scroll_axis_y:
            self.image_width = self.width
            self.image_height = int(self.width / self.image_ratio)
        else:
            self.image_height = self.height
            self.image_width = int(self.height * self.image_ratio)

        self.display_image = pygame.transform.scale(image, (self.image_width, self.image_height))
        self.display_image_x = 0                                 # x position of image within scrollable surface
        self.display_image_y = 0                                 # y position of image within scrollable surface

    # blit component onto screen
    def draw(self):
        self.surface.blit(self.display_image, (self.display_image_x, self.display_image_y))
        self.screen.blit(self.surface, (self.x, self.y))

    # additional variables to resize not covered by parent resize
    def resize(self, new_screen):
        super().resize(new_screen)
        self.surface = pygame.Surface((self.width, self.height))

        # rescale image width/height based on scroll axis
        if self.scroll_axis_y:
            self.image_width = self.width
            self.image_height = int(self.width / self.image_ratio)
            if self.display_image_y >= 0:
                self.display_image_y = 0
            if self.display_image_y <= self.height - self.image_height:
                self.display_image_y = self.height - self.image_height
        else:
            self.image_height = self.height
            self.image_width = int(self.height * self.image_ratio)
            if self.display_image_x >= 0:
                self.display_image_x = 0
            if self.display_image_x <= self.width - self.image_width:
                self.display_image_x = self.width - self.image_width

        self.display_image = pygame.transform.scale(self.image, (self.image_width, self.image_height))


# mouse controlled scrollable image
class MouseScrollableImage(ScrollableImage):
    def __init__(self, name, screen, relative_x, relative_y, relative_width,
                 relative_height, image, scroll_axis_y=True, relative_scroll_length=1 / 8):
        super().__init__(name, screen, relative_x, relative_y, relative_width,
                         relative_height, image, scroll_axis_y)

        self.relative_scroll_length = relative_scroll_length        # scroll length per wheel tick

        if self.scroll_axis_y:
            self.scroll_length = self.relative_scroll_length * self.height
        else:
            self.scroll_length = self.relative_scroll_length * self.width

    def trigger(self, event):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):  # when mouse is on top of button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # wheel roll up
                    if self.scroll_axis_y:
                        if self.display_image_y + self.scroll_length >= 0:
                            self.display_image_y = 0
                        else:
                            self.display_image_y += self.scroll_length
                    else:
                        if self.display_image_x + self.scroll_length >= 0:
                            self.display_image_x = 0
                        else:
                            self.display_image_x += self.scroll_length
                elif event.button == 5:  # wheel roll down
                    if self.scroll_axis_y:
                        if self.display_image_y - self.scroll_length <= self.height - self.image_height:
                            self.display_image_y = self.height - self.image_height
                        else:
                            self.display_image_y -= self.scroll_length
                    else:
                        if self.display_image_x - self.scroll_length <= self.width - self.image_width:
                            self.display_image_x = self.width - self.image_width
                        else:
                            self.display_image_x -= self.scroll_length
                print(self.display_image_x, self.display_image_y)

    # additional variables to resize not covered by parent resize
    def resize(self, new_screen):
        super().resize(new_screen)
        if self.scroll_axis_y:
            self.scroll_length = int(self.relative_scroll_length * new_screen.get_height())
        else:
            self.scroll_length = int(self.relative_scroll_length * new_screen.get_width())


# display text on screen
class TextDisplay(Component):
    def __init__(self, name, screen, relative_x, relative_y, relative_width, relative_height,
                 text, font_file=None, font_color=pygame.Color("black")):
        super().__init__(name, screen, relative_x, relative_y, relative_width, relative_height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # font initialization
        self.font_file = font_file
        self.font_size = int(self.height * 4 / 3)   # font to height pixel ratio = 4:3 so we get font size from height
        self.text_font = pygame.font.Font(font_file, self.font_size)
        self.font_color = font_color
        self.text = text
        self.text_surface = self.text_font.render(self.text, True, self.font_color)

        # make sure text surface fits in dimensions aka reduce font size until width fits
        while self.text_surface.get_width() >= self.width:
            self.font_size -= 1
            self.text_font = pygame.font.Font(font_file, self.font_size)
            self.text_surface = self.text_font.render(self.text, True, self.font_color)

    # blit component onto screen
    def draw(self):
        self.screen.blit(self.text_surface, (self.x, self.y))

    # additional variables to resize not covered by parent resize
    def resize(self, new_screen):
        super().resize(new_screen)
        self.font_size = int(self.height)
        self.text_font = pygame.font.Font(self.font_file, self.font_size)
        self.text_surface = self.text_font.render(self.text, True, self.font_color)


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
        if self.rect.collidepoint(pos):  # when mouse is on top of button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not self.clicked:  # new left click and not held beforehand
                    action = True  # trigger action
                    self.clicked = True  # prevent multiple input by holding click

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # when left click is let go
                self.clicked = False  # set click to false

        return action
