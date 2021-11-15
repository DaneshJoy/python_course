'''
Strong Password Generator
'''
import random
from prettytable import PrettyTable


print(r'''
  _____ _                           _____
 / ____| |                         |  __ \
| (___ | |_ _ __ ___  _ __   __ _  | |__) |_ _ ___ ___
 \___ \| __| '__/ _ \| '_ \ / _` | |  ___/ _` / __/ __|
 ____) | |_| | | (_) | | | | (_| | | |  | (_| \__ \__ \
|_____/ \__|_|  \___/|_| |_|\__, | |_|   \__,_|___/___/
                             __/ |
                            |___/
                            ''')
# %% Input from user
num_char = int(input('How many characters? '))
num_digits = int(input('How many digits? '))
num_symbols = int(input('How many symbols? '))

# %% Creating character lists
chars_lower = 'abcdefghijklmnopqrstuvwxyz'
chars_upper = chars_lower.upper()
chars = chars_lower + chars_upper
digits = '0123456789'
symbols = '~!@#$%^&*()_+`-=?><'

# %% Generate n passwords
n = 5
passwords = []
my_table = PrettyTable()
my_table.field_names = ['#', 'Password']
for i in range(n):
    # Pick random characters from our lists
    sampled_chars = random.sample(chars, num_char)
    sampled_digits = random.sample(digits, num_digits)
    sampled_symbols = random.sample(symbols, num_symbols)

    # Create final password
    final_pass_list = sampled_chars + sampled_digits + sampled_symbols
    random.shuffle(final_pass_list)
    # Convert list to string using join
    final_pass = ''.join(final_pass_list)

    passwords.append(final_pass)
    print(f'Suggested Password {i+1}: {final_pass}')

    # add a row to the table
    my_table.add_row([i+1, final_pass])

print(my_table)