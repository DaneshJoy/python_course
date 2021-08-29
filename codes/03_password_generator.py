'''
Strong Password Generator
'''
import random


n_letters = int(input('How many letters? : '))
n_numbers = int(input('How many numbers? : '))
n_symbols = int(input('How many symbols? : '))

# List of letters
letters = 'abcdefghijklmnopqrstuvwxyz'
letters_list = list(letters)
letters_upper = letters.upper()
letters_list_upper = list(letters_upper)
# Method 1
letters_list = letters_list + letters_list_upper
# Method 2
#letters_list.extend(letters_list_upper)

# List of numbers
numbers = '0123456789'
numbers_list = list(numbers)

# List of symbols
symbols = '~!@#$%^&*-_=+?.'
symbols_list = list(symbols)

# Create random password
list1 = []
for i in range(n_letters):
    list1.append(random.choice(letters_list))

list2 = []
for i in range(n_numbers):
    list2.append(random.choice(numbers_list))

list3 = []
for i in range(n_symbols):
    list3.append(random.choice(symbols_list))

password = list1 + list2 + list3
random.shuffle(password)
password = ''.join(password)

print(f'Your Password: {password}')
    
    