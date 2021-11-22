'''
Barname Ghore Keshi
'''
import random
import time
import my_logos
from datetime import datetime


today = datetime.now()

def print_text(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(0.1)
    print()


# Pick random logo
logo_list = [my_logos.logo1, my_logos.logo2, my_logos.logo3]
logo = random.choice(logo_list)

print(logo)
print()

print(f'Today: {today.year}/{today.month:0>2}/{today.day:0>2}' +
      f' {today.hour:0>2}:{today.minute:0>2}')

# print('Asaami ra yeki yeki vared karde va Enter bezanid\n')
s = 'Asaami ra yeki yeki vared karde va Enter bezanid'
print_text(s)

# print('Asaami tekrari be soorate khodkar hazf mishavand\n')
s = 'Asaami tekrari be soorate khodkar hazf mishavand'
print_text(s)

print_text('Type "exit" to finish')

# %% Daryafte Asami az karbar

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

winners = random.sample(names_list, n)
# winners = '\n'.join(winners)
print('>>> Asami Barandegan:\n')
for name in winners:
    print('\t$' + '\u2500'*6 + '\u25ba ', end='')
    for c in name:
        print(c, end='', flush=True)
        time.sleep(0.1)
    print(' ☺')
