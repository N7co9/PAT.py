
# Wizard101-PetAutomationTool

small scale python project utilizing pyautogui, pillow and opencv to catch and repeat the sequence from the dance game in pet pavilion.

CURRENT ISSUE / KNOWN BUGS:
- The Loading duration depends on wether the game client has already loaded the game files for the dance game or not.
- This means that, the majority of times, when the game first loads the minigame on a fresh start, the loading time will not match the expected 2s wait in the sequence catcher causing the program to fail.
- I'm looking to adress this shortly with further state handling
- All in all the code is very messy at the time being, since im experimenting with multiple libraries, looking for the most efficient solution
- I know that working with memory pointers would solve many issues, though since i don't work with python frequently, this is not within my capabilities yet.

## Installation

clone the src code and run the app.py script - requires pip and python
```bash
cd into directory
pip install requirements.txt
./app.py
```
    
## Acknowledgements

 - [wizwalker](https://github.com/wizwalker/wizwalker)
 - [Deimos](https://github.com/Slackaduts/Deimos-Wizard101)


