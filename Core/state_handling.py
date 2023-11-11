import win32gui


class state_handling:

    def is_active(self):
        hwndMain = win32gui.FindWindow('Wizard Graphical Client', 'Wizard101')
        active_window_hwnd = win32gui.GetActiveWindow()
        if hwndMain == active_window_hwnd:
            return 'true'
        else:
            return 'false'

    def set_active(self):
        hwndMain = win32gui.FindWindow('Wizard Graphical Client', 'Wizard101')
        win32gui.SetForegroundWindow(hwndMain)
