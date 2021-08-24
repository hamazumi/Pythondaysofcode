# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
t_height = 0
t_students = 0

for height in student_heights:
  t_height += int(height)
  t_students += 1
print(t_height)
print(t_students)

avg_height = round(t_height / t_students)
print("Average height of students is " + str(avg_height))



