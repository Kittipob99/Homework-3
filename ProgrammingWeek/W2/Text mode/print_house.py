
def print_roof():
    print("  ^  ")
    print(" ^ ^ ")
    print("^   ^")

def print_ceiling():
    print("|||||")

def print_wall():
    print("|   |")
    print("|   |")

def print_floor():
    print("|||||")

def print_house(h):
    if h < 0:
        h = 0
        
    print_roof()

    for i in range(h):
        print_ceiling()
        print_wall()
        
    print_floor()
   
print_house(int(input("How many floor of the house? : ")))


