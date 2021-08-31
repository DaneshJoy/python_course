'''
Rocks / Paper / Scissors Game
'''
import random

while True:
    # User Choice
    print('Please choose:')
    print('\tR -> Rocks')
    print('\tP -> Paper')
    print('\tS -> Scissors')
    print('\tE -> End Game')

    user_choice = input()
    user_choice = user_choice.lower()
    
    if (user_choice != 's') and (user_choice != 'r') and (user_choice != 'p') and (user_choice != 'e'):
        print('invalid Choice')
        continue
    
    if user_choice == 'e':
        break

    list1 = ['r', 'p', 's']
    robot_choice = random.choice(list1)

    winner = 0 # winner =1 if user wins / winner=2 if robot wins / winner=0 means tie
    if (user_choice == 'r') and (robot_choice == 'p'):
        winner = 2
    elif (user_choice == 'r') and (robot_choice == 's'):
        winner = 1
    elif (user_choice == 'p') and (robot_choice == 'r'):
        winner = 1
    elif (user_choice == 'p') and (robot_choice == 's'):
        winner = 2
    elif (user_choice == 's') and (robot_choice == 'r'):
        winner = 2
    elif (user_choice == 's') and (robot_choice == 'p'):
        winner = 1

    print('Your choice: ', user_choice)
    print('Robot Choice:', robot_choice)

    if winner == 0:
        print('Mosavi')
    elif winner == 1:
        print('Shoma barande shodid')
    else:
        print('Robot Barande Shod')

    

