from lib import login
import csv
import os
import time
import math

filename = r"C:\Users\Chopp\Desktop\Revature\Projects\AlexS-project0\database\items.csv"
items = []
choice2 = ""
cart = {}
sum = []

def menu(datalist):
    string= ""
    for index, x in enumerate(datalist):
        format_num = "{:.2f}".format(float(x[1]))
        string += f'{x[0]} ${format_num}\n' if (index % 5 == 0 and index != 0 or index == (len(datalist) - 1)) else f'{x[0]} ${format_num}  ||  '

    return string

def lookup_item(item_name):
    for x in items:
        if item_name in x:
            cart[x[0]] = x[1]
            return True
        
    return False
    

def main():
    if (login.main() == True):
        with open(filename, 'r') as file:
            reader = csv.reader(file)

            for stuff in reader:
                items.append(stuff)

        os.system('cls')
        time.sleep(0.4)
        login.loading_bar("Loading Items...")

        time.sleep(0.8)
        rerun = True
       
        while (rerun):
            os.system('cls')        
            print(menu(items))

            item_choice = input(f"Cart[{len(cart)}]\nPlease select you item(quit choosing by entering no input): ")

            lookup_item(item_choice)
            rerun = True if item_choice != '' else False
        

        os.system('cls')
        print("Reciept: ")
        for x, y in cart.items():
            sum.append(y)
            print(f'{x}.....${y}')
        
        print(f'\nTotal.....${math.fsum(list(map(float,sum)))}')

if __name__ == "__main__": main()
