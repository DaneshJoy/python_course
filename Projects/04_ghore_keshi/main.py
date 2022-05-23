'''
Barname Ghore Keshi
'''
import random
import time
import my_logos

# Pick random logo
logo_list = [my_logos.logo1, my_logos.logo2, my_logos.logo3]
logo = random.choice(logo_list)

print(logo)
print()
print('Asaami ra yeki yeki vared karde va Enter bezanid\n')
print('Naamhaye tekrari be soorate khodkar hazf mishavand\n')
print('Bad az akharin naam "exit" ra type konid\n')

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
    try:
        n = int(input("Tedade barandegan? : "))
    except:
        print("Tedaad bayad yek addad bashad")
        sys.exit()
        
    if n > len(names_list):
        print('Tedade barandegan az tedade sherkat \
konandegan bishtar ast')
        continue
    else:
        break

# %% Entekhaabe Barandegan

winners = random.sample(names_list, n)
# winners = '\n'.join(winners)
print('>>> Asami Barandegan:\n')
for name in winners:
    for c in name:
        print(c, end='')
        time.sleep(0.1)
    print()
