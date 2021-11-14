from pygame import color
from assets.components import *
from page import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import numpy as np
from pygame.locals import *


class UniqueAnalyticsPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "uniqueanalytics"
        self.input_data = {
            "analytics": [],
            "analyticsID": "",
            "roomID": "",
            "username": ""
        }
        self.criteria = 'score'
        self.output_data = {
            "current_page": self.name,
            "prev_page": "",
            "username": "",
            "roomID": self.input_data["roomID"],
            "analyticsID": "",
            "exit": False
        }

    def plot_display(self):
        self.players = [player_result.get('player_name') for player_result in
                        sorted(self.player_results, key=lambda x: x[self.criteria], reverse=True)]
        self.players = ['Mean'] + self.players
        self.y_pos = np.arange(len(self.players))

        data = self.plot_data.get(self.criteria).get('x_data')
        max = np.max(data)
        median = np.median(data)
        min = np.min(data)
        mean = np.mean(data)
        std = np.std(data)
        stds = [std] + [0] * len(data)
        data = [mean] + data

        relative_x = 3 / 10
        relative_y = 64 / 330
        relative_width = 2 / 3
        relative_height = 195 / 330
        analytics_display_holder = MouseScrollableSurface("analytics_display_holder", self.screen, relative_x,
                                                          relative_y, relative_width, relative_height, relative_width,
                                                          relative_height,
                                                          display_screen=self.screen, on_display=True,
                                                          scroll_axis_y=True, relative_scroll_length=1 / 8)
        self.components["analytics_display_holder"] = analytics_display_holder

        plt.rcdefaults()
        plt.rcParams.update({'font.size': 14, 'font.family': 'sans-serif'})
        fig, ax = plt.subplots(1, 1,
                               figsize=(10, 10 / analytics_display_holder.width * analytics_display_holder.height))
        ax.barh(self.y_pos, data, xerr=stds, align='center',
                color=['silver', 'darkblue', 'royalblue', 'cornflowerblue', 'skyblue', 'lightblue', 'aliceblue'])
        ax.set_yticks(self.y_pos)
        ax.set_yticklabels(self.players, fontweight="bold")
        ax.invert_yaxis()
        ax.set_xlabel(self.plot_data.get(self.criteria).get('x_label'), fontweight="bold")
        ax.set_title('Max: %d;   Median: %d;   Min: %d;   Mean: %d;   σ: %d' % (max, median, min, mean, std),
                     fontweight="bold")
        fig.savefig(self.plot_data.get(self.criteria).get('fig_name'))
        analytics_diagram = pygame.image.load(self.plot_data.get(self.criteria).get('fig_name'))
        (analytics_diagram_width, analytics_diagram_height) = analytics_diagram.get_size()
        analytics_display = ImageDisplay("analytics_display", self.components["analytics_display_holder"].surface,
                                         relative_x=0, relative_y=0,
                                         relative_width=1, relative_height=(
                        analytics_diagram_height / analytics_diagram_width * self.components["analytics_display_holder"].width / self.components["analytics_display_holder"].height),
                                         image=analytics_diagram)
        analytics_display.scrollable = True
        analytics_display.relative_shown_x = analytics_display.relative_x
        analytics_display.relative_shown_y = analytics_display.relative_y
        analytics_display.relative_shown_width = analytics_display.relative_width
        analytics_display.relative_shown_height = analytics_display.relative_height
        self.components["analytics_display_holder"].add_component(analytics_display)

    # set all component variables on input screen
    def set_components(self, screen):
        self.name = "uniqueanalytics"

        # change back navigation every time page changes
        if self.input_data["prev_page"] != self.name:
            self.output_data["back_navigation"] = self.input_data["prev_page"]

        # assign output data
        self.output_data["roomID"] = self.input_data["roomID"]

        # background
        bg_img = pygame.image.load('assets/Backgrounds/analyticsbg.jpg')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        analyticsid_image_rel_x = 5 / 20
        analyticsid_image_rel_y = 1 / 40
        analyticsid_image_rel_width = 1 / 2
        analyticsid_image_rel_height = 1 / 8
        analyticsid_img = pygame.image.load('assets/Buttons/btn_plain.png')
        analyticsid_image = ImageDisplay("analyticsid_image", screen, analyticsid_image_rel_x, analyticsid_image_rel_y,
                                         analyticsid_image_rel_width, analyticsid_image_rel_height, analyticsid_img)
        self.components["analyticsid_image"] = analyticsid_image

        relative_x = 7 / 20
        relative_y = 1 / 14
        relative_width = 1 / 3
        relative_height = 1 / 12
        text_display = TextDisplay("text_display", screen, relative_x, relative_y, relative_width, relative_height,
                                   self.input_data["analyticsID"])
        self.components["text_display"] = text_display

        quiz = self.input_data["analytics"][0]
        self.player_results = self.input_data["analytics"][1]

        quiz_difficulty = quiz.get('quiz_difficulty')
        quiz_start_time = quiz.get('quiz_start_time')
        quiz_duration = (quiz.get('quiz_end_time') - quiz_start_time)
        quiz_info = ['Quiz: ' + quiz.get('quiz_name'), 'Subject: ' + quiz.get('quiz_subject'),
                     'Topic: ' + quiz.get('quiz_topic'), 'Difficulty: ' + str(quiz_difficulty),
                     'Date: ' + quiz_start_time.strftime("%b %d, %Y "), 'Duration: ' + str(quiz_duration)]
        # display
        relative_x = 1 / 30
        relative_y = 1 / 3
        relative_width = 1 / 4
        text_relative_height = 1 / 20
        shown_relative_width = 1 / 4
        shown_relative_height = 1 / 4
        text_list = quiz_info
        selectable_text_list = SelectableTextList("selectable_text_list", screen, relative_x, relative_y,
                                                  relative_width, text_relative_height, shown_relative_width,
                                                  shown_relative_height,
                                                  text_list, screen, single_select=True, passive_color="lightgrey")
        self.components["selectable_text_list"] = selectable_text_list
        self.layers.append(selectable_text_list)

        i = 0
        for player_result in self.player_results:
            i = i + 1
            player_result['completion_time'] = (player_result.get('player_end_time') - quiz_start_time).total_seconds()
            player_result['accuracy'] = player_result.get('no_of_questions_correct') / player_result.get(
                'no_of_questions_attempted') * 100
            player_result['score'] = quiz_difficulty * 1 / (player_result.get('completion_time') / 864) * (
                        1 + 0.5 * quiz.get('mode')) / 2 * player_result.get('accuracy')
        key = lambda d: d['completion_time']
        scores = [player_result.get('score') for player_result in
                  sorted(self.player_results, key=lambda x: x['score'], reverse=True)]
        accuracies = [player_result.get('accuracy') for player_result in
                      sorted(self.player_results, key=lambda x: x['accuracy'], reverse=True)]
        completion_times = [player_result.get('completion_time') for player_result in
                            sorted(self.player_results, key=lambda x: x['completion_time'], reverse=False)]

        # display
        self.criteria_switch = {'analytics_by_score_button': 'score', 'analytics_by_accuracy_button': 'accuracy',
                                'analytics_by_speed_button': 'completion_time'}
        self.plot_data = {'score': {'x_data': scores, 'x_label': 'Score', 'fig_name': 'plot_score.png'},
                          'accuracy': {'x_data': accuracies, 'x_label': 'Accuracy (%)',
                                       'fig_name': 'plot_accuracy.png'},
                          'completion_time': {'x_data': completion_times, 'x_label': 'Completion Times (s)',
                                              'fig_name': 'plot_completion_time.png'}
                          }
        self.plot_display()

        # analytics by score button:
        relative_x = 3 / 10
        relative_y = 23 / 132
        relative_width = 2 / 9
        relative_height = 1 / 28
        analytics_by_score_button = SelectableTextButtonD("analytics_by_score_button", self.screen, relative_x,
                                                          relative_y, relative_width, relative_height, "by Score",
                                                          active=(self.criteria == 'score'))
        self.components["analytics_by_score_button"] = analytics_by_score_button
        self.components["analytics_by_score_button"].active = (self.criteria == 'score')

        # analytics by accuracy button:
        relative_x = 47 / 90
        relative_y = 23 / 132
        relative_width = 2 / 9
        relative_height = 1 / 28
        analytics_by_accuracy_button = SelectableTextButtonD("analytics_by_accuracy_button", self.screen, relative_x,
                                                             relative_y, relative_width, relative_height, "by Accuracy",
                                                             active=(self.criteria == 'accuracy'))
        self.components["analytics_by_accuracy_button"] = analytics_by_accuracy_button
        self.components["analytics_by_accuracy_button"].active = (self.criteria == 'accuracy')

        # analytics by speed button:
        relative_x = 67 / 90
        relative_y = 23 / 132
        relative_width = 2 / 9
        relative_height = 1 / 28
        analytics_by_speed_button = SelectableTextButtonD("analytics_by_speed_button", self.screen, relative_x,
                                                          relative_y, relative_width, relative_height,
                                                          "by Completion Time",
                                                          active=(self.criteria == 'completion_time'))
        self.components["analytics_by_speed_button"] = analytics_by_speed_button
        self.components["analytics_by_speed_button"].active = (self.criteria == 'completion_time')

        # export button
        export_button_rel_x = 11 / 15
        export_button_rel_y = 4 / 5
        export_button_rel_width = 1 / 7
        export_button_rel_height = 1 / 7
        export_button_img = pygame.image.load('assets/Buttons/btn_export.png')
        export_button = ImageButton("export_button", screen, export_button_rel_x, export_button_rel_y,
                                    export_button_rel_width,
                                    export_button_rel_height, export_button_img)
        self.components["export_button"] = export_button

        # back button
        exit_button_rel_x = 1 / 15
        exit_button_rel_y = 4 / 5
        exit_button_rel_width = 1 / 7
        exit_button_rel_height = 1 / 7
        exit_button_img = pygame.image.load('assets/Buttons/btn_back.png')
        exit_button = ImageButton("exit_button", screen, exit_button_rel_x, exit_button_rel_y,
                                  exit_button_rel_width,
                                  exit_button_rel_height, exit_button_img)
        self.components["exit_button"] = exit_button

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            self.output_data["username"] = self.input_data["username"]
            self.output_data["analyticsID"] = self.input_data["analyticsID"]
            self.output_data["roomID"] = self.input_data["roomID"]
            self.output_data["player_status"] = []
            self.output_data["mode_toggle"] = self.input_data["mode_toggle"]
            self.output_data["toggled"] = self.input_data["toggled"]
            self.output_data["custom_quiz_selection"] = self.input_data["custom_quiz_selection"]
            self.output_data["join_host"] = self.input_data["join_host"]

            if triggered_component in [self.components["analytics_by_score_button"],
                                       self.components["analytics_by_accuracy_button"],
                                       self.components["analytics_by_speed_button"]]:
                self.criteria = self.criteria_switch.get(triggered_component.name)
                triggered_component_list.remove(triggered_component)
                self.plot_display()
                pygame.display.update()
                pygame.display.flip()

            else:
                self.output_data["prev_page"] = self.output_data["current_page"]
                if triggered_component in [self.components["exit_button"]]:
                    self.name = "analyticsselect"
            if triggered_component in [self.components["export_button"]]:
                with open(self.input_data["analytics"][0]['quiz_name'] + '_Analytics.csv', 'w') as f:
                    f.write("Name,Score,Accuracy (%),Competion Time (s)\n")
                    i = 0
                    for player in self.players[1:]:
                        f.write("%s,%s,%s,%s\n" % (player,
                                                   self.plot_data['score']['x_data'][i],
                                                   self.plot_data['accuracy']['x_data'][i],
                                                   self.plot_data['completion_time']['x_data'][i]))
                        i = i + 1
