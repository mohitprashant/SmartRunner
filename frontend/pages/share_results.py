import pygame
from assets.components import *
from page import *
import webbrowser
import os
import facebook as fb


class ShareResultsPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "share_results"
        self.input_data = {
            "roomID": "RoomID",  # for end screen
            "username": "username",
            "topic": "",  # for topic leaderboard
            "subject": "",  # for topic leaderboard
            "back_navigation": "",
            "prev_page": ""
        }
        self.output_data = {
            "roomID": "",
            "prev_page": "",
            "username": "",
            "topic_leaderboard_ID": "",
            "back_navigation": "",
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        self.name = "share_results"
        # change back navigation every time page changes
        if self.input_data["prev_page"] != self.name:
            self.output_data["back_navigation"] = self.input_data["prev_page"]

        # background
        bg_img = pygame.image.load('assets/Backgrounds/sharebg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        share_results_display_x = 6 / 20
        share_results_display_y = 3 / 40
        share_results_display_width = 1 / 3
        share_results_display_height = 0.18
        share_results_text = pygame.image.load('assets/Backgrounds/shareresults.png')
        share_results_display = ImageDisplay("share_results_display", screen, share_results_display_x,
                                             share_results_display_y, share_results_display_width,
                                             share_results_display_height, share_results_text)
        self.components["share_results_display"] = share_results_display

        # Twitter Button
        twitter_button_x = 0.24
        twitter_button_y = 0.4
        twitter_button_width = 1 / 6
        twitter_button_height = 0.2
        twitter_button_img = pygame.image.load('assets/Buttons/btn_twitter.png')
        twitter_button2 = ImageButton("twitter_button", screen, twitter_button_x, twitter_button_y,
                                      twitter_button_width, twitter_button_height, twitter_button_img)
        self.components["twitter_button"] = twitter_button2

        # Facebook Button
        facebook_button_x = 0.53
        facebook_button_y = 0.4
        facebook_button_width = 1 / 6
        facebook_button_height = 0.2
        facebook_button_img = pygame.image.load('assets/Buttons/btn_fb.png')
        facebook_button = ImageButton("facebook_button", screen, facebook_button_x, facebook_button_y,
                                      facebook_button_width, facebook_button_height, facebook_button_img)
        self.components["facebook_button"] = facebook_button

        # return button
        return_button_x = 1/15
        return_button_y = 16 / 20
        return_button_width = 1 / 7
        return_button_height = 1 / 7
        return_button__img = pygame.image.load('assets/Buttons/btn_back.png')
        return_button2 = ImageButton("return_button", screen, return_button_x, return_button_y,
                                     return_button_width, return_button_height, return_button__img)
        self.components["return_button"] = return_button2

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        title = "leaderboard_web.html"
        f = open(title, 'w')
        html_template = """
                <!DOCTYPE html>
                <html>
                <head>
                <title>SmartRun Leaderboard</title>
                </head>
                <body>
                <style>
                img {
                width: 100%;
                }
                </style>
                <h1>SmartRun</h1>
                <img src="Leaderboard.jpg" alt="share on facebook" style="width:900px;height:600px;">
                </body>
                </html>

                """
        f.write(html_template)
        f.close()
        filename = 'file:///' + os.getcwd() + '/' + title

        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["username"] = self.input_data["username"]

            if triggered_component in [self.components["twitter_button"]]:
                webbrowser.open("https://twitter.com/intent/tweet?text=Check%20out%20the%20SmartRun%20monthly%20leaderboard%20here:%20https://www.facebook.com/SmartRun-Leaderboard-104831658686019/")
                if self.output_data["back_navigation"] == "topic_leaderboard":
                    self.output_data["subject"] = self.input_data["subject"]
                    self.output_data["topic"] = self.input_data["topic"]
                    share_string = self.output_data["subject"] + ": " + self.output_data["topic"]
                    self.name = "topic_leaderboard"
                elif self.output_data["back_navigation"] == "end_screen":
                    self.output_data["roomID"] = self.input_data["roomID"]
                    self.output_data["player_results"] = self.input_data["player_results"]
                    self.output_data["score"] = self.input_data["score"]
                    self.output_data["playertype"] = self.input_data["playertype"]
                    self.output_data["subject"] = self.input_data["subject"]
                    self.output_data["topic"] = self.input_data["topic"]
                    self.output_data["join_host"] = self.input_data["join_host"]

                    self.name = "end_screen"
            if triggered_component in [self.components["facebook_button"]]:

                webbrowser.open("https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/SmartRun-Leaderboard-104831658686019/")

                if self.output_data["back_navigation"] == "topic_leaderboard":
                    self.output_data["subject"] = self.input_data["subject"]
                    self.output_data["topic"] = self.input_data["topic"]
                    share_string = self.output_data["subject"] + ": " + self.output_data["topic"]
                    self.name = "topic_leaderboard"
                elif self.output_data["back_navigation"] == "end_screen":
                    self.output_data["roomID"] = self.input_data["roomID"]
                    self.output_data["player_results"] = self.input_data["player_results"]
                    self.output_data["score"] = self.input_data["score"]
                    self.output_data["playertype"] = self.input_data["playertype"]
                    self.output_data["subject"] = self.input_data["subject"]
                    self.output_data["topic"] = self.input_data["topic"]
                    self.output_data["join_host"] = self.input_data["join_host"]
                    self.name = "end_screen"

            if triggered_component in [self.components["return_button"]]:
                if self.output_data["back_navigation"] == "topic_leaderboard":
                    self.output_data["subject"] = self.input_data["subject"]
                    self.output_data["topic"] = self.input_data["topic"]
                    share_string = self.output_data["subject"] + ": " + self.output_data["topic"]
                    self.name = "topic_leaderboard"
                elif self.output_data["back_navigation"] == "end_screen":
                    self.output_data["roomID"] = self.input_data["roomID"]
                    self.output_data["player_results"] = self.input_data["player_results"]
                    self.output_data["score"] = self.input_data["score"]
                    self.output_data["playertype"] = self.input_data["playertype"]
                    self.output_data["subject"] = self.input_data["subject"]
                    self.output_data["topic"] = self.input_data["topic"]
                    self.output_data["join_host"] = self.input_data["join_host"]
                    self.name = "end_screen"
