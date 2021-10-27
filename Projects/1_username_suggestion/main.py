
print('***>>> Username Suggestion <<<***')

first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')
phone_number = input('Enter your phone number: ')
birth_year = input('Enter your birth year: ')
fav_number = input('Enter your favorite number: ')

# print(type(first_name))
first_name = first_name.split()
first_name = first_name[0]

username1 = first_name + last_name
username2 = first_name + '.' + last_name
# Method 1
length = len(phone_number)
username3_1 = last_name + phone_number[length-4:length]

# Method 2
username3_2 = last_name + phone_number[-4:]

print('============================')
print('You can use the following usernames:')
print(username1)
print(username2)
print(username3_2)
