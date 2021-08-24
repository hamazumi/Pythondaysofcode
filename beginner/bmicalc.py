# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 

bmi = int(weight) / float(height) ** 2

print(round(bmi, 2))

if bmi < 18.5:
  print(f"{bmi} is underweight")
elif bmi < 25:
  print(f"{bmi} is normal weight")
elif bmi < 30:
  print(f"{bmi} is overweight")
elif bmi < 35:
  print(f"{bmi} is obese")
else:
  print(f"{bmi} is clinically obese")