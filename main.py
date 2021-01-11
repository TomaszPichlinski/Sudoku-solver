from bs4 import BeautifulSoup
import requests
import functions
link_strona="http://mojesudoku.pl/gra-sudoku/niemozliwa_bgbigdb.html"


html_content = requests.get(link_strona).text
numbers = ['1','2', '3', '4', '5', '6', '7','8','9']
soup = BeautifulSoup(html_content, "lxml")



Grid = functions.populate(soup, numbers)
functions.display(Grid)

