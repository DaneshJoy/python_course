'''
Username Suggestion
Saeed Mohagheghi
'''

print('***>>> Username Suggestion <<<***')

# Input some data from user
# In Thonny: Ctrl + 3 --> Comment/Uncomment

first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')
birth_year = input('Please enter your birth year: ')
phone_number = input('Please enter your phone number: ')
fav_number = input('Please enter your favorite number: ')

# # Hard code to test
# first_name = 'saeed'
# last_name = 'alavi'
# birth_year = '1331'
# fav_number = '1234567'

# Get the first part of the first name
first_name_list = first_name.split()
first_name = first_name_list[0]

# Get the first part of the last name
# ---> Tamrin 1

# Create usernames
username1 = first_name + last_name
username2 = last_name + fav_number
username3 = first_name[0] + '.' + last_name + birth_year[-2:]
print('-' * 30)

# Show results to user
print('Username 1: ' + username1)
print('-' * 30)
print('Username 2: ' + username2)
print('-' * 30)
print('Username 3: ' + username3)