#โค้ดนี้เขียนบน Python IDLE 3.14.6
n = 1
divider = 1
save = 0
while n <= 50:
    
    while divider < n:
        if n%divider == 0:
            save = save + divider
        divider = divider + 1
        
    if save == n:
        print(n, "is a perfect number")
    divider = 1
    save = 0
    n = n + 1

#69-010126-1045-5
#กิตติภพ บัวอยู่
    
