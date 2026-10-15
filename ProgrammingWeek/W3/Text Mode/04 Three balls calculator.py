#Made in Python IDLE 3.14.6

# รับค่าจำนวนลูกบอลจากผู้ใช้และแปลงเป็น integer
football = int(input("Enter number of Footballs: "))
basketball = int(input("Enter number of Basketballs: "))
volleyball = int(input("Enter number of Volleyballs: "))

# เปรียบเทียบพื้นฐานเพื่อหาค่าที่มากที่สุด
if football == basketball and football == volleyball:
    print("Equal amount.")
    
elif football > basketball and football > volleyball:
    print("Football has the maximum amount.")
    
elif basketball > football and basketball > volleyball:
    print("Basketball has the maximum amount.")
    
elif volleyball > football and volleyball > basketball:
    print("Volleyball has the maximum amount")
    

#6901012610455
#Kittipob Buayu

