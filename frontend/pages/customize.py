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

        #change back navigation every time page changes
        if self.input_data["prev_page"]!=self.name:
            self.output_data["back_navigation"]=self.input_data["prev_page"]
            print("main change")

        # background
        bg_img = pygame.image.load(curr_dir + 'assets/Backgrounds/gamebg.jpeg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        header_image_rel_x = 0.35
        header_image_rel_y = 0.2
        header_image_rel_width = 0.25
        header_image_rel_height = 0.15
        header_img = pygame.image.load('assets/Backgrounds/leaderboards.png')
        customize_header_image = ImageDisplay("customize_header_image", screen, header_image_rel_x,
                                               header_image_rel_y,
                                               header_image_rel_width,
                                               header_image_rel_height, header_img)
        self.components["customize_header_image"] = customize_header_image

        sprite1_button_rel_x = 2 / 15
        sprite1_button_rel_y = 0.45
        sprite1_button_rel_width = 1 / 7
        sprite1_button_rel_height = 0.3
        sprite1_button_img = pygame.image.load(curr_dir + 'assets/Sprites/Pink_Monster.png')
        sprite1_button_img = ImageButton("sprite1_button_img", screen, sprite1_button_rel_x, sprite1_button_rel_y,
                                  sprite1_button_rel_width,
                                  sprite1_button_rel_height, sprite1_button_img)
        self.components["sprite1_button_img"] = sprite1_button_img

        sprite2_button_rel_x =  6/ 15
        sprite2_button_rel_y = 0.45
        sprite2_button_rel_width = 1 / 7
        sprite2_button_rel_height = 0.3
        sprite2_button_img = pygame.image.load(curr_dir + 'assets/Sprites/Owlet_Monster.png')
        sprite2_button_img = ImageButton("sprite2_button_img", screen, sprite2_button_rel_x, sprite2_button_rel_y,
                                         sprite2_button_rel_width,
                                         sprite2_button_rel_height, sprite2_button_img)
        self.components["sprite2_button_img"] = sprite2_button_img

        sprite3_button_rel_x = 10/15
        sprite3_button_rel_y = 0.45
        sprite3_button_rel_width = 1 / 7
        sprite3_button_rel_height = 0.3
        sprite3_button_img = pygame.image.load(curr_dir + 'assets/Sprites/Dude_Monster.png')
        sprite3_button_img = ImageButton("sprite3_button_img", screen, sprite3_button_rel_x, sprite3_button_rel_y,
                                         sprite3_button_rel_width,
                                         sprite3_button_rel_height, sprite3_button_img)
        self.components["sprite3_button_img"] = sprite3_button_img

        # sprite4_button_rel_x = 8 / 15
        # sprite4_button_rel_y = 0.6
        # sprite4_button_rel_width = 1 / 7
        # sprite4_button_rel_height = 1 / 7
        # sprite4_button_img = pygame.image.load(curr_dir + 'assets/img/guy0.png')
        # sprite4_button_img = ImageButton("sprite4_button_img", screen, sprite4_button_rel_x, sprite4_button_rel_y,
        #                                  sprite4_button_rel_width,
        #                                  sprite4_button_rel_height, sprite4_button_img)
        # self.components["sprite4_button_img"] = sprite4_button_img

        # exit_button_rel_x = 1 / 15
        # exit_button_rel_y = 4 / 5
        # exit_button_rel_width = 1 / 7
        # exit_button_rel_height = 1 / 7
        # exit_button_img = pygame.image.load(curr_dir + 'assets/Buttons/btn_back.png')
        # exit_button = ImageButton("exit_button", screen, exit_button_rel_x, exit_button_rel_y,
        #                           exit_button_rel_width,
        #                            exit_button_rel_height, exit_button_img)
        # self.components["exit_button"] = exit_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["username"] = self.input_data["username"]
            # if triggered_component in [self.components["exit_button"]]:
            #     self.name = "main_menu"
            if triggered_component in [self.components["sprite1_button_img"]]:
                self.output_data["avatar"] = "Pink_Monster"
                avatar = AccountHelper.set_avatar(self.output_data["username"],self.output_data["avatar"])
                self.name= "main_menu"
            elif triggered_component in [self.components["sprite2_button_img"]]:
                self.output_data["avatar"] = "Owlet_Monster"
                print(type(self.output_data["username"]),type(self.output_data["avatar"]))
                avatar = AccountHelper.set_avatar(self.output_data["username"],self.output_data["avatar"])
                self.name= "main_menu"
            elif triggered_component in [self.components["sprite3_button_img"]]:
                self.output_data["avatar"] = "Dude_Monster"
                avatar = AccountHelper.set_avatar(self.output_data["username"],self.output_data["avatar"])
                self.name= "main_menu"
            # elif triggered_component in [self.components["sprite4_button_img"]]:
            #     self.output_data["avatar"] = "4"
            #     avatar = AccountHelper.set_avatar(self.output_data["username"],self.output_data["avatar"])
            #     self.name= "main_menu"
