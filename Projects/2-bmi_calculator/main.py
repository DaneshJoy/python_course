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
print(f"Your BMI is: {bmi} kg/m^2 because your weight is {w} and your height is {h*100}")

if bmi<18.5:
    print("Shoma Underweight Hastid")
elif 18.5<=bmi<24.9:
    print("Tabrik, Shoma Normal Hastid")
else:
    print("Shoma Chagh Hastid")
