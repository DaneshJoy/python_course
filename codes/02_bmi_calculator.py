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

if bmi < 18.5 :
    status = 'Underweight'
elif 18.5 < bmi < 24.9 :
    status = 'Normal'
elif 25 < bmi < 29.9 :
    status = 'Overweight'
else:
    status = 'Obese'

# print("\tYour BMI is:" , round(bmi, ndigits=1))
# print("\tYou are", status)

print(f'Your BMI is : {bmi:.1f}')
print(f'You are {status}')
    
