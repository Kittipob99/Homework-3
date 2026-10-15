#จงเขียนโปรแกรมและรับค่าสำหรับการหาค่า BMI

def show_info():
    W = float(input("Input Weight (in kilogram): "))
    H = float(input("Input Height (in meters): "))
    BMI = W/H**2
    print("Your BMI is",BMI)
show_info()
print("Made by Kittipob Buayu 6901012610455")
