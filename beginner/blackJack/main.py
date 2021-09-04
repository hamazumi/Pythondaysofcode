from art import logo
import random
print(logo)

#cards in blackjack deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#deal random cards
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#calculate score for 21 (blackjack) or Ace
def calculate_score(cards): 
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Compare the user score and computer score
def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "Over 21. You lose"
  if user_score == computer_score:
    return "Tie Game"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Blackjack!!! "
  elif user_score > 21:
    return "Over 21. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win "
  elif user_score > computer_score:
    return "You win "
  else:
    return "You lose "

# Play blackjack game
def play_game():

  print(logo)

#create empty list to append cards into
  user_cards = []
  computer_cards = []
  is_game_over = False

#for 2 empty slots in list, deal cards
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

 #While game isnt over calculate scores for user and CPU
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

#IF someone has blackjack OR user goes over 21 game over is True
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
#Else ask if user would like another card
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
# If Y then deal another card, if not game over.
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
#Computer continues to get card if not blackjack and under 17 total
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

#print the outcome of game
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#Ask if user wants to play again
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()