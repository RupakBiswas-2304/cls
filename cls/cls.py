from os import system
from platform import system as stm

def cls():

    """ Clear the screen, Usefull while working with the interpreter """

    os = stm()
    if os == "Linux":
        system("clear")
    elif os == "Windows":
        system("cls")
    else:
        system("clear")