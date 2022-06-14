from getpass import getpass
import sys
import csv

username = ""
password = ""

def sign_up():
    print("sign up")

def lookup_database():
    print("searching in database...")
    return True

def main():
    if len(sys.argv) < 2:
        choice = input("Are you an existing shopper(Y/N)? or sign in as guest(ENTER) ")

        if (choice.lower() == "n"):
            choice1 = input("Would you like to sign up(Y/N)?: ")
            if (choice1.lower() == "Y"):
                sign_up()
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
