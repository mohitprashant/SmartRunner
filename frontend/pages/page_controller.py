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
from welcome_screen import *
from game_play import *
from customize import *
import sys
sys.path.insert(1, '../../backend/database')
import LeaderboardManager
import QuestionManager
import ResultManager
import RoomManager

'''
main controller of the system
int screen_width starting width of screen
int screen_height starting height of screen
'''
#placeholder data to pull data from database
leadselect = ["Leaderboard 1", "Leaderboard 2", "Leaderboard 3", "Leaderboard 4", "Leaderboard 5", "Leaderboard 6", "Leaderboard 7", "Leaderboard 8"]
roomlist = ["576463", "Room 2", "Room 3", "Room 4", "Room 5", "Room 6", "Room 7", "Room 8"]
player_status = ["Player 1               Active", "Player 2               Active", "Player 3               Active", "Player 4               Active", "Player 5               Active", "Player 6               Active", "Player 7               Active", "Player 8               Active"]
# analyticslist = ["Analytics 1", "Analytics 2", "Analytics 3", "Analytics 4", "Analytics 5", "Analytics 6", "Analytics 7", "Analytics 8"]
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
        self.welcome_screen = WelcomeScreenPage(self.screen)
        self.game_play = Game(self.screen)
        self.customize = CustomizePage(self.screen)



    def start(self):
        pygame.init()
        pygame.display.set_caption(self.caption)
        # holding key delay and repeat rate
        pygame.key.set_repeat(500, 30)
        input_data = {
        }
        page_data = self.welcome_screen.start(self.screen, input_data)
        while self.run:
            self.current_page = page_data[0]["current_page"]
            print("current page", page_data[0]["current_page"])
            # print("prev page", page_data[0]["prev_page"])
            # print("back", page_data[0]["back_navigation"])
            print("pls merge")

            if page_data[0]["exit"]:
                break
            elif page_data[0]["current_page"] == "singleplayer":
                # add from hostroom/playerroom
                subjectlist = QuestionManager.get_subjects()
                print("confusion", page_data[0]["subject_topic_list"])
                input_data = {
                    "back_navigation": "",
                    "username": page_data[0]["username"],
                    "subjectlist": subjectlist,
                    "difficultylist": page_data[0]["difficultylist"],
                    "subject_topic_list": page_data[0]["subject_topic_list"],
                    "subjectselection": page_data[0]["subjectselection"],
                    "topicselection": page_data[0]["topicselection"],
                    "difficultyselection": page_data[0]["difficultyselection"],
                    # put player once multiplayer is up
                    "join_host": page_data[0]["join_host"],
                    "prev_page": page_data[0]["prev_page"],
                    "roomID": page_data[0]["roomID"],
                    "playertype": page_data[0]["playertype"]

                }
                if page_data[0]["back_navigation"] != ("main_menu" or "hostroom"):
                    pass
                elif page_data[0]["prev_page"] == "main_menu":
                    #input_data["playerlist"] = currentplayer
                    pass
                elif page_data[0]["prev_page"] == "hostroom":
                    #input_data["playerlist"] = currentplayer
                    pass
                page_data = self.singleplayer.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "host_settings":
                input_data = {
                    "roomID": page_data[0]["roomID"],
                    "username": page_data[0]["username"],
                    "custom_quiz_selection": page_data[0]["custom_quiz_selection"],
                    "toggled": page_data[0]["toggled"],
                    "mode_toggle": page_data[0]["mode_toggle"],
                    "prev_page": page_data[0]["prev_page"],
                    "join_host": page_data[0]["join_host"]

                }
                if page_data[0]["back_navigation"] != ("hostroom" or "custom_select"):
                    pass
                elif page_data[0]["prev_page"] == "host_settings":
                    input_data["custom_quiz_selection"] = page_data[0]["custom_quiz_selection"]
                elif page_data[0]["prev_page"] == "hostroom":
                    pass

                elif page_data[0]["prev_page"] == "custom_select":
                    pass

                page_data = self.host_settings.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "custom_select":
                input_data = {
                    "roomID": page_data[0]["roomID"],
                    "username": page_data[0]["username"],
                    "custom_quiz_selection": page_data[0]["custom_quiz_selection"],
                    "custom_quizzes": RoomManager.get_room_quizzes_list(page_data[0]["roomID"]),
                    "toggled": page_data[0]["toggled"],
                    "prev_page": page_data[0]["prev_page"]

                }
                page_data = self.custom_select.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "question_select":
                if page_data[0]["custom_quiz_selection"] !="":
                    # page_data[0]["custom_quiz_selection"] = "Custom Quiz 1"
                    custom_quiz_selection = page_data[0]["custom_quiz_selection"]
                    custom_quiz = QuestionManager.get_custom_questions(page_data[0]["roomID"],page_data[0]["custom_quiz_selection"])
                    description = []
                    id = []
                    for question in custom_quiz:
                        description.append(question["Description"])
                        id.append(question["question_id"])
                    desc_id = dict(zip(description, id))
                else:
                    custom_quiz_selection = ""
                    custom_quiz = []
                    description = []
                    page_data[0]["selected_question"] = ""
                    desc_id = {}

                input_data = {
                    "roomID": page_data[0]["roomID"],
                    "username": page_data[0]["username"],
                    "toggled": page_data[0]["toggled"],
                    "custom_quiz_selection": custom_quiz_selection,
                    "custom_question_selection": custom_quiz,
                    "question_list": description,
                    "retrieve_id": desc_id,
                    "selected_question": page_data[0]["selected_question"],
                    "prev_page": page_data[0]["prev_page"]

                }
                page_data = self.question_select.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "add_question":
                input_data = {
                    "roomID": page_data[0]["roomID"],
                    "username": page_data[0]["username"],
                    "toggled": page_data[0]["toggled"],
                    "correct_option": page_data[0]["correct_option"],
                    "custom_quiz_selection": page_data[0]["custom_quiz_selection"],
                    "custom_question_selection": page_data[0]["custom_question_selection"],
                    "selected_question": page_data[0]["selected_question"],
                    "prev_page": page_data[0]["prev_page"]
                }
                page_data = self.add_question.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "share":

                # if page_data[0]["back_navigation"] == "share" and page_data[0]["prev_page"] == "share":
                input_data = {
                        "roomID": page_data[0]["roomID"],
                        "username": page_data[0]["username"],
                        "back_navigation": page_data[0]["prev_page"],
                        "prev_page": page_data[0]["prev_page"],
                        "mode_toggle": page_data[0]["mode_toggle"],
                        "toggled": page_data[0]["toggled"],
                        "custom_quiz_selection": page_data[0]["custom_quiz_selection"],
                        "join_host": page_data[0]["join_host"]

                }
                # elif page_data[0]["prev_page"] == "share":
                #     input_data = {
                #         "roomID": page_data[0]["roomID"],
                #         "username": page_data[0]["username"],
                #         "back_navigation": page_data[0]["prev_page"],
                #         "prev_page": page_data[0]["prev_page"]
                #     }
                # else:
                #     input_data = {
                #     "roomID": page_data[0]["roomID"],
                #     "username": page_data[0]["username"],
                #     "back_navigation": page_data[0]["prev_page"],
                #     "prev_page": page_data[0]["prev_page"]
                # }
                page_data = self.share.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "share_results":
                if page_data[0]["back_navigation"] == "topic_leaderboard" or page_data[0]["prev_page"] == "topic_leaderboard":
                    input_data = {
                        "username": page_data[0]["username"],
                        "back_navigation": page_data[0]["prev_page"],
                        "subject": page_data[0]["subject"],
                        "topic": page_data[0]["topic"],
                        "prev_page": page_data[0]["prev_page"]

                    }
                elif page_data[0]["back_navigation"] == "end_screen" or page_data[0]["prev_page"] == "end_screen":
                    input_data = {
                        "player_results": page_data[0]["player_results"],
                        "score": page_data[0]["score"],
                        "roomID": page_data[0]["roomID"],
                        "username": page_data[0]["username"],
                        "back_navigation": page_data[0]["prev_page"],
                        "prev_page": page_data[0]["prev_page"],
                        "playertype": page_data[0]["playertype"],
                        "subject": page_data[0]["subject"],
                        "topic": page_data[0]["topic"],
                        "join_host": page_data[0]["join_host"]

                    }
                page_data = self.share_results.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "main_menu":
                input_data = {
                    "username": page_data[0]["username"],
                    "prev_page": page_data[0]["prev_page"]
                }
                page_data = self.main_menu.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "topic_leaderboard":
                if page_data[0]["back_navigation"] != ("leadselect" or "share_results"):
                    pass
                elif page_data[0]["prev_page"] == "topic_leaderboard":
                    page_data[0]["subject"] = page_data[1]["subject"]
                    page_data[0]["topic"] = page_data[1]["topic"]
                raw_list = LeaderboardManager.get_leaderboard(page_data[0]["subject"],page_data[0]["topic"])
                topic_leaderboard = []
                print("lm", raw_list)
                for entry in raw_list:
                    user_score = str(entry["username"].split("@",1)[0]) + " " + str(entry["score"])
                    topic_leaderboard.append(user_score)
                topic_leaderboard = topic_leaderboard[::-1]
                input_data = {
                    "topic_leaderboard": topic_leaderboard,
                    "subject": page_data[0]["subject"],
                    "topic": page_data[0]["topic"],
                    "username": page_data[0]["username"],
                    "prev_page": page_data[0]["prev_page"]
                }
                page_data = self.topic_leaderboard.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "end_screen":
                input_data = {
                        "player_results": page_data[0]["player_results"],
                        "username": page_data[0]["username"],
                        "roomID": page_data[0]["roomID"],
                        "prev_page": page_data[0]["prev_page"],
                        "score": page_data[0]["score"],
                        "playertype": page_data[0]["playertype"],
                        "subject": page_data[0]["subject"],
                        "topic": page_data[0]["topic"],
                        "join_host": page_data[0]["join_host"]

                }
                page_data = self.end_screen.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "login":
                input_data ={
                }
                page_data = self.login.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "create_account":
                input_data = {
                }
                page_data = self.create_account.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "room_tab":
                input_data = {
                    "username": page_data[0]["username"],
                    "prev_page": page_data[0]["prev_page"]

                }
                page_data = self.room_tab.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "room_creation":
                input_data = {
                    "username": page_data[0]["username"],
                    "prev_page": page_data[0]["prev_page"]

                }
                page_data = self.room_creation.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "join_room":
                input_data = {
                    "username": page_data[0]["username"],
                    "prev_page": page_data[0]["prev_page"]
                    # "roomID": roomID,
                    # "room_password": room_password
                }
                page_data = self.join_room.start(self.screen, input_data)

            elif page_data[0]["current_page"] == "leadselect":
                leadlist = LeaderboardManager.get_leaderboard_subjects()
                print("leadlist", leadlist)
                lead_subjectlist = []
                for subject in leadlist:
                    topic_list = LeaderboardManager.get_leaderboard_topics(subject)
                    for topic in topic_list:
                        subjecttopic = subject + ": " + topic
                        lead_subjectlist.append(subjecttopic)
                input_data = {
                    #input data goes to the leaderboardselection page
                    "username": page_data[0]["username"],
                    "leaderboardlist": lead_subjectlist,
                    "prev_page": page_data[0]["prev_page"]
                }
                page_data = self.leadselect.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "managerooms":
                roomname_list=[]
                roomid_list =RoomManager.get_list_of_rooms_by_host(page_data[0]["username"])
                for room in roomid_list:
                    roomname_list.append(RoomManager.get_room_name_from_id(room))
                roomid_dict=dict(zip(roomname_list,roomid_list))
                input_data = {
                    "username": page_data[0]["username"],
                    "roomname_list": roomname_list,
                    "roomid_dict":roomid_dict,
                    "prev_page": page_data[0]["prev_page"]
                }
                print("username:", page_data[0]["username"])
                page_data = self.managerooms.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "hostroom":

                input_data = {
                    "player_status": page_data[0]["player_status"],
                    "username": page_data[0]["username"],
                    "roomID": page_data[0]["roomID"],
                    "prev_page": page_data[0]["prev_page"],
                    "mode_toggle": page_data[0]["mode_toggle"],
                    "toggled": page_data[0]["toggled"],
                    "join_host": page_data[0]["join_host"],
                    "custom_quiz_selection": page_data[0]["custom_quiz_selection"]
                }
                if page_data[0]["back_navigation"]!=("managerooms" or "host_settings" or "share"):
                    pass
                elif page_data[0]["prev_page"] == "host_settings":
                    # mode_toggle = page_data[0]["mode_toggle"]
                    # toggled = page_data[0]["toggled"]
                    # customchoice = page_data[0]["custom_quiz_selection"]
                    pass
                    # input_data["mode_toggle"] = page_data[0]["mode_toggle"]
                    # input_data["toggled"] = page_data[0]["toggled"]
                    # input_data["custom_quiz_selection"] = page_data[0]["custom_quiz_selection"]

                elif page_data[0]["prev_page"] == "share":
                    pass
                elif page_data[0]["prev_page"] == "hostroom":
                    pass
                    # page_data[0]["roomID"] = page_data[1]["roomID"]
                print("mode_toggle", input_data["mode_toggle"])
                print("toggled", input_data["toggled"])
                print("custom_quiz_selection", input_data["custom_quiz_selection"])
                page_data = self.hostroom.start(self.screen, input_data)

            elif page_data[0]["current_page"] == "playerroom":
                if page_data[0]["back_navigation"]!="join_room":
                    pass
                elif page_data[0]["prev_page"] == "playerroom":
                    pass
                    # page_data[0]["roomID"] = page_data[1]["roomID"]
                # player_status_dict = RoomManager.get_room_member_statuses(page_data[0]["roomID"])
                # print("backend:", player_status_dict)
                # player_status = list(player_status_dict.items())
                # print("dict items:", player_status)
                # player_status_list = [ "%s %s" % x for x in player_status]
                print("roomID", page_data[0]["roomID"])
                input_data = {
                    "player_status": page_data[0]["player_status"],
                    "username": page_data[0]["username"],
                    "roomID": page_data[0]["roomID"],
                    "prev_page": page_data[0]["prev_page"]
                }
                page_data = self.playerroom.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "analyticsselect":
                if page_data[0]["prev_page"] == "analyticslist":
                    page_data[0]["roomID"] = page_data[1]["roomID"]
                # page_data[0]["roomID"] = "576463"

                analyticslist = RoomManager.get_room_quizzes_list(page_data[0]["roomID"])

                input_data = {
                    "analyticslist": analyticslist,
                    "roomID": page_data[0]["roomID"],
                    "username": page_data[0]["username"],
                    "prev_page": page_data[0]["prev_page"],
                    "mode_toggle": page_data[0]["mode_toggle"],
                    "toggled": page_data[0]["toggled"],
                    "custom_quiz_selection": page_data[0]["custom_quiz_selection"],
                    "join_host": page_data[0]["join_host"]

                }

                page_data = self.analyticsselect.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "uniqueanalytics":
                quiz_info = RoomManager.get_room_quiz_info(page_data[0]["roomID"], page_data[0]["analyticsID"])

                players_results = ResultManager.get_game_results_list(page_data[0]["roomID"],
                                                                      page_data[0]["analyticsID"])

                questions_results = ResultManager.get_game_question_results_list(page_data[0]["roomID"],
                                                                                 page_data[0]["analyticsID"])

                analyticsdata = [quiz_info, players_results, questions_results]
                input_data = {
                    "analytics": analyticsdata,
                    "username": page_data[0]["username"],
                    "roomID": page_data[0]["roomID"],
                    "analyticsID": page_data[0]["analyticsID"],
                    "prev_page": page_data[0]["prev_page"],
                    "mode_toggle": page_data[0]["mode_toggle"],
                    "toggled": page_data[0]["toggled"],
                    "custom_quiz_selection": page_data[0]["custom_quiz_selection"],
                    "join_host": page_data[0]["join_host"]

                }
                page_data = self.uniqueanalytics.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "welcome_screen":
                input_data = {
                }
                page_data = self.welcome_screen.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "game_play":
                input_data = {
                    "username": page_data[0]["username"],
                    "questions": page_data[0]["questions"],
                    "answers": page_data[0]["answers"],
                    "roomID": page_data[0]["roomID"],
                    "playertype": page_data[0]["playertype"],
                    "readystatus": page_data[0]["readystatus"],
                    "join_host": page_data[0]["join_host"],
                    "subjectselection": page_data[0]["subjectselection"],
                    "topicselection": page_data[0]["topicselection"],
                    "custom_quiz_selection": page_data[0]["custom_quiz_selection"]

                }
                page_data = self.game_play.start(self.screen, input_data)
            elif page_data[0]["current_page"] == "customize":
                input_data = {
                    "username": page_data[0]["username"],
                    "prev_page": page_data[0]["prev_page"],
                }
                page_data = self.customize.start(self.screen, input_data)

            pygame.display.update()

        pygame.quit()


