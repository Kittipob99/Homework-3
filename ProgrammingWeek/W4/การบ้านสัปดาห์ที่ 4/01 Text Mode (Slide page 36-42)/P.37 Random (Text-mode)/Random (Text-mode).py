#Made in Python IDLE 3.14.6

import random
def random_x():
    x = random.randint(-5,5)

    print(x)
    if x < 0: #แสดง x is negative ถ้า x ต่ำกว่า 0
        print("x is negative")
    else: #แสดง x is not negative ถ้า x มากกว่าเท่ากับ 0
        print("x is not negative")

    n = int(input("Input 1 to try again : ")) #ให้ตัวเลือกในการ Run โปรแกรมใหม่อีกครั้ง
    
    if n == 1:
        random_x()
    else: 
        print("End")

random_x()

#6901012610455
#กิตติภพ บัวอยู่
