print(" >>>>> BMI Calculator <<<<< ")

# Daryafte Ghad va Vazne Karbar
w = input("Please enter your weight (in kg): ")
h = input("Please enter your height (in cm): ")

w = float(w)
h = float(h)
h /= 100

# Mohasebeye BMI
bmi = w / h**2
bmi = round(bmi, 1)

# Gozaresh be karbar
print(" Your BMI is:", bmi)

if bmi<18.5:
    print("Shoma Underweight Hastid")
elif 18.5<=bmi<24.9:
    print("Tabrik, Shoma Normal Hastid")
else:
    print("Shoma Chagh Hastid")
