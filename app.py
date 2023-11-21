import time

from Action import action
from Core import comparison_handling
from Core import state_handling
from Spy import spy


class PetAutomationTool:
    def __init__(self, state_handling, spy, comparison_handling, action):
        self.state_handling = state_handling.StateHandling()
        self.spy = spy.Spy()
        self.comparison_handler = comparison_handling.ComparisonHandling()
        self.action = action.Action()

    def application_entrance(self):
        self.before_l1()
        for num in [4, 5, 6, 7]:
            self.after_l1(num)
            if num == 7:
                break
        self.reward_handling()

    def before_l1(self):
        self.state_handling.set_active()
        popup_coordinates = self.spy.locate_dance_game_popup()
        self.action.simulate_popup_press(coordinates=popup_coordinates)
        level_coordinates = self.spy.locate_level()
        self.action.simulate_level_selection(coordinates=level_coordinates)
        play_button_coordinates = self.spy.locate_play()
        self.action.simulate_play_execution(coordinates=play_button_coordinates)
        self.spy.wait_for_loading()
        self.spy.wait_for_start(loaded=True, num=3)
        key_sequence = self.comparison_handler.compare_sequence(num=3)
        self.action.simulate_key_presses(keys=key_sequence)

    def after_l1(self, num):
        self.spy.wait_for_start(loaded=True, num=num)
        key_sequence = self.comparison_handler.compare_sequence(num=num)
        self.action.simulate_key_presses(keys=key_sequence)

    def reward_handling(self):
        coordinates = self.spy.locate_next()
        self.action.simulate_next_selection(coordinates=coordinates)
        coordinates = self.spy.locate_finish()
        self.action.simulate_finish_selection(coordinates=coordinates)
        time.sleep(5)
        self.application_entrance()


app_instance = PetAutomationTool(state_handling, spy, comparison_handling, action)
app_instance.application_entrance()
