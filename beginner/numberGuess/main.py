from art import logo
import random
print(logo)
print("Welcome to the guessing game! I'm thinking of a number between 1-100. ")
random_number = random.randrange(1,100)
turns = 0
print(f"Hint, correctt number is {random_number}")

level = input("Choose 'easy' or 'hard':\n")
if level == 'easy':
  turns = 10
else:
  turns = 5

print(f"You have {turns} tries remaining to guess the #! ")


while turns != 0:
  guess = int(input("Make a guess: \n"))
  if guess == random_number:
    print("You Guessed it") 
  elif guess > random_number:
    turns -= 1
    print("Guess Lower Number")
    print(f"You have {turns} tries remaining to guess the #! ")
  else:
    turns -= 1
    print("Guess Higher Number")
    print(f"You have {turns} tries remaining to guess the #! ")

if turns == 0:
  print("Ran out of guesses, you lose")
