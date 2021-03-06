from turtle import color
from lib import login
import csv
import os
import time
import math
import colorama

filename = r"C:\Users\Chopp\Desktop\Revature\Projects\AlexS-project0\database\items.csv"
items = []
choice2 = ""
cart = {}
sum = []

def menu(datalist):
    string= ""
    for index, x in enumerate(datalist):
        colorama.Style.RESET_ALL
        format_num = "{:.2f}".format(float(x[1]))
        string += f'{colorama.Fore.BLUE}{x[0]} {colorama.Fore.WHITE}-> price: {colorama.Fore.RED}${format_num}\n' if (index % 5 == 0 and index != 0 or index == (len(datalist) - 1)) else f'{colorama.Fore.BLUE}{x[0]} {colorama.Fore.WHITE}-> price: {colorama.Fore.RED}${format_num}  {colorama.Fore.WHITE}||  '

    return string

def lookup_item(item_name):
    for x in items:
        if item_name in x:
            if(item_name in cart): 
                cart[x[0]] += float(x[1])
            else:
                cart[x[0]] = float(x[1])
            print("Item found")
            return True

    print("Item not found" if item_name != '' else "Quitting..")    
    return False
    
def unit_price(name):
    for x in items:
        if name in x:
            return float(x[1])

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
    
            item_choice = input(f"{colorama.Fore.WHITE}Instruction: Please type in the exact name of the item and press enter\n(quit choosing by pressing enter with no input)\nCart[{len(cart)}]\n>>> ")

            lookup_item(item_choice)
            time.sleep(0.9)
            rerun = True if item_choice != '' else False
        

        os.system('cls')
        print("Reciept: ")
        for x, y in cart.items():
            sum.append(y)
            print(f'{x}.....${y}(x{int(y // unit_price(x))})')
        
        print(f'\nTotal.....${math.fsum(list(map(float,sum)))}')

if __name__ == "__main__": main()
