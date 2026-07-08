## Guessing Game

import random

print("=" * 40)
print("      WELCOME TO THE NUMBER GUESSING GAME      ")
print("=" * 40)
print("I am thinking of a number between 1 and 100.")
print("Can you guess what it is?\n")

## Secret_number and input_number is created to hold value
secret_number = random.randint(1, 100)

input_number = int(input("Enter the number: "))

## Logic begins

while secret_number != input_number:
    print("Your prediction is wrong, Try again")
    if secret_number > input_number:
        print("Guess higher\n")
    else:
        print("Guess lower\n")
    input_number = int(input("Enter the number: "))

print("\nYour prediction is correct!")
