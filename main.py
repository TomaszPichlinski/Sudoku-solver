import functions

numbers = ['1','2', '3', '4', '5', '6', '7','8','9']


Grid = functions.populate(numbers)
functions.display(Grid)

functions.check('4',0,2,0,0, Grid)
