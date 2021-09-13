from art import logo, vs
from game_data import data
import random


def random_account():
  return random.choice(data)

def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, followers1, followers2):
  #check to return true or false statement
  if followers1 > followers2:
    return guess == "a"
  else:
    return guess == "b"

def game():
  print(logo)
  score = 0
  end_game = False
  account1 = random_account()
  account2 = random_account()

  while end_game == False:
    account1 = account2
    account2 = random_account()

    while account1 == account2:
      account2 = random_account()

    print(f"Compare A: {format_data(account1)}.")
    print(vs)
    print(f"Against B: {format_data(account2)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    follower_count1 = account1["follower_count"]
    follower_count2 = account2["follower_count"]
    answer = check_answer(guess, follower_count1, follower_count2)
  
    if answer:
      score += 1
      print(f"Your score is {score}")
    else:
      end_game = True
      print(f"Wrong, final score:{score}")

game()

