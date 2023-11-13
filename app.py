import time
import pyautogui

from Core import state_handling
from Spy import spy
from Core import comparison_handling
from Action import action

class PetAutomationTool:
    def first_level(self):
        # set Wizard101 to active Window
        core_instance = state_handling.StateHandling()
        core_instance.set_active()
        # locates the Dance Game Popup and presses X if found
        spy_instance = spy.Spy()
        spy_instance.locate_dance_game_popup()
        time.sleep(1)
        # locates the level and selects it
        spy_instance.locate_level()
        time.sleep(1)
        # locates the play button and presses it
        spy_instance.locate_play()
        time.sleep(1.5)
        # waits for the game to load
        spy_instance.wait_for_loading()
        time.sleep(2)
        # compares the caught sequence with template
        core_instance = comparison_handling.ComparisonHandling()
        keystrokes = core_instance.compare_sequence()
        action_instance = action.Action()
        action_instance.simulate_key_presses(keys=keystrokes)


app_instance = PetAutomationTool()
app_instance.first_level()
