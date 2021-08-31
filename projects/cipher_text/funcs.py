from keyboard import press_and_release
import os
import sys

def clear_screen():
    # Clear screen
    
    # For Thonny IDE
    # print()
    # press_and_release('ctrl+l')
    
    if (os.name == 'nt'):
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def apply_caesar_cipher(direction, cipher_text, s):
    '''
    A function to apply cipher algorithm
    direction: encrypt or decrypt
    cipher_text: input text
    s: shift
    '''
    
    result = ''
    
    if direction == 'decrypt':
        s = -1 * s
    
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        result += chr((ord(char) - 32 + s) % 95 + 32)
    
    return result