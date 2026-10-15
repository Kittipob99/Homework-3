#making object accelerates in Processing Python

def setup():
    size(500,500)
x = 0
y = 250
def ball(x,y):
    ellipse(x,y,50,50) #x = velocity of ball
def boom(x,y):
    ellipse(500,y,x,x)
    
def draw():
    global x
    ball(x,y)
    x = 1.01*x + 0.1 #multiply x to create acceleration
    if x > width:
        boom(x,y)
    
#Made by Kittipob 6901012610455
