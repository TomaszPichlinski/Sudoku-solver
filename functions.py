from bs4 import BeautifulSoup
import requests
import random

def populate(numbers):
    link_strona = "http://mojesudoku.pl/gra-sudoku/niemozliwa_bgbigdb.html"
    html_content = requests.get(link_strona).text
    soup = BeautifulSoup(html_content, "lxml")
    Grid = []
    Square_row = []
    Square = []
    Row = []

    licznik_row = 0
    licznik_square = 0
    licznik_square_row = 0

    for link in soup.find_all("td", {"class": "sudokuInnerCell"}):
        number_in_square = str(link)[37]
        if (number_in_square not in numbers):
            number_in_square = ' '
        if(licznik_row<3):
            Row.append(number_in_square)
            licznik_row+=1
            if(licznik_row==3):
                licznik_row=0
                Square.append(Row)
                Row=[]
                licznik_square+=1
                if(licznik_square==3):
                    licznik_square=0
                    Square_row.append(Square)
                    Square=[]
                    licznik_square_row+=1
                    if(licznik_square_row==3):
                        licznik_square_row=0
                        Grid.append(Square_row)
                        Square_row=[]

    return Grid


def display(Grid):
    for x in range(3):
        for y in range(3):
            for z in range(3):
                for field in range(3):
                    print(f'[{Grid[x][z][y][field]}]', end='')
                print(" ", end="")
            print("")
        print(" ")

def square_check(number_to_check, row_of_squares, square, grid):
    for x in range(3):
        for y in range(3):
            if number_to_check == grid[row_of_squares][square][x][y]:

                return False
    return True

def row_check(number_to_check, row_of_squares, row, grid):
    for x in range(3):
        for y in range(3):
            if number_to_check == grid[row_of_squares][x][row][y]:
                return False
    return True

def column_check(number_to_check, square, number_in_square, grid):
    for x in range(3):
        for y in range(3):
            if number_to_check == grid[x][square][y][number_in_square]:
                return False
    return True

def avaible_numbers(row_of_squares, square, row, number_in_square, grid, numbers):

    good_numbers = []
    for number in numbers:

        if check_if_correct(row_of_squares, square, row, number_in_square, grid, number):
            good_numbers.append(number)
    return good_numbers

def check_if_correct(row_of_squares, square, row, number_in_square, grid, number):
    check1 = square_check(number, row_of_squares, square, grid)
    print(check1)
    if check1:
        print("1")
        check2 = row_check(number, row_of_squares, row, grid)
        if check2:
            print("2")
            check3 = column_check(number, square, number_in_square, grid)

            if check3:
                print("3")
                return True
    return False

def find_empty(new_Grid):
    for x in range(3):
         for y in range(3):
            for z in range(3):
                 for a in range(3):
                    if new_Grid[x][y][z][a] == ' ':
                        return [x,y,z,a]
    return None



def solve(new_Grid):
    find = find_empty(new_Grid)
    if not find:
        return True
    else:
        found = find
        print(found)
    for i in range(1,10):
        if check_if_correct(found[0], found[1], found[2], found[3], new_Grid, str(i)):
            new_Grid[found[0]][found[1]][found[2]][found[3]] = str(i)
            if solve(new_Grid):
                return True
            new_Grid[found[0]][found[1]][found[2]][found[3]] = ' '
    return False
