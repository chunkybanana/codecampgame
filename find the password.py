from os import system, name
from time import sleep

def clear():

    if name == 'nt':
        _ = system('cls')
    
    else:
        _ = system('clear')

print("go to from the person and set a password and then show them the computer and tell them to try find the password")
setpassword=input("set a password ")
clear()
while-True:
    password=input("what is the password? ")
    if password == setpassword:
        print("correct")
        quit()
    else:
        print("wrong")