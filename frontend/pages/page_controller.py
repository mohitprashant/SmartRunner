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
from host_settings import *
from share import *
from join_room import *
from end_screen import *
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
scoreboard = ["User1= 23", "User2 = 20", "User3 = 19"]


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
        self.join_room = JoinRoomPage(self.screen)
        self.end_screen = EndScreenPage(self.screen)


    def start(self):
        pygame.init()
        pygame.display.set_caption(self.caption)
        # holding key delay and repeat rate
        pygame.key.set_repeat(500, 30)
        input_data = {
            "analyticslist": analyticslist,
            "roomID": "RoomID"
        }
        page_data = self.end_screen.start(self.screen, input_data)
        while self.run:
            self.current_page = page_data[0]["current_page"]
            print(self.current_page)
            if page_data[0]["exit"]:
                break
            if page_data[0]["current_page"] == "singleplayer":
                page_data = self.singleplayer.start(self.screen, input_data)

            if page_data[0]["current_page"] == "room_tab":
                page_data = self.room_tab.start(self.screen, input_data)
            if page_data[0]["current_page"] == "host_settings":
                page_data = self.host_settings.start(self.screen, input_data)
            if page_data[0]["current_page"] == "share":
                page_data = self.share.start(self.screen, input_data)
            if page_data[0]["current_page"] == "join_room":
                page_data = self.join_room.start(self.screen, input_data)
            if page_data[0]["current_page"] == "main_menu":
                page_data = self.main_menu.start(self.screen, input_data)
            if page_data[0]["current_page"] == "end_screen":
                input_data = {
                    "score_board": scoreboard,
                    "roomID": page_data[1]["roomID"]
                }
                page_data = self.end_screen.start(self.screen, input_data)

            if page_data[0]["current_page"] == "login":
                input_data ={
                    "username": username,
                    "password": password
                }
                page_data = self.login.start(self.screen, input_data)
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
                input_data = {
                    "player_status": player_status,
                    "roomID": page_data[1]["roomID"]
                }
                page_data = self.hostroom.start(self.screen, input_data)
            if page_data[0]["current_page"] == "playerroom":
                input_data = {
                    "player_status": player_status,
                    "roomID": page_data[1]["roomID"]
                }
                page_data = self.playerroom.start(self.screen, input_data)
            if page_data[0]["current_page"] == "analyticsselect":
                input_data = {
                    "analyticslist": analyticslist,
                    "roomID": page_data[1]["roomID"]
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


