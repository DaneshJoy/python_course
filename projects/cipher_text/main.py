'''
Cipher App
'''
import sys
import art
import funcs


funcs.clear_screen()
while True:
    # TODO: Better UI
    
    print(art.logo1)
    
    # Menu
    print('''
    Please choose:
        1- Encryption
        2- Decryption
        x- Exit
        ''')

     
    user_choice = input()
    
    funcs.clear_screen()
    
    print(art.logo1)
    
    # TODO: check if user input is valid and act
    # TODO: clear screen
    
    # Get text from user
    cipher_text = input('Enter your text: ')

    # Encrypt Text
    s = 13
    
    direction = ''
    if (user_choice == '1'):
        direction = 'encrypt'
            
    elif (user_choice == '2'):
        direction = 'decrypt'

    elif (user_choice == 'x'):
        sys.exit()
        
    result = funcs.apply_caesar_cipher(direction, cipher_text, s)
            
    # report to the user
    print('Result:', result)

    # ask user to continue or exit?
    u_c = input('''
        Do you want to continue?
            y: yes
            n: no
            ''')
    
    # TODO: clear screen

    if u_c == 'n':
        break
    
    funcs.clear_screen()





