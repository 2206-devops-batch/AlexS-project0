import login
import csv

check = login.main()
filename = "items.csv"
items = []
choice2 = ""


def menu(list=items):
    result = ""
    


if (check == True):
    with open(filename, 'r') as file:
        reader = csv.reader(file)

        for stuff in reader:
            items.append(stuff)
        
        choice2 = input(f"{items}\nPlease select your item: ")

