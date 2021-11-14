import pygame
from assets.components import *
from page import *
sys.path.insert(1, '../../backend/database')

import LeaderboardManager
import ResultManager



class EndScreenPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "end_screen"
        self.input_data = {
            "player_results": {},
            "roomID": "",
            "username":"",
            "prev_page":"",
            "score":"",
            "playertype": "",
            "subject": "",
            "topic": ""
        }
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "room_ID": "",
            "score_board": [],
            "username":"",
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        self.name = "end_screen"

        # change back navigation every time page type changes
        if self.input_data["prev_page"] != self.name:
            self.output_data["back_navigation"] = self.input_data["prev_page"]

        # background
        bg_img = pygame.image.load('assets/Backgrounds/endgamebg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

#relative_x, relative_y, relative_width, relative_height,relative_shown_width, relative_shown_height,
        # player list
        # relative_x = 0.05
        # relative_y = 0.15
        # relative_width = 0.8
        # text_relative_height = 8 / 10
        # shown_relative_width = 6 / 10
        # shown_relative_height = 3 / 5
        # player_results = MouseScrollableSurface("player_results", screen, relative_x,
        #                                           relative_y, relative_width,
        #                                           text_relative_height, shown_relative_width, shown_relative_height,
        #                                           screen)
        # #create surface
        # self.components["player_results"] = player_results
        # self.layers.append(player_results)



        list_image_rel_x = 0.095
        list_image_rel_y = 0.1
        list_image_rel_width = 0.8
        list_image_rel_height = 0.7
        list_img = pygame.image.load('assets/Backgrounds/scrollable.png')
        scroll_image = ImageDisplay("scroll_image", screen, list_image_rel_x, list_image_rel_y,
                                           list_image_rel_width,
                                           list_image_rel_height, list_img)
        self.components["analyticslist_image"] = scroll_image

        # results header
        results_image_rel_x = 0.3
        results_image_rel_y = 0.04
        results_image_rel_width = 0.3
        results_image_rel_height = 0.15
        results_img = pygame.image.load('assets/Backgrounds/results.png')
        resultsheader_image = ImageDisplay("resultsheader_image", screen, results_image_rel_x, results_image_rel_y,
                                           results_image_rel_width,
                                           results_image_rel_height, results_img)
        self.components["resultsheader_image"] = resultsheader_image

        #SelectableTextList
        relative_x = 0.2
        relative_y = 0.2
        relative_width = 0.55
        text_relative_height = 0.1
        shown_relative_width = 0.55
        shown_relative_height = 0.5
        score_text_list = ["Player: " + self.input_data["player_results"]["player_name"], "Total Questions: "+ str(self.input_data["player_results"]["attempted"]), "Total Correct: " + str(self.input_data["player_results"]["correct"]), "Time Taken: " + str(self.input_data["player_results"]["time"])+ "s", "Score: " + str(self.input_data["score"])]
        # print(self.input_data.keys())
        # print(score_text_list)

        score_board_text_list = SelectableTextList("score_board_text_list", screen, relative_x,
                                                  relative_y, relative_width,
                                                  text_relative_height, shown_relative_width, shown_relative_height,
                                                  score_text_list, screen, single_select=True, active_color="white")

        self.components["score_board_text_list"] = score_board_text_list
       # player_results.add_component(score_board_text_list)
        self.layers.append(score_board_text_list)


        # Player Score display
        # player_results_display_x = 1 / 4
        # player_results_display_y = 1 / 4
        # player_results_display_width = 1 / 2
        # player_results_display_height = 1 / 4
        # player_results_text ="Player 1: Score"
        # player_results_display = TextDisplay("player_results_display", screen, player_results_display_x, player_results_display_y, player_results_display_width,
        #                       player_results_display_height,player_results_text)
        # self.components["player_results_display"] = player_results_display


        # Share button
        share_button_x = 8 / 10
        share_button_y = 8 / 10
        share_button_width = 1 / 7
        share_button_height = 1 / 7
        share_button_img = pygame.image.load('assets/Buttons/btn_share.png')
        share_button = ImageButton("share_button", screen, share_button_x, share_button_y,
                             share_button_width,
                             share_button_height, share_button_img)
        self.components["share_button"] = share_button

        # Back button
        back_button_x = 4 / 10
        back_button_y = 4 / 5
        back_button_width = 1 / 5
        back_button_height = 1 / 7
        back_button_img = pygame.image.load('assets/Buttons/btn_confirm.png')
        back_button = ImageButton("back_button", screen, back_button_x, back_button_y,
                                   back_button_width,
                                   back_button_height, back_button_img)
        self.components["back_button"] = back_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["roomID"] = self.input_data["roomID"]
            self.output_data["player_results"] = self.input_data["player_results"]
            self.output_data["username"] = self.input_data["username"]
            self.output_data["prev_page"] = self.name
            self.output_data["score"] = self.input_data["score"]
            self.output_data["player_status"] = []
            self.output_data["mode_toggle"] = False
            self.output_data["toggled"] = False
            self.output_data["custom_quiz_selection"] = ""
            self.output_data["playertype"] = self.input_data["playertype"]
            self.output_data["subject"] = self.input_data["subject"]
            self.output_data["topic"] = self.input_data["topic"]
            self.output_data["join_host"] = self.input_data["join_host"]






            if triggered_component in [self.components["share_button"]]:
                rect = pygame.Rect(0, 0, self.screen_width, (self.screen_height * 0.8))
                sub = self.screen.subsurface(rect)
                pygame.image.save(sub, "Leaderboard.jpg")
                print('\nsaved leaderboard.jpg\n')
                self.name = "share_results"

            if triggered_component in [self.components["back_button"]]:
                if self.input_data["roomID"] == "singleplayer":
                    print("Username: ", self.input_data["username"])
                    print("Subject: ", self.input_data["subject"])
                    print("Topic: ", self.input_data["topic"])

                    LeaderboardManager.update_leaderboard(self.input_data["username"], self.input_data["subject"], self.input_data["topic"])
                    self.name = "main_menu"

                elif self.input_data["playertype"] == "host":
                    if self.input_data["player_results"]["quiz_name"]!="" and self.input_data["join_host"]:
                        ResultManager.save_game_results(self.input_data["player_results"]["roomID"], self.input_data["player_results"]["quiz_name"], self.input_data["player_results"]["player_name"], self.input_data["player_results"]["attempted"], self.input_data["player_results"]["correct"])
                    self.name = "hostroom"
                elif self.input_data["playertype"] == "client":
                    if self.input_data["player_results"]["quiz_name"]!="" and self.input_data["readystatus"]:
                        ResultManager.save_game_results(self.input_data["player_results"]["roomID"], self.input_data["player_results"]["quiz_name"], self.input_data["player_results"]["player_name"], self.input_data["player_results"]["attempted"], self.input_data["player_results"]["correct"])
                    self.name = "playerroom"
                #add another one for multiplayer (how to account for host?)
            # if triggered_component in [self.components["player_results"]]:
            #     print("store  in self.output_data[roomID] for sharing")
            else:
                print("entry failed")
