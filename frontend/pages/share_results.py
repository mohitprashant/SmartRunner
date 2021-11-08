import pygame
from assets.components import *
from page import *


class ShareResultsPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "share_results"
        self.input_data = {
            "roomID": "RoomID",                     #for end screen
            "username": "username",
            "topic_leaderboard_ID":"",              #for topic leaderboard
            "score_board": [],                      #for end screen
            "back_navigation": ""
        }
        self.output_data = {
            "roomID": "",
            "prev_page": "",
            "score_board": [],
            "username": "",
            "topic_leaderboard_ID": "",
            # "back_navigation":"",
            "exit": False
        }

        # set all component variables on input screen

    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/Backgrounds/sharebg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # # toggle test
        # toggle_rel_x = 9 / 20
        # toggle_rel_y = 1 / 20
        # toggle_rel_width = 1 / 10
        # toggle_rel_height = 1 / 10
        # toggle_image = pygame.image.load('assets/img/save_btn.png')
        # toggle_image2 = pygame.image.load('assets/img/load_btn.png')
        # toggle_password = ToggleButton("toggle", screen, toggle_rel_x, toggle_rel_y, toggle_rel_width, toggle_rel_height,
        #                       toggle_image, toggle_image2)
        # self.components["toggle"] = toggle_password

        share_results_display_x = 4 / 20
        share_results_display_y = 3 / 40
        share_results_display_width = 1 / 2
        share_results_display_height = 0.2
        share_results_text = pygame.image.load('assets/Backgrounds/shareresults.png')
        share_results_display = ImageDisplay("share_results_display", screen, share_results_display_x,
                                             share_results_display_y, share_results_display_width,
                                             share_results_display_height, share_results_text)
        self.components["share_results_display"] = share_results_display

        # Twitter Button
        twitter_button_x = 3 / 20
        twitter_button_y = 0.4
        twitter_button_width = 1 / 4
        twitter_button_height = 0.30
        twitter_button_img = pygame.image.load('assets/Buttons/btn_twitter.png')
        twitter_button2 = ImageButton("twitter_button", screen, twitter_button_x, twitter_button_y,
                                         twitter_button_width,
                                         twitter_button_height, twitter_button_img)
        self.components["twitter_button"] = twitter_button2


        # Facebook Button
        facebook_button_x = 10 / 20
        facebook_button_y = 0.4
        facebook_button_width = 1 / 4
        facebook_button_height = 0.3
        facebook_button_img = pygame.image.load('assets/Buttons/btn_fb.png')
        facebook_button = ImageButton("facebook_button", screen, facebook_button_x, facebook_button_y,
                                      facebook_button_width,
                                      facebook_button_height, facebook_button_img)
        self.components["facebook_button"] = facebook_button

        # return button
        return_button_x = 17 / 20
        return_button_y = 17 / 20
        return_button_width = 1 / 10
        return_button_height = 1 / 10
        return_button__img = pygame.image.load('assets/Buttons/btn_back.png')
        return_button2 = ImageButton("return_button", screen, return_button_x, return_button_y,
                                    return_button_width,
                                    return_button_height, return_button__img)
        self.components["return_button"] = return_button2



        # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            # self.output_data["back_navigation"]=self.output_data["prev_page"]
            #test
            # print("test", self.output_data["back_navigation"])
            self.output_data["prev_page"] = self.output_data["current_page"]
            # self.output_data["roomID"] = self.input_data["roomID"]
            # self.output_data["score_board"] = self.input_data["score_board"]
            self.output_data["username"] = self.input_data["username"]
            if triggered_component in [self.components["twitter_button"]]:
                print("open twitter")
            if triggered_component in [self.components["facebook_button"]]:
                print("open facebook")
            if triggered_component in [self.components["return_button"]]:
                print("test", self.input_data["back_navigation"])
                if self.input_data["back_navigation"] == "topic_leaderboard":
                    self.output_data["topic_leaderboard_ID"] = self.input_data["topic_leaderboard_ID"]
                    self.name = self.input_data["back_navigation"]
                elif self.input_data["back_navigation"] == "end_screen":
                    self.output_data["score_board"] = self.input_data["score_board"]
                    self.output_data["roomID"]=self.input_data["roomID"]
                    self.name = self.input_data["back_navigation"]




