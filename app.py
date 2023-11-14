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
        # set Wizard101 Game client to the active Window
        self.state_handling.set_Active()
        # locates the Dance Game Popup and presses X if found
        popup_coordinates = self.spy.locate_dance_game_popup()
        self.action.simulate_popup_press(coordinates=popup_coordinates)
        # proceeds with level selection
        level_coordinates = self.spy.locate_level()
        self.action.simulate_level_selection(coordinates=level_coordinates)
        # proceeds with play instruction
        play_button_coordinates = self.spy.locate_play()
        self.action.simulate_play_execution(coordinates=play_button_coordinates)
        # proceeds with loading screen handling and begins catching the sequence
        # after loading is complete(...)
        self.spy.wait_for_loading()
        # compares the caught sequence with templates
        key_sequence = self.comparison_handler.compare_sequence()
        self.action.simulate_key_presses(keys=key_sequence)


app_instance = PetAutomationTool()
app_instance.application_entrance()
