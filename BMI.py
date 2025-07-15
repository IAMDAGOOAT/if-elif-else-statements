height = float(input("enter your height in cm: "))
weight = float(input("enter your weight in kg: "))

BMI = weight / (height/100)**2

print("your BMI is", BMI)

if BMI <= 18.4:
    print("You're underweigth")
elif BMI <= 24.9:
    print("You're healthy")
elif BMI <= 29.9:
    print("You're overweight")
elif BMI <= 34.9:
    print("You're severly overweight")
elif BMI <= 39.9:
    print("You're obese")
else:
    print("you are severly overweight.")