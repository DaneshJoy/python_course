'''
BMI Calculator
'''

'''
User input
'''
weight = input("Please enter your weight (kg): ")
height = input("Please enter your heigh (cm): ")

# Converting to float
weight = float(weight)
height = float(height)
height /= 100

'''
Calculate BMI
'''
bmi = weight / (height ** 2)

'''
Report to user
'''

if bmi <= 18.5:
    status = 'Underweight'
elif 18.5 < bmi <= 25:
    status = 'Normal'
elif 25 < bmi <= 30:
    status = 'Overweight'
elif 30 < bmi <= 35:
    status = 'Obese Class I'
elif 35 < bmi <= 40:
    status = 'Obese Class II'
else:
    status = 'Obese Class III'

# print("\tYour BMI is:" , round(bmi, ndigits=1))
# print("\tYou are", status)

print(f'Your BMI is : {bmi:.1f}')
print(f'You are {status}')


bmi_n_lower = 18.5
bmi_n_upper = 25
wn_lower = bmi_n_lower * (height ** 2)
wn_upper = bmi_n_upper * (height ** 2)

if weight > wn_upper:
    d_w = weight-wn_upper
    print(f'You should lose {int(d_w)} kg')
elif weight < wn_lower:
    d_w = wn_lower - weight
    print(f'You should gain {int(d_w)} kg')


    
