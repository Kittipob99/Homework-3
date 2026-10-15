#โค้ดนี้เขียนบน Python IDLE 3.14.6

print("Types of coin available : 10 baht, 5 baht, 1 baht")
temp = 1
amount_10 = 0
amount_5 = 0
amount_1 = 0
total_10 = 0
total_5 = 0
total_1 = 0
total_money = 0
mode = 0
def Choose_mode(): #เพิ่มเติมให้เปลี่ยนโหมดเป็นแบบเลือกจำนวนเหรียญเองได้
    global mode
    mode = int(input("Customize mode? 1 = yes, 0 = no : "))
    if mode == 1:
        print("Ok, Custom mode chosen")
    elif mode == 0:
        print("Ok, Normal mode chosen")
    else:
        print("Error: only 1 or 0")
        Choose_mode()
        
Choose_mode()

def Customize_mode(): #เพิ่มเติมโหมดเลือกจำนวนเหรียญเองได้
    n = int(input("Amount of money you want to exchange : "))
    
    amount_10 = int(input("Amount of 10 baht coins you want : "))
    while 10*amount_10 > n:
        print("Error: Exchanged amount exceed your money")
        amount_10 = int(input("Amount of 10 baht coins you want : "))
        
    print("Current total : ", 10*amount_10, "baht")    
    amount_5 = int(input("Amount of 5 baht coins you want : "))
    while 10*amount_10 + 5*amount_5 > n:
        print("Error: Exchanged amount exceed your money")
        amount_5 = int(input("Amount of 5 baht coins you want : "))
        
    print("Current total : ", 10*amount_10 + 5*amount_5, "baht")     
    amount_1 = int(input("Amount of 1 baht coins you want : "))
    while 10*amount_10 + 5*amount_5 + amount_1 > n:
        print("Error: Exchanged amount exceed your money")
        amount_1 = int(input("Amount of 1 baht coins you want : "))

    if n > 10*amount_10 + 5*amount_5 + amount_1:
        print("Error: Your exchanged amount is lower than your money given")
        print("Amount you tried to exchange : ", 10*amount_10 + 5*amount_5 + amount_1, "baht")
        Customize_mode()
    print("10 baht coins : ", amount_10, "coins")
    print("5 baht coins : ", amount_5, "coins")
    print("1 baht coins : ", amount_1, "coins")
    print("Sum : ", n, "baht")
    
    
if mode == 0:
    while temp != 0: #โหมดปกติตามที่โจทย์กำหนด
        n = int(input("Amount of money you want to exchange, input 0 to end the process : "))
        total_money = total_money + n
        temp = n
        if temp == 0:
            print("Total 10 baht coins : ", total_10, "coins")
            print("Total 5 baht coins : ", total_5, "coins")
            print("Total 1 baht coins : ", total_1, "coins")
            print("Sum : ", total_money, "baht")
            break
        while n >= 10:
            amount_10 = amount_10 + 1
            n = n - 10
        while n >= 5:
            amount_5 = amount_5 + 1
            n = n - 5
        while n >= 1:
            amount_1 = amount_1 + 1
            n = n - 1
        print("10 baht coins : ", amount_10, "coins")
        print("5 baht coins : ", amount_5, "coins")
        print("1 baht coins : ", amount_1, "coins")
        total_10 = total_10 + amount_10
        total_5 = total_5 + amount_5
        total_1 = total_1 + amount_1
        amount_10 = 0
        amount_5 = 0
        amount_1 = 0
        
if mode == 1: #เพิ่มเติมโหมดเลือกจำนวนเหรียญเองได้
    Customize_mode()
   
#6901012610455
#Kittipob Buayu
