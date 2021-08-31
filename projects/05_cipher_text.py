'''
Cipher App
'''

while True:
    # TODO: Better UI
    
    # Menu
    print('''
    Please choose:
        1- Encryption
        2- Decryption
        x- Exit
        ''')
 
    user_choice = input()
    
    
    # TODO: check user choice and act
    # TODO: check if user input is valid and act
    # TODO: clear screen

    # Get text from user
    cipher_text = input('Enter your text: ')

    # Encrypt Text
    s = 13
    result = ''
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
        

    # TODO: Decrypt

            
    # report to the user
    print('Encrypted text:', result)

    # ask user to continue or exit?
    u_c = input('''
        Do you want to continue?
            y: yes
            n: no
            ''')
    
    # TODO: clear screen

    if u_c == 'n':
        break





