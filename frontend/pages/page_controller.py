import pygame
from login import *
from main_menu import *
from end_screen import *
from topic_leaderboard import *
from room_tab import *
from room_creation import *
from join_room import *
from host_settings import *
from share import *
'''
main controller of the system
int screen_width starting width of screen
int screen_height starting height of screen
'''


class PageController:
    def __init__(self, screen_width=720, screen_height=480):
        self.run = True
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        self.caption = "Smart Runners"
        # define pages
<<<<<<<<< Temporary merge branch 1
        self.current_page = "join_room"
        self.login_page = LoginPage(self.screen)
=========
        self.current_page = "login"
        self.login = LoginPage(self.screen)
>>>>>>>>> Temporary merge branch 2
        self.main_menu = MainMenuPage(self.screen)
        self.end_screen = EndScreenPage(self.screen)
        self.topic_leaderboard = TopicLeaderboardPage(self.screen)
        self.room_tab = RoomTabPage(self.screen)
        self.room_creation = RoomCreationPage(self.screen)
        self.join_room = JoinRoomPage(self.screen)
        self.host_settings = HoseSettingsPage(self.screen)
        self.share = SharePage(self.screen)



    def start(self):
        pygame.init()
        pygame.display.set_caption(self.caption)
        # holding key delay and repeat rate
        pygame.key.set_repeat(500, 30)

        while self.run:
            print(self.current_page)
<<<<<<<<< Temporary merge branch 1
            page_output = self.share.start(self.screen)
=========
            page_output = self.login.start(self.screen)
>>>>>>>>> Temporary merge branch 2
            if page_output["exit"]:
                break
            if page_output["share"] == "share":
                self.current_page = "share"

            pygame.display.update()

        pygame.quit()


