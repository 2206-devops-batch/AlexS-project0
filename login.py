from getpass import getpass
import sys
import csv
import re

username = ""
password = ""


filename = 'client_info.csv'

def sign_up(username, password):
     with open(filename, 'a') as file:
        file.write(f'{username}, {password}')


def lookup_database():
    with open(filename, 'r') as file:
        reader = csv.reader(file)
    return True

def main():
    if len(sys.argv) < 2:
        choice = input("Are you an existing shopper(Y/N)? or sign in as guest(ENTER) ")

        if (choice.lower() == "n"):
            choice1 = input("Would you like to sign up(Y/N)?: ")
            if (choice1.lower() == "y"):
                username = input("Username: ")
                password = input("Password: ")
                sign_up(username, password)
                return False
            else:
                print("sign in as guest")
        elif (choice.lower() == "y"):
            username = input("Username: ")
            password = getpass("Password(echo off): ")

            lookup_database() 
            return True
        else:
            print("sign in as guest")
            return True
    
    else:
        username = sys.argv[1]
        if(len(sys.argv) == 2):
            password = input("Please typed in password: ")
        else:
            password = sys.argv[2]
    
        lookup_database()

# if __name__ == "__main__": main()
