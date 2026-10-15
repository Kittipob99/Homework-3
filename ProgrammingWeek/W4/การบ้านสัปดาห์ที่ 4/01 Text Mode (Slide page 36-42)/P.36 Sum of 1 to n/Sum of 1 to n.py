#Made in Python IDLE 3.14.6

def Sum_of_1_to_n(n): #สร้างฟังก์ชันเพื่อใช้คำนวณ
    total_sum = 1
    print("Sum of 1 to", n, "is",end=" ") #ใช้ end= เพื่อนำคำสั่ง print ที่จะมาทีหลังมาต่อท้าย
    while n > 1 : #สำหรับผู้ใช้ที่ต้องการหาผลรวมของ 1 ถึง จำนวนเต็มบวก
        total_sum += n
        n = n - 1
        
    while n < 1: #สำหรับผู้ใช้ที่ต้องการหาผลรวมของ 1 ถึง จำนวนเต็มลบ
        total_sum += n
        n = n + 1
        
    print(total_sum) #แสดงผลลัพธ์
    Sum_of_1_to_n(int(input("You want to know sum of 1 to ")))#Run โปรแกรมอีกครั้งแบบอัตโนมัติเพื่อความสะดวก
        
Sum_of_1_to_n(int(input("You want to know sum of 1 to "))) #ใช้คำสั่ง input เพื่อให้โปรแกรมสามารถรับค่าได้โดยตรง

#6901012610455
#กิตติภพ บัวอยู่


