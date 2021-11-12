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
import random




DECEL = 0.1
MINSPEED = 1.0
BLACK=(0,0,0)


class Game(Page):
    
    def __init__(self, screen, avatar = 'guy', multiplayer = False):
        super().__init__(screen)
        pygame.init()
            
            
        self.starttime = time.time()
        self.lastupdate = time.time()
        self.game_stats = {}
        self.game_stats['id'] = 0
        self.game_stats['correct'] = 0
        self.game_stats['time'] = 0.0
        self.game_stats['score'] = 0
        
        
        self.avatar = avatar
        self.speed = 1.5
        self.score = 0
        self.distance = 100.0
        self.lastavatarupdate = time.time()
        self.avatarstate = 2
        self.questionstate = 0
        
        self.font_obj=pygame.font.Font("C:\Windows\Fonts\Arial.ttf",25) 
        
        self.players = {}
        
        
        
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
        
        
        #question display
        relative_x = 7/20
        relative_y = 2/15
        relative_width = 1/5
        relative_height = 1/15
        question_text = TextDisplay("question_text", screen, relative_x, relative_y, relative_width, relative_height, self.questions[0])
        self.components["question_text"] = question_text
        
        correction = TextDisplay("correction", screen, relative_x, relative_y, relative_width, relative_height, '')
        self.components["correction"] = correction
        
        
        #answer display
        relative_x = 10 / 40
        relative_y = 7 / 10
        relative_width = 1/5
        relative_height = 1/15
        answer_text1 = TextDisplay("answer_text1", screen, relative_x, relative_y, relative_width, relative_height, self.answers[0][0])
        self.components["answer_text1"] = answer_text1
        
        relative_x = 30 / 40
        relative_y = 7 / 10
        relative_width = 1/5
        relative_height = 1/15
        answer_text2 = TextDisplay("answer_text2", screen, relative_x, relative_y, relative_width, relative_height, self.answers[0][1])
        self.components["answer_text2"] = answer_text2
        
        relative_x = 10 / 40
        relative_y = 9 / 10
        relative_width = 1/5
        relative_height = 1/15
        answer_text3 = TextDisplay("answer_text3", screen, relative_x, relative_y, relative_width, relative_height, self.answers[0][2])
        self.components["answer_text3"] = answer_text3
        
        relative_x = 30 / 40
        relative_y = 9 / 10
        relative_width = 1/5
        relative_height = 1/15
        answer_text4 = TextDisplay("answer_text4", screen, relative_x, relative_y, relative_width, relative_height, self.answers[0][3])
        self.components["answer_text4"] = answer_text4
        
        
        
        
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
        player = pygame.image.load('assets/img/'+self.avatar+'2.png')
        player = ImageDisplay("player", screen, game_image_rel_x, game_image_rel_y,
                              game_image_rel_width, game_image_rel_height,player)
        
        self.components["player"] = player
        
        
    def host_multiplayer(self):
        pass
    
    
    def join_multiplayer(self, code):
        pass
    
    
 
    def playerupdate(self, screen):
        if(time.time() - self.lastavatarupdate > 1/self.speed):
            self.avatarstate = (self.avatarstate + 1) %4
            
            game_image_rel_x = 4 / 10
            game_image_rel_y = 4.5 / 10
            game_image_rel_width = 1 / 6
            game_image_rel_height = 1 / 6
            player = pygame.image.load('assets/img/'+self.avatar+str(self.avatarstate)+'.png')
            player = ImageDisplay("player", screen, game_image_rel_x, game_image_rel_y,
                                  game_image_rel_width, game_image_rel_height,player)
            self.components['player'] = player
            self.lastavatarupdate = time.time()
            
            
    def questionupdate(self, screen, correct):
        if(self.questionstate >= len(self.questions)):
            relative_x = 7/20
            relative_y = 2/15
            relative_width = 1/5
            relative_height = 1/15
            question_text = TextDisplay("question_text", screen, relative_x, relative_y, relative_width, relative_height, 'No more questions')
            self.components["question_text"] = question_text
            return
        
        
         #question display
        if(correct):
            relative_x = 15/20
            relative_y = 1/15
            relative_width = 1/5
            relative_height = 1/15
            correction = TextDisplay("correction", screen, relative_x, relative_y, relative_width, relative_height, 'Correct Answer')
            self.components["correction"] = correction
        else:
            relative_x = 10/20
            relative_y = 1/15
            relative_width = 2/5 
            relative_height = 1/15
            correction = TextDisplay("correction", screen, relative_x, relative_y, relative_width, relative_height, 'The correct answer was : '+str(self.correct[self.questionstate-1]))
            self.components["correction"] = correction
        
        
        
         #question display
        relative_x = 7/20
        relative_y = 2/15
        relative_width = 1/5
        relative_height = 1/15
        question_text = TextDisplay("question_text", screen, relative_x, relative_y, relative_width, relative_height, self.questions[self.questionstate])
        self.components["question_text"] = question_text
        
        
        #answer display
        relative_x = 10 / 40
        relative_y = 7 / 10
        relative_width = 1/5
        relative_height = 1/15
        answer_text1 = TextDisplay("answer_text1", screen, relative_x, relative_y, relative_width, relative_height, self.answers[self.questionstate][0])
        self.components["answer_text1"] = answer_text1
        
        relative_x = 30 / 40
        relative_y = 7 / 10
        relative_width = 1/5
        relative_height = 1/15
        answer_text2 = TextDisplay("answer_text2", screen, relative_x, relative_y, relative_width, relative_height, self.answers[self.questionstate][1])
        self.components["answer_text2"] = answer_text2
        
        relative_x = 10 / 40
        relative_y = 9 / 10
        relative_width = 1/5
        relative_height = 1/15
        answer_text3 = TextDisplay("answer_text3", screen, relative_x, relative_y, relative_width, relative_height, self.answers[self.questionstate][2])
        self.components["answer_text3"] = answer_text3
        
        relative_x = 30 / 40
        relative_y = 9 / 10
        relative_width = 1/5
        relative_height = 1/15
        answer_text4 = TextDisplay("answer_text4", screen, relative_x, relative_y, relative_width, relative_height, self.answers[self.questionstate][3])
        self.components["answer_text4"] = answer_text4
                
        
        
    def get_gamedata(self):
        data = {}
        
        
        
    def add_player(self, playerName):
        self.multiplayer += 1



    def page_function(self, triggered_component_list):
        for x in triggered_component_list:
            pass


    # start running the page
    def start(self, screen, input_data):
        self.input_data = input_data
        self.questions = input_data['questions']
        self.correct = []
        self.answers = input_data['answers']
        
        for x in self.answers:
            self.correct.append(x[0])
            
        for i in range(len(self.answers)):
            random.shuffle(self.answers[i])
        
        
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
                        
                            if(s == 'answer1' and self.questionstate<len(self.questions)):
                                if(self.correct[self.questionstate] == self.answers[self.questionstate][0]):
                                    self.questionstate += 1
                                    self.speed += 1.0
                                    self.game_stats['correct'] += 1
                                    self.questionupdate(screen, True)
                                else:
                                    self.questionstate += 1
                                    self.speed = max(1.0, self.speed - 1.0)
                                    self.questionupdate(screen, False)
                            
                            elif(s == 'answer2' and self.questionstate<len(self.questions)):
                                if(self.correct[self.questionstate] == self.answers[self.questionstate][1]):
                                    self.questionstate += 1
                                    self.speed += 1.0
                                    self.game_stats['correct'] += 1
                                    self.questionupdate(screen, True)
                                else:
                                    self.questionstate += 1
                                    self.speed = max(1.0, self.speed - 1.0)
                                    self.questionupdate(screen, False)
                            
                            elif(s == 'answer3' and self.questionstate<len(self.questions)):
                                if(self.correct[self.questionstate] == self.answers[self.questionstate][2]):
                                    self.questionstate += 1
                                    self.speed += 1.0
                                    self.game_stats['correct'] += 1
                                    self.questionupdate(screen, True)
                                else:
                                    self.questionstate += 1
                                    self.speed = max(1.0, self.speed - 1.0)
                                    self.questionupdate(screen, False)
                            
                            elif(s == 'answer4' and self.questionstate<len(self.questions)):
                                if(self.correct[self.questionstate] == self.answers[self.questionstate][3]):
                                    self.questionstate += 1
                                    self.speed += 1.0
                                    self.game_stats['correct'] += 1
                                    self.questionupdate(screen, True)
                                else:
                                    self.questionstate += 1
                                    self.speed = max(1.0, self.speed - 1.0)
                                    self.questionupdate(screen, False)
                                    
                                
                self.page_function(triggered_component_list)
                
                
                
            #sprite loops
            self.playerupdate(screen)
            
            #update loops
            updatecheck = False
            first = True
            
            if(time.time() - self.lastupdate > 0.1):
                if(self.distance <= 0):
                    self.game_stats['time'] = time.time() - self.starttime
                    self.game_stats['score'] = self.speed * self.correct * 1/(self.game_stats['time'])
                    self.speed = 0.000000000001
                    
                    
                updatecheck = True
                if(self.speed > 1.0):
                    self.speed -= DECEL*0.1
                self.distance -= self.speed*0.1
                    
                game_image_rel_x = 7 / 100
                game_image_rel_y = 3 / 100
                game_image_rel_width = 38*((100-self.distance)/100) / 100 #max at 38
                game_image_rel_height = 1 / 50
                cover = pygame.image.load('assets/img/cover.png')
                cover = ImageDisplay("cover", screen, game_image_rel_x, game_image_rel_y,
                                                game_image_rel_width, game_image_rel_height,cover)
                
                self.components["cover"] = cover
                
                
                if(self.distance < 20):
                    game_image_rel_x = (9 - (4*(-self.distance))) / 10
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




p = Game(pygame.display.set_mode((400, 400), pygame.RESIZABLE))
input_data = {}
input_data['questions'] = ['who am I?', 'what is my name?']*20
input_data['answers'] = [['a', 'b', 'c', 'd'],['e', 'y', 'g', 'h']]*20

p.start(p.screen, input_data)





