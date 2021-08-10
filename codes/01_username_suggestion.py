# Username Suggestion

'''
Input from user
'''

name = input("Enter your name: ")

last_name = input("Enter your last name: ")

year = input("Enter your birth year: ")

num = input("Enter your favorite number: ")

'''
Create usernames
'''
name_split = name.split()
name_split = name_split[0]
# Exercise1: Create last_name_split
num_limited = num[-4:]  # 4 raghame akhare num
username1 = name_split + num_limited
username2 = last_name + year
# Ecercise2: Create more usernames
username3 = '?'   # create your username

'''
Show results
'''
print("You can choose these useranmes:")
print(username1)
print(username2)
print(username3)







