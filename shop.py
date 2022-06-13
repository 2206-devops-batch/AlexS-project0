import login
import csv

check = login.main()
filename = "items.csv"
items = []

if (check == True):
    with open(filename, 'r') as file:
        reader = csv.reader(file)

        for stuff in reader:
            items.append(stuff)
        
        print(items)

       