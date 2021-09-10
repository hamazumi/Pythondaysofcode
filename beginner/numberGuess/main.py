from art import logo
from random import randint

#Set player turns to zero
turns = 0 

#Function to check for answer
def check(guess, number, turns):
    if guess > number:
        print("Too high")
        return turns - 1
    elif guess < number:
        print("Too low")
        return turns - 1
    else:
        print(f"Yes!, number is {number}!")

#Function to set difficulty level
def difficulty():
    level = input("Choose 'easy' or 'hard':\n")
    if level == 'easy':
        return turns + 10
    else:
        return turns + 5

def game():
    print(logo)
    print("Welcome to the guessing game! I'm thinking of a number between 1-100. ")
    #Choosing a random number between 1-100
    number = randint(1, 100)
    print(f"Hint, correct number is {number}")

    turns = difficulty()
    guess = 0

    #Repeat the guessing functionality if they get it wrong.
    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")

        #Let the user guess a number.
        guess = int(input("Make a guess: "))

        #Track the number of turns and reduce by 1 if they get it wrong.
        turns = check(guess, number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")
game()