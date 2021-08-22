import random

# Barname Ghorekeshi

names = input('Please enter names (separated by ","): ')

names_list = names.split(',')

i = random.randint(0, len(names_list)-1)

print(names_list[i])



