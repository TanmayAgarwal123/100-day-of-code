numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(numbers)


list_of_strings = input().split(',')
# list comprehension to convert strings to integers
numbers = [int(x) for x in list_of_strings]
# list comprehension to filter on even numbers
result = [num for num in numbers if num%2==0]
print(result)


with open("file1.txt") as file1:
    list1 = file1.readlines()
with open("file2.txt") as file2:
    list2 = file2.readlines()
result = [int(num) for num in list1 if num in list2]
print(result)