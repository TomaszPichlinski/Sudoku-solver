import functions
import random
import copy
import ctypes
import time
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

Original_grid = functions.populate(numbers)
poprawnie = False
licznik =1
new_Grid = copy.copy(Original_grid)
while not poprawnie:

    new_Grid = copy.copy(functions.populate(numbers))

    print(f'KURWA LICNIK{licznik}')
    licznik+=1
    krok = 0
    correct_numbers= []
    for x in range(3):
        for y in range(3):
            for z in range(3):
                for a in range(3):
                    if new_Grid[x][y][z][a] == ' ':
                        correct_numbers = functions.avaible_numbers(x, y, z, a, new_Grid, numbers)
                        print(len(correct_numbers))
                        print(correct_numbers)
                        if len(correct_numbers) != 0:
                            krok+=1
                            new_Grid[x][y][z][a] = correct_numbers[random.randint(0, len(correct_numbers) - 1)]
                        elif len(correct_numbers) == 0:
                            break
                    if len(correct_numbers) == 0:
                        break
                if len(correct_numbers) == 0:
                    break
            if len(correct_numbers) == 0:
                break
        if len(correct_numbers) == 0:
            break
    print(krok)
    poprawnie = functions.general_check(new_Grid)
functions.display(new_Grid)

MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, 'Hello', 'Window title', 0)
