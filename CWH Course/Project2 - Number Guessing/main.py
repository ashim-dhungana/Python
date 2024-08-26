# NUMBER GUESSSING GAME

from random import randint

num = randint(1,100)

step=0
while True:
    guess = int(input("Guess the number: "))

    step += 1

    if (num==guess):
        print("\nYou guessed correctly!")
        break
    elif (num<guess):
        print("\nLower number please.")
    elif (num>guess):
        print("\nHigher number please.")

print(f"You guessed the correct number in {step} attempts")