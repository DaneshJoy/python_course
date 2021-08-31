# Barname Ghorekeshi

import random

names = input('Please enter names (separated by ","): ')

names_list = names.split(',')

# Method 1
# i = random.randint(0, len(names_list)-1)
# print(names_list[i])

# Method 2
print(random.choice(names_list))
    



