import functions

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']



Grid = functions.populate(numbers)
functions.display(Grid)

print(functions.avaible_numbers(1,1,1,1, Grid, numbers))
