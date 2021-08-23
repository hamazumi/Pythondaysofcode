print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride!")
  age = int(input("Age? "))
  if age < 12:
    bill = 5
    print("$5")
  elif age <= 18:
    bill = 7
    print("$7")
  else:
    bill = 12
    print("$12")
  photo = input("Want photo? Y or N \n ")
  if photo == "Y":
    bill += 3
  print(f"Total cost is ${bill}")
  
else:
  print("TOO SHORT!")