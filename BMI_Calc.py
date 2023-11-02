def bmiCalc(height, weight):
    bmi = weight/height**2
    remark =''
    if bmi < 18.5: remark="Underweight"
    elif 18.5 <= bmi < 22.9: remark="Normal"
    elif 23 <= bmi < 24.9: remark="Overweight"
    elif 25 <= bmi < 29.9: remark="Obese I"
    elif bmi < 30: remark="Obese II"

    return round(bmi, 2), remark;

h = float(input("Enter height in cm: "))
w = float(input("Enter weight in kg: "))

print(bmiCalc(h/100,w))
