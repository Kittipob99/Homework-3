#Made in Python IDLE 3.14.6
#โจทย์นี้มาจาก Exercise 6.12.3. ของ Online Textbook: Think Python: How to Think Like a Computer Scientist, Allen B. Downey, 2024

#Write a boolean function, is_between(x, y, z), that returns True if x < y < z or if z < y < x, and False otherwise.

def is_between(x, y, z):
    if x < y < z or z < y < x:
        return True
    else:
        return False

#ใช้ input เพื่อให้ผู้ใช้ใส่ค่าได้เองเพื่อความสะดวก
if is_between(float(input("Input x : ")), float(input("Input y : ")), float(input("Input z : "))) == True: #หากฟังก์ชั่นเป็นจริง
    print("True") #แสดงผลลัพธ์เป็นจริง
else:
    print("False") #แสดงผลลัพธ์เป็นเท็จ

#6901012610455
#Kittipob Buayu
