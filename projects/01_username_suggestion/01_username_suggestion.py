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
name_split = name.split()[0]
last_name_split = last_name.split()[0]
num_limited = num[-4:]  # 4 raghame akhare num
username1 = name_split + num_limited
username2 = last_name_split + year
username3 = name_split[0] + '.' + last_name_split

'''
Show results
'''
print("You can choose these useranmes:")
print(username1)
print(username2)
print(username3)







