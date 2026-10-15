#โค้ดนี้เขียนบน Python IDLE 3.14.6
import random
lucky_number = random.randint(1,100)

user_input = 0

while user_input != lucky_number:
    
    user_input = int(input("Guess the number : "))
    
    if user_input == 0:
        print("User exitted the game, the lucky number was : ", lucky_number)
        break
    
    elif user_input > lucky_number:
        print("Your guessed number was too high")
        
    elif user_input < lucky_number:
        print("Your guessed number was too low")
        
    else:
        print("Congratulation, you guessed it! The lucky number was : ", lucky_number)

#69-010126-1045-5
#กิตติภพ บัวอยู่
              
              
        
    
    
    
