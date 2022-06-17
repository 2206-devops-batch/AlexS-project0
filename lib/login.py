from getpass import getpass
from pickle import TRUE
import os
import sys
import csv
import re
import time
from turtle import clear

username = ""
password = ""

filename = r'C:\Users\Chopp\Desktop\Revature\Projects\AlexS-project0\database\client_info.csv'

def sign_up(username, password):

    with open(filename, 'a+') as file:
        file.writelines(f'{username},{password}\n')
        print(f"Success! Welcome {username}")

        time.sleep(1)
        print("Reloading Screen soon")

        time.sleep(2)
        os.system('cls')
    

    main()
        

def loading_bar(word):
    #word = "Fetching Client Infomartion..."
    toolbar_width = len(word)
  
    for i in range(toolbar_width):
        time.sleep(0.1) # do real work here
        # update the bar
        print(word[i], end = "", flush = True)

    return True

def lookup_database(username, password):
    people = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)

        for clients in reader:
            people.append(clients)  

    return (True in set(map(lambda x: username in x and password in x, people)))


def main():
    if len(sys.argv) < 2:
        choice = input("Are you an existing shopper(y/n)? or sign in as guest(ENTER) ")

        if (choice.lower() == "n"):
            choice1 = input("Would you like to sign up(y/n)?: ")
            if (choice1.lower() == "y"):
                username = input("Username: ")
                password = input("Password: ")
                sign_up(username, password)
            else:
                return False
        elif (choice.lower() == "y"):
            username = input("Username: ")
            password = getpass("Password(echo off): ")

            return (lookup_database(username, password))            
        else:
            return False
    
    else:
        username = sys.argv[1]
        password = input("Please typed in a password: ") if (len(sys.argv) == 2) else sys.argv[2]    
        lookup_database(username, password)


if __name__ == "__main__": main()
