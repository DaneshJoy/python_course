'''
Barname Ghore Keshi (version 2)
'''
import os
import random
import time
import my_logos
from datetime import datetime
from persiantools.jdatetime import JalaliDateTime


def print_text(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(0.1)
    print()


print(my_logos.logo1 + '\n')

today_miladi = datetime.now()
today_shamsi = JalaliDateTime.now()
# Method 1
# print(f'Emrooz: {today_miladi.year}/{today_miladi.month:0>2}/{today_miladi.day:0>2}' +
#       f' {today_miladi.hour:0>2}:{today_miladi.minute:0>2}')

# Method 2
print(today_miladi.strftime('Emrooz: %Y/%m/%d %H:%M:%S'))
print(today_shamsi.strftime('Emrooz: %Y/%m/%d %H:%M:%S'))
print(today_shamsi.strftime('%c'))

print_text('Asaami ra yeki yeki vared karde va Enter bezanid')
print_text('Naamhaye tekrari be soorate khodkar hazf mishavand')
print_text('Bad az akharin naam "exit" ra type konid')

# %% Daryafte Asaami az karbar

i = 1
names_list = []
while True:
    s = input(f'Naame Sherkat Konande {i}: ')
    i += 1

    if s.lower() == 'exit':
        break

    names_list.append(s)

# Remove duplicate items
names_list = list(set(names_list))

# %% Tedade Barandegan

while True:
    n = int(input('Tedade Barandegan: '))
    if n > len(names_list):
        print_text('Tedade barandegan az tedade sherkat' +
                   ' konandegan bishtar ast')
        continue
    else:
        break

# %% Entekhaabe Barandegan

# Clear screen
if os.name == 'nt':
    _ = os.system('cls')  # Clear screen in Windows CMD
else:
    _ = os.system('clear')  # Clear screen in Linux/Mac

print(my_logos.logo2 + '\n')

winners = random.sample(names_list, n)
# winners = '\n'.join(winners)
print('>>> Asami Barandegan:\n')
for name in winners:
    print('\t$' + '\u2500'*6 + '\u25ba ', end='')
    for c in name:
        print(c, end='', flush=True)
        time.sleep(0.1)
    print(' ☺')
    
input()
