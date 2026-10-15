def say_hello(choice):
    if choice == 1:
        print("Hello, KMUTNB")
    elif choice == 2:
        print("Sawasdee, KMUTNB")
    elif choice == 3:
        print("Buenas, KMUTNB")
    else:
        print("Error: There is no choice", choice,"please try again")
        say_hello(float(input("Choose a choice between 1-3 : ")))


say_hello(float(input("Choose a choice between 1-3 : ")))
