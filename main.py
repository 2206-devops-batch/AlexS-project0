from lib import login
import csv

check = login.main()
filename = "items.csv"
items = []
choice2 = ""


def menu(datalist):
    string= ""
    for index, x in enumerate(datalist, start=1):
        string += f'{index}) {x[0]} '
        if ((index % 3) == 0 ):
            string += '\n'
    
    return string


if (check == True):
    with open(filename, 'r') as file:
        reader = csv.reader(file)

        for stuff in reader:
            items.append(stuff)
        
        choice2 = input(menu(items) + "\nPlease select your item: ")

