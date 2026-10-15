#Written in Python IDLE 3.14.6
import random

week = 4
day = 7
n1 = 0
n2 = 0
temp_4week = []

while n1 < week :
    temp = []
    while n2 < day :
        temp.append(round(random.uniform(25,35),1))
        n2 += 1
    temp_4week.append(temp)
    n2 = 0
    n1 += 1

print("Temperature (℃)")
for i in range(len(temp_4week)):
    print(f"Week {i + 1} :", end=" ")
    for j in range(len(temp_4week[i])):
        print(temp_4week[i][j], end=" ")
    print()

def week_average(w):
    sum = 0
    for j in range(len(temp_4week[w])):
        sum += temp_4week[w][j]
    average = sum/len(temp_4week[w])
    return round(average,1)
    
def week_max(w):
    max = temp_4week[w][0]
    for j in range(len(temp_4week[w])):
        if max < temp_4week[w][j]:
            max = temp_4week[w][j]
    return max

def week_min(w):
    min = temp_4week[w][0]
    for j in range(len(temp_4week[w])):
        if min > temp_4week[w][j]:
            min = temp_4week[w][j]
    return min

def overall_max():
    o_max = week_max(0)
    for i in range(len(temp_4week)):
        if o_max < week_max(i):
            o_max = week_max(i)
    return o_max

def overall_min():
    o_min = week_min(0)
    for i in range(len(temp_4week)):
        if o_min > week_min(i):
            o_min = week_min(i)
    return o_min

def control_panel(week):
    print("Average temperature on week ", week , ":" ,week_average(week - 1))
    print("Maximum temperature on week ", week , ":" ,week_max(week - 1))
    print("Minimum temperature on week ", week , ":" ,week_min(week - 1))
    print("Overall maximum temperature across 4 weeks :",overall_max())
    print("Overall minimum temperature across 4 weeks :",overall_min())

control_panel(int(input("What week do you want to know? (Input 1 - 4) : ")))
#69-010126-1045-5
#Kittipob Buayu
