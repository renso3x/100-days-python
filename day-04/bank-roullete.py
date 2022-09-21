import random

names_string = input("Give me everbody's name, separated by a comma. ")

names = names_string.split(',')

random_choice = random.randint(0, len(names) - 1)

print(names[random_choice])