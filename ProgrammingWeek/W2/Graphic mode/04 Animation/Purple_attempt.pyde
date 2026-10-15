from processing import *
x = 0
y = 200
def setup():
  size(400,400)
def draw_red(x, y):
    fill(255,0,51)
    ellipse(x, y, 50, 50)
def draw_blue(x,y):
    fill(69,176,210)
    ellipse(400-x, y, 50, 50)
def purple(x,y):
    fill(102, 51, 153)
    ellipse(200,200,x+50,x+50)
def boom(x,y):
    fill(194, 173, 214)
    ellipse(200,200,x+75,x+75)
def white_screen():
    fill(255)
    ellipse(200,200,1000,1000)


def draw():
    global x
    draw_red(x,y)
    draw_blue(x,y)
    x = x + 4
    if x > 200:
        purple(x,y)
        if x > width:
            boom(x,y)
            if x > width+400:
                white_screen()
