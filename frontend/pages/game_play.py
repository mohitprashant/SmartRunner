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
import socket




DECEL = 0.1
MINSPEED = 1.0
BLACK=(0,0,0)
SPORT = 4000
CPORT = 4100


class Game(Page):
    
    def __init__(self, screen, multiplayer = False):
        super().__init__(screen)
        pygame.init()
        self.is_server = False
        self.is_client = False
        self.multiplayer =  multiplayer
        
        
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
        relative_x = 3/20
        relative_y = 2/15
        relative_width = 4/5
        relative_height = 1/15
        question_text = TextDisplay("question_text", screen, relative_x, relative_y, relative_width, relative_height, self.questions[0])
        self.components["question_text"] = question_text
        
        correction = TextDisplay("correction", screen, relative_x, relative_y, relative_width, relative_height, '')
        self.components["correction"] = correction
        
        
        #answer display
        relative_x = 9 / 40
        relative_y = 29.5 / 40
        relative_width = 1/5
        relative_height = 1/15
        answer_text1 = TextDisplay("answer_text1", screen, relative_x, relative_y, relative_width, relative_height, self.answers[0][0])
        self.components["answer_text1"] = answer_text1
        
        relative_x = 30 / 40
        relative_y = 29.5 / 40
        relative_width = 1/5
        relative_height = 1/15
        answer_text2 = TextDisplay("answer_text2", screen, relative_x, relative_y, relative_width, relative_height, self.answers[0][1])
        self.components["answer_text2"] = answer_text2
        
        relative_x = 9 / 40
        relative_y = 35.5 / 40
        relative_width = 1/5
        relative_height = 1/15
        answer_text3 = TextDisplay("answer_text3", screen, relative_x, relative_y, relative_width, relative_height, self.answers[0][2])
        self.components["answer_text3"] = answer_text3
        
        relative_x = 30 / 40
        relative_y = 35.5 / 40
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
        
        
        for x in self.players:
            multiplayer = pygame.image.load('assets/img/'+x.avatar+'2.png')
            multiplayer = ImageDisplay("player", screen, game_image_rel_x, game_image_rel_y,
                              game_image_rel_width, game_image_rel_height,multiplayer)
        
        
    def host_multiplayer(self):
        if(multiplayer == False):
            print('Multiplayer not enabled')
            return
        
        self.is_server = True
        self.is_client = False
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind(('localhost', SPORT))
        
            
    
    def join_multiplayer(self, code):
        if(multiplayer == False):
            print('Multiplayer not enabled')
            return
        
        self.is_server = False
        self.is_client = True
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.bind(('localhost', CPORT))
        self.server = (code, SPORT)
            
    
 
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
            
        for x in self.players:
            pass
            
            
            
    def questionupdate(self, screen, correct):
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
        
        
        
        if(self.questionstate >= len(self.questions)):
            relative_x = 3/20
            relative_y = 2/15
            relative_width = 4/5
            relative_height = 1/15
            question_text = TextDisplay("question_text", screen, relative_x, relative_y, relative_width, relative_height, 'No more questions')
            self.components["question_text"] = question_text
            return
        
        #question display
        relative_x = 3/20
        relative_y = 2/15
        relative_width = 4/5
        relative_height = 1/15
        question_text = TextDisplay("question_text", screen, relative_x, relative_y, relative_width, relative_height, self.questions[self.questionstate])
        self.components["question_text"] = question_text
        
        
        #answer display
        relative_x = 9 / 40
        relative_y = 29.5 / 40
        relative_width = 1/5
        relative_height = 1/15
        answer_text1 = TextDisplay("answer_text1", screen, relative_x, relative_y, relative_width, relative_height, self.answers[self.questionstate][0])
        self.components["answer_text1"] = answer_text1
        
        relative_x = 30 / 40
        relative_y = 29.5 / 40
        relative_width = 1/5
        relative_height = 1/15
        answer_text2 = TextDisplay("answer_text2", screen, relative_x, relative_y, relative_width, relative_height, self.answers[self.questionstate][1])
        self.components["answer_text2"] = answer_text2
        
        relative_x = 9 / 40
        relative_y = 35.5 / 40
        relative_width = 1/5
        relative_height = 1/15
        answer_text3 = TextDisplay("answer_text3", screen, relative_x, relative_y, relative_width, relative_height, self.answers[self.questionstate][2])
        self.components["answer_text3"] = answer_text3
        
        relative_x = 30 / 40
        relative_y = 35.5 / 40
        relative_width = 1/5
        relative_height = 1/15
        answer_text4 = TextDisplay("answer_text4", screen, relative_x, relative_y, relative_width, relative_height, self.answers[self.questionstate][3])
        self.components["answer_text4"] = answer_text4
                
    
    def display_score(self, screen):
        relative_x = 10/20
        relative_y = 5/17
        relative_width = 1/5
        relative_height = 1/15
        score_display = TextDisplay("score_display", screen, relative_x, relative_y, relative_width, relative_height, 'Score : '+str(self.game_stats['score']//1))
        self.components["score_display"] = score_display
        
        relative_x = 10/20
        relative_y = 6/17
        relative_width = 1/5
        relative_height = 1/15
        time_display = TextDisplay("time_display", screen, relative_x, relative_y, relative_width, relative_height, 'Time taken : '+str(self.game_stats['time']))
        self.components["time_display"] = time_display
        
        relative_x = 10/20
        relative_y = 7/17
        relative_width = 1/5
        relative_height = 1/15
        correct_display = TextDisplay("correct_display", screen, relative_x, relative_y, relative_width, relative_height, 'Correct : '+str(self.game_stats['correct'])+'/'+str(len(self.questions)))
        self.components["correct_display"] = correct_display
        
        
        game_image_rel_x = 9 / 10
        game_image_rel_y = 1 / 10
        game_image_rel_width = 1 / 10
        game_image_rel_height = 1 / 10
        exit_btn = pygame.image.load('assets/img/exit_btn.png')
        exit_btn = ImageDisplay("exit_btn", screen, game_image_rel_x, game_image_rel_y,
                                        game_image_rel_width, game_image_rel_height,exit_btn)
        self.components["exit_btn"] = exit_btn
    
    
        
    def get_gamedata(self):
        return self.game_stats



    def page_function(self, triggered_component_list):
        for x in triggered_component_list:
            if(x == 'exit_btn'):
                pygame.quit()


    # start running the page
    def start(self, screen, input_data):
        self.input_data = input_data
        
        self.starttime = time.time()
        self.lastupdate = time.time()
        self.game_stats = {}
        self.game_stats['id'] = 0
        self.game_stats['correct'] = 0
        self.game_stats['time'] = 0
        self.game_stats['score'] = 0
        self.game_stats['attempted'] = 0
        
        if('avatar' in input_data.keys()):
            self.avatar = input_data['avatar']
        else:
            self.avatar = 'guy'
            
        self.speed = 15
        self.score = 0
        self.distance = 100.0
        self.lastavatarupdate = time.time()
        self.avatarstate = 2
        self.questionstate = 0
        
        # self.font_obj=pygame.font.Font("C:\Windows\Fonts\Arial.ttf",25) 
        
        self.players = {}     
        
        self.questions = input_data['questions']
        self.correct = []
        self.answers = input_data['answers']
        
        for x in self.answers:
            self.correct.append(x[0])
            
        for i in range(len(self.answers)):
            random.shuffle(self.answers[i])
        
        ##################################
        
        self.output_data["current_page"] = self.name
        self.set_components(screen)
        
        
        
        while self.run:
            #Execute data transfer
            if(self.multiplayer == True):
                if(self.is_client):
                    message = self.avatar + str(self.avatarstate) + ' ' + str(self.distance)
                    self.client.sendto(message, self.server)
                    
                    data, addr = s.recvfrom(1024)
                    data = data.decode('utf-8')
                    data = data.split()
                    for i in range(len(data)):
                        if(i%2 != 0):
                            continue
                        self.players[i] = (data[i], int(data[i+1]))
                    
                    
                elif(self.is_server):
                    data, addr = s.recvfrom(1024)
                    data = data.decode('utf-8')
                    data = data.split()
                    self.players[addr] = (data[0], int(data[1]))
                    
                    message = ''
                    for x in self.players.keys():
                        if(x == addr):
                            continue
                        message += self.players[x][0] + ' ' + str(self.players[x][1]) + ' '
                        
                    message += self.avatar + str(self.avatarstate) + ' ' + str(self.distance)
                        
                    s.sendto(message.encode('utf-8'), addr)
                    
                    
            
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
                            triggered_component_list.append(s)
                        
                            if(s == 'answer1' and self.questionstate<len(self.questions) and self.distance <= 0):
                                if(self.correct[self.questionstate] == self.answers[self.questionstate][0]):
                                    self.questionstate += 1
                                    self.speed += 1.0
                                    self.game_stats['correct'] += 1
                                    self.questionupdate(screen, True)
                                else:
                                    self.questionstate += 1
                                    self.speed = max(1.0, self.speed - 1.0)
                                    self.questionupdate(screen, False)
                            
                            elif(s == 'answer2' and self.questionstate<len(self.questions) and self.distance <= 0):
                                if(self.correct[self.questionstate] == self.answers[self.questionstate][1]):
                                    self.questionstate += 1
                                    self.speed += 1.0
                                    self.game_stats['correct'] += 1
                                    self.questionupdate(screen, True)
                                else:
                                    self.questionstate += 1
                                    self.speed = max(1.0, self.speed - 1.0)
                                    self.questionupdate(screen, False)
                                    
                            
                            elif(s == 'answer3' and self.questionstate<len(self.questions) and self.distance <= 0):
                                if(self.correct[self.questionstate] == self.answers[self.questionstate][2]):
                                    self.questionstate += 1
                                    self.speed += 1.0
                                    self.game_stats['correct'] += 1
                                    self.questionupdate(screen, True)
                                else:
                                    self.questionstate += 1
                                    self.speed = max(1.0, self.speed - 1.0)
                                    self.questionupdate(screen, False)
                            
                            elif(s == 'answer4' and self.questionstate<len(self.questions) and self.distance <= 0):
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
                    if(self.game_stats['time'] == 0):
                        self.game_stats['time'] = (time.time() - self.starttime)//1
                        self.game_stats['score'] = self.speed * self.game_stats['correct'] - (self.game_stats['time'])
                        self.game_stats['attempted'] = self.questionstate
                    self.speed = 0.000000000001
                    
                    self.display_score(screen)
                    
                    
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
input_data['questions'] = ['who am I?', 'what is my name?']*2
input_data['answers'] = [['a', 'b', 'c', 'd'],['e', 'y', 'g', 'h']]*2

p.start(p.screen, input_data)





