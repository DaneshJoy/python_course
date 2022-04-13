

def calculate_bmi(h, w):
    h /= 100

    # Mohasebeye BMI
    bmi = w / h**2
    bmi = round(bmi, 1)
    return bmi