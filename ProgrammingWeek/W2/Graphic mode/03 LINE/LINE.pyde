from processing import *

x = 25
gap = 50

# ---------- LINE ----------
def L(x, y):
    line(x, y, x, y + 50)
    line(x, y + 50, x + 25, y + 50)

def I(x, y):
    line(x, y, x + 25, y)
    line(x + 12.5, y, x + 12.5, y + 50)
    line(x, y + 50, x + 25, y + 50)

def N(x, y):
    line(x, y, x, y + 50)
    line(x, y, x + 25, y + 50)
    line(x + 25, y, x + 25, y + 50)

def E(x, y):
    line(x, y, x, y + 50)
    line(x, y, x + 25, y)
    line(x, y + 25, x + 20, y + 25)
    line(x, y + 50, x + 25, y + 50)

def setup():
    size(400, 400)

def draw():
    background(255)

    # ---------- LINE ----------
    xpos = x
    top = 25

    L(xpos, top)
    xpos += gap

    I(xpos, top)
    xpos += gap

    N(xpos, top)
    xpos += gap

    E(xpos, top)

    # ---------- ENIL ----------
    xpos = x
    top = 150

    E(xpos, top)
    xpos += gap

    N(xpos, top)
    xpos += gap

    I(xpos, top)
    xpos += gap

    L(xpos, top)
    xpos += gap
    
    #---------- LINEN ----------
    xpos = x
    top = 275
    
    L(xpos, top)
    xpos += gap
    
    I(xpos, top)
    xpos += gap
    
    N(xpos, top)
    xpos += gap
    
    E(xpos, top)
    xpos += gap
    
    N(xpos, top)
    xpos += gap
