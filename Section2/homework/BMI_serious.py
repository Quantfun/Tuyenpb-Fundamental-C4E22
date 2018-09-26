#Measure the BMI

height = int(input("your height in centimeter ? "))
weight = int(input("your weigt in kilogram ? "))

BMI = 100 * weight / (height * height)

print("your BMI is ",BMI)

if BMI < 16:
    print("severly underweight")

elif BMI <= 18.5:
    print("underweight")

elif BMI <= 25:
    print("normal")

elif BMI <=30:
    print("overweight")

else:
    print("obese")
