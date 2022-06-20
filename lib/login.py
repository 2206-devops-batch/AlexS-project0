from getpass import getpass
from pickle import TRUE
import os, sys, csv, re, time
from turtle import clear
from colorama import *
import colorama


username = ""
password = ""
init(convert=True)
filename = r'C:\Users\Chopp\Desktop\Revature\Projects\AlexS-project0\database\client_info.csv'

def loading_bar(word):
    #word = "Fetching Client Infomartion..."
    toolbar_width = len(word)
  
    for i in range(toolbar_width):
        time.sleep(0.1) # do real work here
        # update the bar
        print(word[i], end = "", flush = True)


def lookup_database(username, password):
    people = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)

        for clients in reader:
            people.append(clients)  

    return (True in set(map(lambda x: username in x and password in x, people)))


def sign_up(username, password):
    if re.search('[a-zA-Z]\d+' , username) and not (lookup_database(username, password)): 
        with open(filename, 'a+') as file:
            file.writelines(f'{username},{password}\n')
            print(f"Success!! Welcome {username}")

            time.sleep(2)
            print("Reloading Screen soon")

            time.sleep(1)
            os.system('cls')
        main()
    else:
        return False

def main():
    if len(sys.argv) < 2:
        choice = input("Are you an existing shopper(y/n)?")

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

            loading_bar("Searching Database...")
            time.sleep(0.4)
            if (lookup_database(username, password)) == True:
                print(f"\n{Fore.GREEN}Success!!")
                    
                time.sleep(0.4)
                os.system('cls')
                return True
            else:
                time.sleep(0.1)
                print(f"\n{Fore.RED}Wrong username or password!!")
                return False      
        else:
            return False
    
    else:
        username = sys.argv[1]
        password = input("Please typed in a password: ") if (len(sys.argv) == 2) else sys.argv[2]    
        
        loading_bar("Searching Database...")
        time.sleep(0.4)        
        if (lookup_database(username, password)) == True:
            print(f"\n{Fore.GREEN}Success!!")  
               
            time.sleep(0.4)
            os.system('cls')
            colorama.deinit()
            return True
        else:
            time.sleep(0.1)
            print(F"\n{Fore.RED}Wrong username or password!!")
            return False  



if __name__ == "__main__": main()
