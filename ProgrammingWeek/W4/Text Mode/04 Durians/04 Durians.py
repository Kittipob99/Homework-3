#โค้ดนี้เขียนบน Python IDLE 3.14.6

durian_weight = float(input("Input durian weight, input 0 to conclude : "))
total_durian_weight = 0
durian_amount = 0

while durian_weight != 0:
    total_durian_weight = total_durian_weight + durian_weight
    durian_amount = durian_amount + 1
    durian_weight = float(input("Input durian weight, input 0 to conclude : "))

print("Total of ", durian_amount, "durians")
print("Average weight is ", total_durian_weight/durian_amount)

#69-010126-1045-5
#กิตติภพ บัวอยู่
    
