import copy
import time

import pyautogui

import functions

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

populate_array = functions.populate(numbers)
Original_grid = populate_array[0]
new_Grid = copy.deepcopy(Original_grid)
functions.solve(new_Grid)
check = -1
pyautogui.keyDown('alt')
pyautogui.keyDown('tab')
pyautogui.keyUp('alt')
pyautogui.keyUp('tab')
pyautogui.click(x=400, y=400)
pyautogui.press('tab')
time.sleep(1)
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
