# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 16:10:35 2021

@author: 18moh
"""


from assets.components import *
from page import *
import pygame
import sys
import time

print([4]*5)

DECEL = 0.1
MINSPEED = 1.0
BLACK=(0,0,0)

class Player:
    def __init__(self, avatar):
        self.avatar = avatar
        self.speed = 3.0
        self.score = 0
        self.distance = 100.0
        self.lastupdate = time.time()
        self.state = 2
        self.question = 0



class Game(Page):
    
    def __init__(self, screen, questions, answers, timeperquestion = 10):
        super().__init__(screen)
        # pygame.init()
        self.questions = questions
        self.answers = answers
        self.timeavailable = timeperquestion * len(questions)
        self.starttime = time.time()
        self.lastupdate = time.time()
        self.game_stats = {}
        
        self.players = [Player('default')]       
        
        # self.font_obj=pygame.font.Font("C:\Windows\Fonts\Arial.ttf",25) 
        
        
        
    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/img/sky.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # picture display - sun to be replaced with a game image
        game_image_rel_x = 5 / 10
        game_image_rel_y = 2 / 10
        game_image_rel_width = 1 / 5
        game_image_rel_height = 1 / 5
        game_image_img = pygame.image.load('assets/img/sun.png')
        game_image_box = ImageDisplay("sun", screen, game_image_rel_x, game_image_rel_y,
                                       game_image_rel_width, game_image_rel_height,game_image_img)
        self.components["sun"] = game_image_box
        
        
        # floor
        game_image_rel_x = 0 / 10
        game_image_rel_y = 6 / 10
        game_image_rel_width = 1
        game_image_rel_height = 1 / 5
        floor = pygame.image.load('assets/img/grass.png')
        floor = ImageDisplay("floor", screen, game_image_rel_x, game_image_rel_y,
                                       game_image_rel_width, game_image_rel_height,floor)
        
        self.components["floor"] = floor
        
        
        # question box - invisible to begin with
        game_image_rel_x = 1 / 10
        game_image_rel_y = 1 / 10
        game_image_rel_width = 8 / 10
        game_image_rel_height = 1 / 7
        question = pygame.image.load('assets/img/questionbox.png')
        question = ImageDisplay("question", screen, game_image_rel_x, game_image_rel_y,
                                       game_image_rel_width, game_image_rel_height,question)
        
        self.components["question"] = question
        
        
        
        
        # ground
        game_image_rel_x = 0 / 10
        game_image_rel_y = 8 / 10
        game_image_rel_width = 1
        game_image_rel_height = 1 / 5
        dirt = pygame.image.load('assets/img/dirt.png')
        dirt = ImageDisplay("dirt", screen, game_image_rel_x, game_image_rel_y,
                                       game_image_rel_width, game_image_rel_height,dirt)
        self.components["dirt"] = dirt
        
        
        # answer boxes - invisible to begin with
        game_image_rel_x = 1 / 40
        game_image_rel_y = 7 / 10
        game_image_rel_width = 4 / 9
        game_image_rel_height = 2 / 16
        answer1 = pygame.image.load('assets/img/answer.png')
        answer1 = ImageDisplay("answer1", screen, game_image_rel_x, game_image_rel_y,
                                        game_image_rel_width, game_image_rel_height,answer1)
        
        self.components["answer1"] = answer1    
        
        
        game_image_rel_x = 21 / 40
        game_image_rel_y = 7 / 10
        answer2 = pygame.image.load('assets/img/answer.png')
        answer2 = ImageDisplay("answer2", screen, game_image_rel_x, game_image_rel_y,
                                        game_image_rel_width, game_image_rel_height,answer2)
        self.components["answer2"] = answer2 
        
        
        game_image_rel_x = 1 / 40
        game_image_rel_y = 8.5 / 10
        answer3 = pygame.image.load('assets/img/answer.png')
        answer3 = ImageDisplay("answer3", screen, game_image_rel_x, game_image_rel_y,
                                       game_image_rel_width, game_image_rel_height,answer3)
        self.components["answer3"] = answer3 
        
        
        game_image_rel_x = 21 / 40
        game_image_rel_y = 8.5 / 10
        answer4 = pygame.image.load('assets/img/answer.png')
        answer4 = ImageDisplay("answer4", screen, game_image_rel_x, game_image_rel_y,
                                       game_image_rel_width, game_image_rel_height,answer4)
        self.components["answer4"] = answer4 
        
        
        # progress bar
        game_image_rel_x = 1 / 100
        game_image_rel_y = 1 / 100
        game_image_rel_width = 1 / 2
        game_image_rel_height = 1 / 20
        progress = pygame.image.load('assets/img/progressbar.png')
        progress = ImageDisplay("progress", screen, game_image_rel_x, game_image_rel_y,
                                        game_image_rel_width, game_image_rel_height,progress)
        
        self.components["progress"] = progress
        
        
        # coverage -> max width at 38
        game_image_rel_x = 7 / 100
        game_image_rel_y = 3 / 100
        game_image_rel_width = 0 / 100
        game_image_rel_height = 1 / 50
        cover = pygame.image.load('assets/img/cover.png')
        cover = ImageDisplay("cover", screen, game_image_rel_x, game_image_rel_y,
                                        game_image_rel_width, game_image_rel_height,cover)
        
        self.components["cover"] = cover
        
        
        # player sprite
        game_image_rel_x = 4 / 10
        game_image_rel_y = 4.5 / 10
        game_image_rel_width = 1 / 6
        game_image_rel_height = 1 / 6
        player = pygame.image.load('assets/img/guy2.png')
        player = ImageDisplay("0", screen, game_image_rel_x, game_image_rel_y,
                              game_image_rel_width, game_image_rel_height,player)
        
        self.components[0] = player
        
        
        
    def playerupdate(self, screen):
        for x in self.players:
            if(time.time() - x.lastupdate > 1/x.speed):
                x.state = (x.state + 1) %4
                
                game_image_rel_x = 4 / 10
                game_image_rel_y = 4.5 / 10
                game_image_rel_width = 1 / 6
                game_image_rel_height = 1 / 6
                player = pygame.image.load('assets/img/guy'+str(x.state)+'.png')
                player = ImageDisplay("0", screen, game_image_rel_x, game_image_rel_y,
                                      game_image_rel_width, game_image_rel_height,player)
                self.components[0] = player
                x.lastupdate = time.time()
                
        
    def get_gamedata(self):
        data = {}
        
        for player in players.names:
            data[player] = players[player].data
        
        
        
    def add_player(self, playerName):
        self.multiplayer += 1



    def page_function(self, triggered_component_list):
        for x in triggered_component_list:
            pass

    # start running the page
    def start(self, screen, input_data):
        
        
        self.input_data = input_data
        self.output_data["current_page"] = self.name
        self.set_components(screen)
        
        
        while self.run:
            self.draw_components()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.output_data["exit"] = True
                    pygame.quit()
                    return self.output_data, self.input_data
                
                if event.type == pygame.VIDEORESIZE:
                    self.resize_components()
                    
                triggered_component_list = []
                # top_layer_triggered = False
                
                if(event.type == pygame.MOUSEBUTTONUP):
                    pos = pygame.mouse.get_pos()
              
                    # get a list of all sprites that are under the mouse cursor
                    for s in self.components.keys():
                        if(self.components[s].rect.collidepoint(pos)):
                            triggered_component_list.append(self.components[s])
                        
                            if(s == 'answer1'):
                                if(self.answers[self.players[0].question][0]):
                                    self.players[0].question += 1
                                    self.players[0].speed += 1.0
                            
                            elif(s == 'answer2'):
                                if(self.answers[self.players[0].question][1]):
                                    self.players[0].question += 1
                                    self.players[0].speed = max(1.0, self.players[0].speed - 1.0)
                            
                            elif(s == 'answer3'):
                                if(self.answers[self.players[0].question][2]):
                                    self.players[0].question += 1
                                    self.players[0].speed = max(1.0, self.players[0].speed - 1.0)
                            
                            elif(s == 'answer4'):
                                if(self.answers[self.players[0].question][3]):
                                    self.players[0].question += 1
                                    self.players[0].speed = max(1.0, self.players[0].speed - 1.0)
                        
                
                # self.page_function(triggered_component_list)
                
                
                
            #sprite loops
            self.playerupdate(screen)
            
            #update loops
            updatecheck = False
            first = True
            for x in self.players:
                if(time.time() - self.lastupdate > 1):
                    if(x.distance <= 0):
                        x.speed = 0.000000000001
                        pass
                        
                    updatecheck = True
                    if(x.speed > 1.0):
                        x.speed -= DECEL
                    x.distance -= x.speed
                    
                    if(first):
                        first = False
                        
                        game_image_rel_x = 7 / 100
                        game_image_rel_y = 3 / 100
                        game_image_rel_width = 38*((100-x.distance)/100) / 100 #max at 38
                        game_image_rel_height = 1 / 50
                        cover = pygame.image.load('assets/img/cover.png')
                        cover = ImageDisplay("cover", screen, game_image_rel_x, game_image_rel_y,
                                                        game_image_rel_width, game_image_rel_height,cover)
                        
                        self.components["cover"] = cover
                        
                        
                        if(x.distance < 20):
                            game_image_rel_x = (9 - (4*(20-x.distance))) / 10
                            game_image_rel_y = 4.5 / 10
                            game_image_rel_width = 1 / 6
                            game_image_rel_height = 1 / 6
                            end = pygame.image.load('assets/img/exit.png')
                            end = ImageDisplay("end", screen, game_image_rel_x, game_image_rel_y,
                                                            game_image_rel_width, game_image_rel_height,end)
                            
                            self.components["end"] = end
        
                
            if(updatecheck):
                self.lastupdate = time.time()
            
            
            pygame.display.update()




p = Game(pygame.display.set_mode((400, 400), pygame.RESIZABLE), ['who am I?']*20, [['a', 'b', 'c', 'd']]*20)
p.start(p.screen, [])





