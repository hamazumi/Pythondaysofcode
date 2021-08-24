# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true = 0
love = 0

x = (name1 + name2).lower()
a = x.count('t') + x.count('r') + x.count('u') + x.count('e')
b = x.count('l') + x.count('o') + x.count('v') + x.count('e')
score = int(str(a) + str(b))
# score = int(str_score)

if score < 10 or score > 90:
  print(f"Your score is {a}{b}%, you like coke and mentos")
elif score >= 40 and score <= 50:
  print(f"Your score is {a}{b}%, you alright")
else:
    print(f"Your score is {a}{b}%")





