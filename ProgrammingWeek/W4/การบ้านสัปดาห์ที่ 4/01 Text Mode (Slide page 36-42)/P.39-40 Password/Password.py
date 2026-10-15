#Made in Python IDLE 3.14.6

import getpass

Tries = 3 #กำหนดจำนวนครั้งโอกาสที่ใส่ password ได้

def password():
    global Tries
    print("You have 3 tries")
    user_password = getpass.getpass("Enter your password: ")
    Tries = Tries - 1 # -1 โอกาสหลังจากที่ใส่ password
    
    while Tries > 0: #ถ้าโอกาสยังไม่หมดให้ loop ใหม่
        
        if user_password == "secret123":
            print("Access granted :)")
            break #หยุด loop เมื่อใส่ password ถูกต้อง
        
        else: #ถ้าใส่ password ผิดให้ใส่ใหม่และบอกจำนวนโอกาสที่เหลือ
            print("Access denied!", Tries, "more tries left")
            user_password = getpass.getpass("Enter your password: ")
            Tries = Tries - 1 # -1 โอกาสหลังจากที่ใส่ password

password()
#6901012610455
#กิตติภพ บัวอยู่

