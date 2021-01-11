def populate(soup, numbers):
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
            number_in_square = '/'
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
    print(Grid)
    for x in range(3):
        for y in range(3):
            for z in range(3):
                for square in range(3):
                    print(Grid[x][y][z][square])

