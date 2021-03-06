import pygame
import sys
import pathlib

sys.path.insert(0, '../../backend/account')
sys.path.insert(1, '../../frontend/pages')
import AccountHelper

from assets.components import *
from page import *


curr_dir = str(pathlib.Path(__file__).parent.resolve()) + '/'


class CustomizePage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "customize"
        self.input_data = {
            "back_navigation":"",
            "username": "",
            "prev_page": ""
        }
        self.output_data = {
            "back_navigation": "",
            "current_page": self.name,
            "prev_page": "",
            "username": "",
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        self.name = "main_menu"

        # change back navigation every time page changes
        if self.input_data["prev_page"]!=self.name:
            self.output_data["back_navigation"]=self.input_data["prev_page"]

        # background
        bg_img = pygame.image.load(curr_dir + 'assets/Backgrounds/gamebg.jpeg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        header_image_rel_x = 0.2
        header_image_rel_y = 0.15
        header_image_rel_width = 0.6
        header_image_rel_height = 0.3
        header_img = pygame.image.load('assets/Backgrounds/chooseavatar.png')
        customize_header_image = ImageDisplay("customize_header_image", screen, header_image_rel_x, header_image_rel_y,
                                              header_image_rel_width, header_image_rel_height, header_img)
        self.components["customize_header_image"] = customize_header_image

        sprite1_button_rel_x = 2 / 15
        sprite1_button_rel_y = 0.45
        sprite1_button_rel_width = 0.2
        sprite1_button_rel_height = 0.3
        sprite1_button_img = pygame.image.load(curr_dir + 'assets/Sprites/Pink_Monster.png')
        sprite1_button_img = ImageButton("sprite1_button_img", screen, sprite1_button_rel_x, sprite1_button_rel_y,
                                         sprite1_button_rel_width, sprite1_button_rel_height, sprite1_button_img)
        self.components["sprite1_button_img"] = sprite1_button_img

        sprite2_button_rel_x = 6/15
        sprite2_button_rel_y = 0.45
        sprite2_button_rel_width = 0.2
        sprite2_button_rel_height = 0.3
        sprite2_button_img = pygame.image.load(curr_dir + 'assets/Sprites/Owlet_Monster.png')
        sprite2_button_img = ImageButton("sprite2_button_img", screen, sprite2_button_rel_x, sprite2_button_rel_y,
                                         sprite2_button_rel_width, sprite2_button_rel_height, sprite2_button_img)
        self.components["sprite2_button_img"] = sprite2_button_img

        sprite3_button_rel_x = 10/15
        sprite3_button_rel_y = 0.45
        sprite3_button_rel_width = 0.2
        sprite3_button_rel_height = 0.3
        sprite3_button_img = pygame.image.load(curr_dir + 'assets/Sprites/Dude_Monster.png')
        sprite3_button_img = ImageButton("sprite3_button_img", screen, sprite3_button_rel_x, sprite3_button_rel_y,
                                         sprite3_button_rel_width, sprite3_button_rel_height, sprite3_button_img)
        self.components["sprite3_button_img"] = sprite3_button_img

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["username"] = self.input_data["username"]

            if triggered_component in [self.components["sprite1_button_img"]]:
                self.output_data["avatar"] = "Pink_Monster"
                avatar = AccountHelper.set_avatar(self.output_data["username"],self.output_data["avatar"])
                self.name= "main_menu"
            elif triggered_component in [self.components["sprite2_button_img"]]:
                self.output_data["avatar"] = "Owlet_Monster"
                avatar = AccountHelper.set_avatar(self.output_data["username"],self.output_data["avatar"])
                self.name= "main_menu"
            elif triggered_component in [self.components["sprite3_button_img"]]:
                self.output_data["avatar"] = "Dude_Monster"
                avatar = AccountHelper.set_avatar(self.output_data["username"],self.output_data["avatar"])
                self.name= "main_menu"
