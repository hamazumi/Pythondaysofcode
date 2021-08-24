# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

num_people = len(names)
# below needs to be minus 1 because List/Array starts at 0
ran_person = random.randint(0,num_people - 1)

single_name = names[ran_person]
print(f"{single_name} is paying today!!")

# OR
person_pays = random.choice(names)
print(person_pays + " is paying today!!")