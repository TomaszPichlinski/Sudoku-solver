import win32con

import functions
from win32 import win32gui
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
import copy
import time
import pyautogui

populate_array = functions.populate(numbers)
Original_grid = populate_array[0]
print(populate_array[1])
new_Grid = copy.deepcopy(Original_grid)
functions.solve(new_Grid)
functions.display(new_Grid)
Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
time.sleep(3)
pyautogui.click(x=400, y=400)
pyautogui.press('tab')
check = -1
for x in range(3):
    for y in range(3):
        for z in range(3):
            for a in range(3):
                check += 1
                if check in populate_array[1]:
                    continue
                else:
                    pyautogui.press(new_Grid[x][y][z][a])
                    pyautogui.press('tab')


