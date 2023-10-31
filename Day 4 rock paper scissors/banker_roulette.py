import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
name=random.choice(names)
print(f"{name} is going to buy the meal today!")
