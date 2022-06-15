from getpass import getpass
from pickle import TRUE
import sys
import csv
import re
import time
import pathlib

username = ""
password = ""

filename = r'C:\Users\Chopp\Desktop\Revature\Projects\AlexS-project0\database\client_info.csv'

def sign_up(username, password):
    regex = re.match("^[a-zA-Z]\d+", username)

    with open(filename, 'a') as file:
        if regex != None:
            file.write(f'{username}, {password}')
            return True
        else:
            print("username must have letters and numbers")
            return False


def loading_bar():
    word = "Fetching Client Infomartion..."
    toolbar_width = len(word)
  
    for i in range(toolbar_width):
        time.sleep(0.1) # do real work here
        # update the bar
        print(word[i], end = "", flush = True)

def lookup_database(username):
    with open(filename, 'r') as file:
            print(file.read())

        

def main():
    if len(sys.argv) < 2:
        choice = input("Are you an existing shopper(y/n)? or sign in as guest(ENTER) ")

        if (choice.lower() == "n"):
            choice1 = input("Would you like to sign up(Y/N)?: ")
            if (choice1.lower() == "y"):
                username = input("Username (Must have atleast letters and numbers): ")
                password = input("Password: ")
                sign_up(username, password)
                return False
            else:
                print("sign in as guest")
        elif (choice.lower() == "y"):
            username = input("Username: ")
            password = getpass("Password(echo off): ")

            return (lookup_database(username))            
        else:
            print("sign in as guest")
            return True
    
    else:
        username = sys.argv[1]
        password = input("Please typed in a password: ") if (len(sys.argv) == 2) else sys.argv[2]    
        lookup_database()

if __name__ == "__main__": main()
