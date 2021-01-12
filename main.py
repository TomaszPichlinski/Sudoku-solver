import win32con

import functions
from win32 import win32gui
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
import copy
import time
import pyautogui

while True:
    populate_array = functions.populate(numbers)
    Original_grid = populate_array[0]
    new_Grid = copy.deepcopy(Original_grid)
    functions.solve(new_Grid)
    check = -1
    print("XD")
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
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=1265, y=321)
    time.sleep(3)
    pyautogui.click(x=650, y=800)
    time.sleep(3)
    pyautogui.click(x=539, y=52)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('c')
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('tab')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('a')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('a')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('v')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('s')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('s')
