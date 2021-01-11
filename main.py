import functions
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
import copy
import ctypes


Original_grid = functions.populate(numbers)
new_Grid = copy.deepcopy(Original_grid)
functions.solve(new_Grid)
functions.display(new_Grid)

MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, 'Hello', 'Window title', 0)
