#Made in Python IDLE 3.14.6
def Calculate_Area_of_Land():
    global Area
    Width = float(input("Input width of land in meter : "))
    Length = float(input("Input length of land in meter : "))
    Area = Width*Length
    return Area

Calculate_Area_of_Land()

print("Area : ", Area, "Square meters, enough for playing : ", end="") #รอข้อความอื่นๆ มาต่อ

if Area < 170:
    print("Nothing")

if Area >= 170:
    print("Volleyball", end="") #รอข้อความอื่นๆ มาต่อ
    
if Area >= 450:
    print(", Basketball", end="")#รอข้อความอื่นๆ มาต่อ
    
if Area >= 7000:
    print(", Football") #การใช้ if ถัดจาก if จะทำให้ if อันก่อนหน้าทำงานด้วยต่างจาก elif ที่จะทำงานแค่อันบนสุด

#6901012610455
#Kittipob Buayu

    
