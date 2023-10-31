
student_height = input().split()

for n in range(0, len(student_height)):
  student_height[n] = int(student_height[n])
total_height = 0

for height in student_height:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0

for student in student_height:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")