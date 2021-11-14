import pygame
import sys

sys.path.insert(1, '../../backend/database')

import RoomManager
import QuestionManager

# parent class for pages
# python.Surface screen - screen the page is to be displayed
class Page:
    def __init__(self, screen):
        self.name = "page_constructor"              # name of page
        self.run = True                             # if the page is running
        self.screen = screen                        # screen the page to display on
        self.screen_width = screen.get_width()      # screen width
        self.screen_height = screen.get_height()    # screen height
        self.input_data = {}
        self.output_data = {                               # data to and from other pages
            "current_page": self.name,
            "exit": False
        }
        self.components = {}                        # all components within the page
        self.layers = []
    # initialize all components and add them to component list
    def set_components(self):
        pass
    '''
    draw all components within component list
    '''
    def draw_components(self):
        for component in self.components.values():
            component.draw()


    '''
    resize every component in page to scale with current screen dimensions
    '''
    def resize_components(self):
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        new_screen = pygame.display.set_mode((self.screen_width, self.screen_height),
                                             pygame.RESIZABLE)
        for component in self.components.values():
            component.resize(new_screen)
            component.draw()
    '''
    main logic of page in reaction to event
    will be kept running once page starts running
    '''
    def page_function(self, event):
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
                    return self.output_data, self.input_data
                if event.type == pygame.VIDEORESIZE:
                    self.resize_components()
                triggered_component_list = []
                top_layer_triggered = False

                # go down layers at mouse pos and only trigger top layer surface
                for layer in reversed(self.layers):
                    active_layer = layer
                    pos = pygame.mouse.get_pos()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if layer.scrollable:
                            if layer.shown_display_rect.collidepoint(pos):
                                # to double check
                                layer.trigger(event)
                                print(component.name)
                                triggered_component_list.append(layer)
                                top_layer_triggered = True
                                break

                        elif layer.display_rect.collidepoint(pos):
                            #to double check
                            layer.trigger(event)
                            print(component.name)
                            triggered_component_list.append(layer)
                            top_layer_triggered = True
                            break
                if not top_layer_triggered:
                    for component in self.components.values():
                        if component.mouse_function:
                            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                                if component.trigger(event):
                                    print(component.name)
                                    triggered_component_list.append(component)
                        if component.keyboard_function:
                            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                                if component.trigger(event):
                                    print(component.name)
                                    triggered_component_list.append(component)
                self.page_function(triggered_component_list)
                #refresh function
                if (self.name == "playerroom") or (self.name == "hostroom"):
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and len(triggered_component_list) == 1:
                        if top_layer_triggered and triggered_component_list[0].navigation_surface:
                            self.output_data["current_page"] = self.name
                            return self.output_data, self.input_data
                        elif top_layer_triggered == False:
                            self.output_data["current_page"] = self.name
                            return self.output_data, self.input_data
                    else:
                        activity_status = RoomManager.get_room_activity_status(self.input_data["roomID"])
                        if activity_status:
                            self.name = "game_play"
                            self.output_data["questions"] = QuestionManager.get_questions_by_host(self.input_data["roomID"])
                            self.output_data["answers"] = QuestionManager.get_answers_by_host(self.input_data["roomID"])
                            self.output_data["current_page"] = self.name
                            return self.output_data, self.input_data
                        print("is it empty", self.input_data["roomID"])
                        player_status_dict = RoomManager.get_room_member_statuses(self.input_data["roomID"])
                        print("heloooooo")
                        player_status = list(player_status_dict.items())
                        player_status_list = ["%s %s" % x for x in player_status]
                        self.output_data["player_status"] = player_status_list
                        self.output_data["current_page"] = self.name
                        print("player_Ststus", self.output_data["player_status"])

                        return self.output_data, self.input_data
                # for navigation
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and len(triggered_component_list)==1:
                    if top_layer_triggered and triggered_component_list[0].navigation_surface:
                        self.output_data["current_page"] = self.name
                        return self.output_data, self.input_data
                    elif top_layer_triggered==False:
                        self.output_data["current_page"] = self.name
                        return self.output_data, self.input_data


            pygame.display.update()

