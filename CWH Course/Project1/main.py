# ROCK PAPER SCISSORS GAME

'''
    1 for rock
    -1 for paper
    0 for scissors
'''

import random

computer = random.choice([1,-1,0])

choice = input("Enter your choice: ")
youDict = {"r":1, "p":-1, "s":0}
reverseDict = {1:"Rock", -1:"Paper", 0:"Scissors"}

you = youDict[choice]

print(f"\nYou choose {reverseDict[you]} & computer chose {reverseDict[computer]}")


if (computer==you):
    print("It is a draw!")

else:
    if (computer==1 and you==-1):
        print("You win!")

    elif (computer==-1 and you==0):
        print("You win!")

    elif (computer==0 and you==1):
        print("You win!")

    elif (computer==1 and you==0):
        print("You Lose!")

    elif (computer==-1 and you==1):
        print("You Lose!")

    elif (computer==0 and you==-1):
        print("You Lose!")