from lib import login
import csv

check = login.main()
filename = "items.csv"
items = []
choice2 = ""

# def check():
#     return login.main()

def menu(datalist):
    string= ""
    for index, x in enumerate(datalist, start=1):
        string += f'{index}) {x[0]} '
        if ((index % 3) == 0 ):
            string += '\n'
    
    return string

def main():
    if (check == True):
        with open(filename, 'r') as file:
            reader = csv.reader(file)

            for stuff in reader:
                items.append(stuff)
        
            choice2 = input(menu(items) + "\nPlease select your item: ")


if __name__ == "__main__": main()
