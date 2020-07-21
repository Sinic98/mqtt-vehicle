import sys
import os
import sensors

def idle():
    print("Welcome, ")
    print("***  MENU  *** \n\n")
    print("~ 1-Car Stats ~")
    print("~ 2-Air conditioning ~")
    print("~ 3-Logout ~")

    input = raw_input("Please enter the number of your choice: ")

    if input == "1":
        carstats()
    elif input == "2":
        aircond()
    elif input =="3":
        logout()

def carstats():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Car stats")
    print("Altimeter: " + sensors.Altimeter.value)
    print("Press 'b' for going back")

def aircond():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Air Cond")

def logout():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Logout")