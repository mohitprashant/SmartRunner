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
        self.current_page = "uniqueanalytics"
        self.login = LoginPage(self.screen)
        self.main_menu = MainMenuPage(self.screen)
        self.singleplayer = SinglePlayerPage(self.screen)
        self.leadselect = LeadSelectPage(self.screen)
        self.managerooms = ManageRoomsPage(self.screen)
        self.hostroom = HostRoomPage(self.screen)
        self.playerroom = PlayerRoomPage(self.screen)
        self.analyticsselect = AnalyticsSelectPage(self.screen)
        self.uniqueanalytics = UniqueAnalyticsPage(self.screen)

    def start(self):
        pygame.init()
        pygame.display.set_caption(self.caption)
        # holding key delay and repeat rate
        pygame.key.set_repeat(500, 30)

        while self.run:
            print(self.current_page)
            page_output = self.analyticsselect.start(self.screen)
            if page_output["exit"]:
                break
            if page_output["current_page"] == "analyticsselect":
                print("test")

            pygame.display.update()

        pygame.quit()


