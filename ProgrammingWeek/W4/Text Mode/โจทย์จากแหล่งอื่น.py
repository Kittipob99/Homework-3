#โค้ดนี้เขียนบน Python IDLE 3.14.6
password = int(input("Create your password, maximum of 4 digits : "))

while password > 9999 or password < 0:
    if password > 9999:
        print("Maximum 4 digits for password!")
        password = int(input("Create your password, maximum of 4 digits : "))
    else:
        print("Password can't be negative!")
        password = int(input("Create your password, maximum of 4 digits : "))
    
attempt = 0

while attempt < 3:
    login = int(input("Input your password : "))
    if login == password:
        print("Succeed!")
        break
    else:
        print("Log in failed!")
        attempt += 1
        if attempt == 3:
            print("Access denied!")
            
#69-010126-1045-5
#Kittipob Buayu
    
    

        
    
    
    
