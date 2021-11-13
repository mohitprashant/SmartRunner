import pygame.cursors

from assets.components import *
from page import *
import sys
sys.path.insert(1, '../../backend/database')
import QuestionManager
import RoomManager


class SinglePlayerPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "singleplayer"
        self.input_data = {
            "back_navigation": "",
            "subjectlist": [],
            "topiclist": [],
            "difficultylist": [],
            "subjectselection": "",
            "topicselection": "",
            "difficultyselection": "",
            "prev_page": ""

        }
        self.output_data = {
            "back_navigation": "",
            "current_page": self.name,
            "prev_page": "",
            "username": "",
            "password": "",
            "exit": False,
            "subjectselection": "",
            "topicselection": "",
            "difficultyselection": ""
        }


    # set all component variables on input screen
    def set_components(self, screen):
        self.name = "singleplayer"

        # change back navigation every time page type changes
        if self.input_data["prev_page"] != self.name:
            self.output_data["back_navigation"] = self.input_data["prev_page"]

        # background
        bg_img = pygame.image.load('assets/Backgrounds/singleplayerbg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # start button
        start_button_rel_x = 3 / 7
        start_button_rel_y = 4 / 5
        start_button_rel_width = 1 / 7
        start_button_rel_height = 1 / 7
        start_button_img = pygame.image.load('assets/Buttons/btn_start.png')
        start_button = ImageButton("start_button", screen, start_button_rel_x, start_button_rel_y, start_button_rel_width,
                              start_button_rel_height, start_button_img)
        self.components["start_button"] = start_button

        # back button
        exit_button_rel_x = 1 / 15
        exit_button_rel_y = 4 / 5
        exit_button_rel_width = 1 / 7
        exit_button_rel_height = 1 / 7
        exit_button_img = pygame.image.load('assets/Buttons/btn_back.png')
        exit_button = ImageButton("exit_button", screen, exit_button_rel_x, exit_button_rel_y,
                                   exit_button_rel_width,
                                   exit_button_rel_height, exit_button_img)
        self.components["exit_button"] = exit_button

        # difficulty list
        difficultylist_rel_x = 1 / 7
        difficultylist_rel_y = 5 / 10
        difficultylist_rel_width = 5 / 7
        difficultylist_rel_height = 1 / 10
        difficultylist_text_list = self.input_data["difficultylist"]
        prompt = self.input_data["difficultyselection"]
        num_expand_text = 3
        difficultylist = DynamicDropdownTextSelect("difficultylist", screen, difficultylist_rel_x, difficultylist_rel_y,
                                            difficultylist_rel_width,
                                            difficultylist_rel_height, difficultylist_text_list, prompt,
                                            num_expand_text, screen)
        self.components["difficultylist"] = difficultylist
        self.layers.append(difficultylist)

        # topic list
        topiclist_rel_x = 1 / 7
        topiclist_rel_y = 3 / 10
        topiclist_rel_width = 5 / 7
        topiclist_rel_height = 1 / 10
        topiclist_text_list = self.input_data["subject_topic_list"]
        prompt = self.input_data["topicselection"]
        num_expand_text = 3
        topiclist = DynamicDropdownTextSelect("topiclist", screen, topiclist_rel_x, topiclist_rel_y,
                                       topiclist_rel_width,
                                       topiclist_rel_height, topiclist_text_list, prompt, num_expand_text, screen)
        self.components["topiclist"] = topiclist
        self.layers.append(topiclist)

        # subject list
        subjectlist_rel_x = 1 / 7
        subjectlist_rel_y = 1 / 10
        subjectlist_rel_width = 5 / 7
        subjectlist_rel_height = 1 / 10
        subjectlist_text_list = self.input_data["subjectlist"]
        prompt = self.input_data["subjectselection"]
        num_expand_text = 3
        subjectlist = DynamicDropdownTextSelect("subjectlist", screen, subjectlist_rel_x, subjectlist_rel_y,
                                         subjectlist_rel_width,
                                         subjectlist_rel_height, subjectlist_text_list, prompt, num_expand_text, screen)
        self.components["subjectlist"] = subjectlist
        self.layers.append(subjectlist)

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["prev_page"] = self.output_data["current_page"]
            self.output_data["username"] = self.input_data["username"]
            self.output_data["subject_topic_list"] = self.input_data["subject_topic_list"]
            self.output_data["difficultylist"] = self.input_data["difficultylist"]
            self.output_data["subjectselection"] = self.input_data["subjectselection"]
            self.output_data["topicselection"] = self.input_data["topicselection"]
            self.output_data["difficultyselection"] = self.input_data["difficultyselection"]
            self.output_data["roomID"] = self.input_data["roomID"]
            self.output_data["join_host"] = self.input_data["join_host"]
            self.output_data["playertype"] = self.input_data["playertype"]
            self.output_data["readystatus"] = ""
            self.output_data["custom_quiz_selection"] = ""






            # put player once multiplayer is up
            if triggered_component in [self.components["start_button"]]:
                questiondb = QuestionManager.get_questions_by_difficulty(self.output_data["subjectselection"],self.output_data["topicselection"],int(self.output_data["difficultyselection"]))
                print(questiondb)
                questionlist = []
                answerlist = []
                for question in questiondb:
                    answers = []
                    questionlist.append(question["Description"])
                    answers.append(str(question["Correct"]))
                    answers.append(str(question["Wrong_1"]))
                    answers.append(str(question["Wrong_2"]))
                    answers.append(str(question["Wrong_3"]))
                    answerlist.append(answers)
                print(questionlist)
                print(answerlist)
                self.output_data["questions"] = questionlist
                self.output_data["answers"] = answerlist
                if self.output_data["roomID"] != "singleplayer":
                    self.output_data["questions"].insert(0,self.input_data["topicselection"])
                    self.output_data["questions"].insert(0,self.input_data["subjectselection"])
                    print("roomID: ", self.output_data["roomID"])
                    print("questions: ", self.output_data["questions"])
                    print("answers: ", self.output_data["answers"])
                    QuestionManager.set_questions_by_host(self.output_data["roomID"], self.output_data["questions"])
                    QuestionManager.set_answers_by_host(self.output_data["roomID"], self.output_data["answers"])
                    RoomManager.set_room_activity_status(self.output_data["roomID"], True)
                self.name = "game_play"

            if triggered_component in [self.components["exit_button"]]:
                self.name = "main_menu"

            if triggered_component in [self.components["subjectlist"]]:
                self.input_data["subjectselection"] = self.components["subjectlist"].button.text
                self.output_data["subjectselection"] = self.input_data["subjectselection"]
                self.output_data["subject_topic_list"] = QuestionManager.get_topics(self.output_data["subjectselection"])

                self.name = "singleplayer"
            if triggered_component in [self.components["topiclist"]]:
                self.input_data["topicselection"] = self.components["topiclist"].button.text
                self.output_data["topicselection"] = self.input_data["topicselection"]
                difficultylist = QuestionManager.get_question_difficulty_list(self.output_data["subjectselection"], self.output_data["topicselection"])
                self.output_data["difficultylist"] = list(map(str, difficultylist))
                print(self.components["topiclist"].button.text)
                self.name = "singleplayer"
            if triggered_component in [self.components["difficultylist"]]:
                self.input_data["difficultyselection"] = self.components["difficultylist"].button.text
                print(self.components["difficultylist"].button.text)
                self.output_data["difficultyselection"] = self.input_data["difficultyselection"]
                self.name = "singleplayer"




