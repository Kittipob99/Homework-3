#Made in Python IDLE 3.14.6

import random

total_sum = 0
x = 0

def Choice(n): #ให้ตัวเลือกระหว่างโหมดสุ่มกับโหมดใส่ตัวเลข
    if n == 1 :
        Random_Mode()

    if n == 2 :
        Input_Mode()
        
    else: #หากตัวเลือกอยู่นอกเหนือจากที่ให้โปรแกรมจะ Error
        print("Error: there is no choice", n)
    
def Random_Mode(): #โหมดสุ่ม
    global total_sum
    global x
    
    while x != -1:
        x = random.randint(-1, 10)
        print (x)
        total_sum += x
        
    print ("Sum of random mode is : ", total_sum)

def Input_Mode(): #โหมดใส่ตัวเลข
    global total_sum
    global x
    
    while x != -1:
        x = int(input("input any integer, input -1 to end : "))
        total_sum += x
        
    print ("Sum of this session is : ", total_sum)

Choice(float(input("input 1 for Random Mode, input 2 for Input Mode : "))) #ใช้คำสั่ง input เพื่อให้โปรแกรมสามารถรับค่าตัวแปรได้โดยตรง

#6901012610455
#กิตติภพ บัวอยู่
    
