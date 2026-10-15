#Made in Python IDLE 3.14.6
def Calculate_BMI():
    global BMI
    Weight = float(input("Input Weight in KG : "))
    Height = float(input("Input Height in meter : "))
    BMI = Weight/Height**2
    return BMI #ส่งค่า BMI ไปใช้นอก Function

Calculate_BMI()

print("Your BMI = ", BMI)

if BMI < 18.5:
    print("Underweight")
    
elif 18.5 < BMI < 25:
    print("Healthy Weight")
    
elif 25 < BMI < 30:
    print("Overweight")
    
elif BMI >= 30:
    
    if 30 < BMI < 35:
        print("Class 1 Obesity")
        
    elif 35 < BMI < 40:
        print("Class 2 Obesity")
        
    else:
        print("Class 3 Obesity (Severe)")

#6901012610455
#Kittipob Buayu
    

