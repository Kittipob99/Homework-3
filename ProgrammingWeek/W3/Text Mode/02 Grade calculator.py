#Made in Python IDLE 3.14.6

def Calculate_Score():
    global Score
    Score = float(input("Input Test Score : "))
    if Score > 100 or Score < 0: #ใช้คำสั่ง or เพื่อเพิ่มทางเลือก
        print("Something went wrong, please try again")
        Calculate_Score()
    return Score

Calculate_Score()

if 79 < Score <= 100:
    print("Grade : A")
elif 70 < Score <= 79:
    print("Grade : B")
elif 60 < Score <= 69:
    print("Grade : C")
elif 50 < Score <= 59:
    print("Grade : D")
elif 0 < Score <= 49:
    print("Grade : F")

#6901012610455
#Kittipob Buayu
