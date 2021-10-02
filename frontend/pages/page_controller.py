import pygame
from login import *
from main_menu import *
from end_screen import *
from topic_leaderboard import *
from room_tab import *
from room_creation import *
from join_room import *
from host_settings import *
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
        self.current_page = "join_room"
        self.login_page = LoginPage(self.screen)
        self.main_menu = MainMenuPage(self.screen)
        self.end_screen = EndScreenPage(self.screen)
        self.topic_leaderboard = TopicLeaderboardPage(self.screen)
        self.room_tab = RoomTabPage(self.screen)
        self.room_creation = RoomCreationPage(self.screen)
        self.join_room = JoinRoomPage(self.screen)
        self.host_settings = HoseSettingsPage(self.screen)


    def start(self):
        pygame.init()
        pygame.display.set_caption(self.caption)
        pygame.key.set_repeat(500, 30)

        while self.run:
            print(self.current_page)
            page_output = self.host_settings.start(self.screen)
            if page_output["exit"]:
                break
            if page_output["current_page"] == "host_settings":
                self.current_page = "host_settings"

            pygame.display.update()

        pygame.quit()


