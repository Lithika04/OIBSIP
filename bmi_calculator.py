print("----BMI CALCULATOR---")
try:
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))
except TypeError:
    print("Invalid input")
bmi = weight / (height/100)**2
x = round(bmi,2)
print(f"You BMI is :",x)

if bmi < 18.5:
    print("---YOU ARE UNDERWEIGHT---")
elif (bmi >= 18.5 and bmi <25):
    print("---YOU ARE HEALTHY---")
elif (bmi  >25 and bmi<30):
    print("---YOU ARE OVERWEIGHT---")
elif (bmi >=30 and bmi< 35):
    print("--- YOU ARE IN OBESE CLASS I---")
elif (bmi >= 35 and bmi <40):
    print("---YOU ARE OBESE CLASS II---")
else:
    print("--- YOU ARE OBESE CLASS III---")
