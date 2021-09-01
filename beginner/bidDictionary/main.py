from art import logo

print(logo)
bid_dictionary = {}
bids_done = False


def winningBid(bid_dictRecord):
  highest_bid = 0
  winner = ""
  for bidder in bid_dictRecord:
    amount = bid_dictRecord[bidder]
    if amount > highest_bid:
      highest_bid = amount
      winner = bidder
  print(f"{winner} with ${highest_bid}")

while not bids_done:
  name = input("What is your name? \n")
  bid = int(input("How much do you want to bid? \n$"))
  bid_dictionary[name] = bid
  moreBids = input("Any other bidders? y/n \n")
  if moreBids == "n":
    bids_done = True
    winningBid(bid_dictionary)



