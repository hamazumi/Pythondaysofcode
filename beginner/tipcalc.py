#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator.💰")
bill = float(input("What is the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n%"))
tip_per = float(int(tip)/ 100)
total = tip / 100 * bill + bill
people = int(input("How many people splitting the bill?\n"))
each = total / people
# Below {:.2f} tells code to have 2 numbers AFTER decimal
amount = "{:.2f}".format(each)
print(f"Each person should pay ${amount}")
