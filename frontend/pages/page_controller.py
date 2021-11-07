import pygame
from login import *
from main_menu import *
from singleplayer import *
from leaderboardselection import *
from managerooms import *
from hostroom import *
from playerroom import *
from analyticsselection import *
from uniqueanalytics import *
from room_tab import *
from room_creation import *
from join_room import *
from host_settings import *
from share import *
from end_screen import *
from topic_leaderboard import *
from share_results import *
from custom_select import *
from create_account import *
from question_select import *
from add_question import *
import sys
sys.path.insert(1, '../../backend/database')
from FirebaseManager import *
'''
main controller of the system
int screen_width starting width of screen
int screen_height starting height of screen
'''
#placeholder data to pull data from database
leadselect = ["Leaderboard 1", "Leaderboard 2", "Leaderboard 3", "Leaderboard 4", "Leaderboard 5", "Leaderboard 6", "Leaderboard 7", "Leaderboard 8"]
roomlist = ["Room 1", "Room 2", "Room 3", "Room 4", "Room 5", "Room 6", "Room 7", "Room 8"]
player_status = ["Player 1               Active", "Player 2               Active", "Player 3               Active", "Player 4               Active", "Player 5               Active", "Player 6               Active", "Player 7               Active", "Player 8               Active"]
analyticslist = ["Analytics 1", "Analytics 2", "Analytics 3", "Analytics 4", "Analytics 5", "Analytics 6", "Analytics 7", "Analytics 8"]
analyticsdata = ["Mean= 23", "Median = 20", "Mode = 19", "Highest = 40", "Lowest = 12", "Standard Deviation = 3"]
username = ["User1", "User2", "User3", "User 4"]
password = ["hello", "pen", "bottle", "candle"]
score_board = ["User1 23", "User2 20", "User3 19", "User 4 25", "User 5 40", "User 6 34", "User 7 54"]
topicleadselect = {"Leaderboard 1": ["wee",'woo'], "Leaderboard 2": ["hee", "hoo"]}
roomID = ["R1", "R2", "R3", "R4"]
room_password = ["R1_P", "R2_P", "R3_P", "R4_P"]
custom_quiz = ["Custom Quiz 1", "Custom Quiz 2", "Custom Quiz 3", "Custom Quiz 4", "Custom Quiz 5", "Custom Quiz 6", "Custom Quiz 7"]
Toggle = ["True", "False"]
subjectlist = ["English", "Math", "Science"]
topiclist = {"English": ["Noun", "Tense", "Verb", "Adjectives"], "Math": ["Subtraction", "Addition", "Multiplication", "Division"], "Science": ["Matter", "Magnets", "Organism Classification"]}
difficultylist = ["Easy", "Medium", "Hard"]
custom_questions_selection = ["1+1: 2  4   5", "4+4: 3  8  10", "3+2: 1  2   5", "3+3: 6  3   5", "7+2: 1  9   6", "8+2: 10  2   5", "6+2: 8  1   5"]

class PageController:
    def __init__(self, screen_width=720, screen_height=480):
        self.run = True
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        self.caption = "Smart Runners"
        # define pages
        self.current_page = ""
        self.login = LoginPage(self.screen)
        self.main_menu = MainMenuPage(self.screen)
        self.singleplayer = SinglePlayerPage(self.screen)
        self.leadselect = LeadSelectPage(self.screen)
        self.managerooms = ManageRoomsPage(self.screen)
        self.hostroom = HostRoomPage(self.screen)
        self.playerroom = PlayerRoomPage(self.screen)
        self.analyticsselect = AnalyticsSelectPage(self.screen)
        self.uniqueanalytics = UniqueAnalyticsPage(self.screen)
        self.room_tab = RoomTabPage(self.screen)
        self.host_settings = HostSettingsPage(self.screen)
        self.share = SharePage(self.screen)
        self.share_results = ShareResultsPage(self.screen)
        self.join_room = JoinRoomPage(self.screen)
        self.end_screen = EndScreenPage(self.screen)
        self.topic_leaderboard = TopicLeaderboardPage(self.screen)
        self.room_creation = RoomCreationPage(self.screen)
        self.custom_select = CustomSelectPage(self.screen)
        self.create_account = CreateAccountPage(self.screen)
        self.question_select = QuestionSelectPage(self.screen)
        self.add_question = AddQuestionPage(self.screen)



    def start(self):
        pygame.init()
        pygame.display.set_caption(self.caption)
        # holding key delay and repeat rate
        pygame.key.set_repeat(500, 30)
        input_data = {
            "username": username,
            "password": password
        }
        page_data = self.login.start(self.screen, input_data)
        while self.run:
            self.current_page = page_data[0]["current_page"]
            print("current page", self.current_page)
            if page_data[0]["exit"]:
                break
            if page_data[0]["current_page"] == "singleplayer":
                if page_data[0]["prev_page"]== "singleplayer":
                    # page_data[0]["subjectselection"]= page_data[1]["subjectselection"]
                    input_data = {
                        "subjectlist": subjectlist,
                        "topiclist": topiclist,
                        "difficultylist": difficultylist,
                        "subject_topic_list": ["Select Topic"],
                        "subjectselection": page_data[1]["subjectselection"]
                    }
                else:
                    input_data = {
                        "subjectlist": subjectlist,
                        "topiclist": topiclist,
                        "difficultylist": difficultylist,
                        "subject_topic_list": ["Select Topic"],
                        "subjectselection": "English"
                    }
                page_data = self.singleplayer.start(self.screen, input_data)
            if page_data[0]["current_page"] == "host_settings":
                if page_data[0]["prev_page"] == "custom_select":
                    input_data = {
                        "roomID": page_data[0]["roomID"],
                        "username": username,
                        "custom_quiz_selection": page_data[0]["custom_quiz_selection"],
                        "toggled": False
                        # "password": password
                    }
                else:
                    input_data = {
                        "roomID": page_data[0]["roomID"],
                        "username": username,
                        "toggled": False,
                        # "custom_quiz_selection": page_data[0]["custom_quiz_selection"]
                        # "password": password
                    }
                page_data = self.host_settings.start(self.screen, input_data)
            if page_data[0]["current_page"] == "custom_select":
                input_data = {
                    "roomID": roomID,
                    "username": username,
                    "custom_quiz": custom_quiz
                }
                page_data = self.custom_select.start(self.screen, input_data)
            if page_data[0]["current_page"] == "question_select":
                input_data = {
                    "roomID": roomID,
                    "username": username,
                    "custom_question_selection": custom_questions_selection
                        # "password": password
                }
                page_data = self.question_select.start(self.screen, input_data)
            if page_data[0]["current_page"] == "add_question":
                input_data = {
                    "roomID": roomID,
                    "username": username,
                    "custom_question_new": ""
                        # "password": password
                }
                page_data = self.add_question.start(self.screen, input_data)
            if page_data[0]["current_page"] == "share":
                if page_data[0]["prev_page"] == "playerroom":
                    input_data = {
                        "roomID": page_data[0]["roomID"],
                        "room_password": room_password,
                        "username": username,
                        "back_navigation":page_data[0]["prev_page"],
                        "toggled": False
                    }
                page_data = self.share.start(self.screen, input_data)
            if page_data[0]["current_page"] == "share_results":
                if page_data[0]["prev_page"] == "topic_leaderboard":
                    input_data = {
                        "username": username,
                        "back_navigation": page_data[0]["prev_page"],
                        "topic_leaderboard_ID": page_data[0]["topic_leaderboard_ID"],
                    }
                elif page_data[0]["prev_page"] == "end_screen":
                    input_data = {
                        "roomID": roomID,
                        "username": username,
                        "back_navigation": page_data[0]["prev_page"],
                        "score_board": page_data[0]["score_board"]
                    }
                page_data = self.share_results.start(self.screen, input_data)
            if page_data[0]["current_page"] == "main_menu":
                input_data = {
                    "username": username
                }
                page_data = self.main_menu.start(self.screen, input_data)
            if page_data[0]["current_page"] == "topic_leaderboard":
                if page_data[0]["prev_page"] == "topic_leaderboard":
                    page_data[0]["topic_leaderboard_ID"] = page_data[1]["topic_leaderboard_ID"]
                input_data = {
                    "topic_leaderboard": topicleadselect,
                    "topic_leaderboard_ID": page_data[0]["topic_leaderboard_ID"],
                    "username":username
                }
                page_data = self.topic_leaderboard.start(self.screen, input_data)
                print(page_data[0]["current_page"], "next")
            if page_data[0]["current_page"] == "end_screen":
                input_data = {
                    "score_board": score_board,
                    "roomID": page_data[1]["roomID"],
                    "username": username
                }
                page_data = self.end_screen.start(self.screen, input_data)
            if page_data[0]["current_page"] == "login":
                input_data ={
                    "username": username,
                    "password": password
                }
                page_data = self.login.start(self.screen, input_data)
            if page_data[0]["current_page"] == "create_account":
                input_data = {
                }
                page_data = self.create_account.start(self.screen, input_data)
            if page_data[0]["current_page"] == "room_tab":
                input_data = {
                    "username": username
                }
                page_data = self.room_tab.start(self.screen, input_data)
            if page_data[0]["current_page"] == "room_creation":
                input_data = {
                    "username": username,
                    # "roomID": roomID,
                    # "room_password": room_password
                }
                page_data = self.room_creation.start(self.screen, input_data)
            if page_data[0]["current_page"] == "join_room":
                input_data = {
                    "username": username,
                    # "roomID": roomID,
                    # "room_password": room_password
                }
                page_data = self.join_room.start(self.screen, input_data)

            if page_data[0]["current_page"] == "leadselect":
                input_data = {
                    #input data goes to the leaderboardselection page
                    "leaderboardlist": leadselect
                }
                page_data = self.leadselect.start(self.screen, input_data)
            if page_data[0]["current_page"] == "managerooms":
                input_data = {
                    "roomlist": roomlist
                }
                page_data = self.managerooms.start(self.screen, input_data)
            if page_data[0]["current_page"] == "hostroom":
                if page_data[0]["prev_page"] == "hostroom":
                    page_data[0]["roomID"] = page_data[1]["roomID"]
                input_data = {
                    "player_status": player_status,
                    "roomID": page_data[0]["roomID"]
                }
                page_data = self.hostroom.start(self.screen, input_data)
            if page_data[0]["current_page"] == "playerroom":
                if page_data[0]["current_page"] == "playerroom":
                    if page_data[0]["prev_page"] == "playerroom":
                        page_data[0]["roomID"] = page_data[1]["roomID"]
                    input_data = {
                        "player_status": player_status,
                        "roomID": page_data[0]["roomID"]
                    }
                    page_data = self.playerroom.start(self.screen, input_data)
            if page_data[0]["current_page"] == "analyticsselect":
                if page_data[0]["prev_page"] == "analyticslist":
                    page_data[0]["roomID"] = page_data[1]["roomID"]
                input_data = {
                    "analyticslist": analyticslist,
                    "roomID": page_data[0]["roomID"]
                }
                page_data = self.analyticsselect.start(self.screen, input_data)
            if page_data[0]["current_page"] == "uniqueanalytics":
                input_data = {
                    "analytics": analyticsdata,
                    "roomID": page_data[1]["roomID"]
                }
                page_data = self.uniqueanalytics.start(self.screen, input_data)



            pygame.display.update()

        pygame.quit()


