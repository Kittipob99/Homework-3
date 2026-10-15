#Written in Python IDLE 3.14.6
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def show(self):
        print("Product name :", self.name)
        print("Price :", self.price, "$")
        print("Quantity :", self.quantity)

products = []

with open("products.txt", "r") as file:
    for line in file:
        info = line.strip().split(",")

        name = info[0]
        price = float(info[1])
        quantity = int(info[2])

        product = Product(name, price, quantity)
        products.append(product)

def show_most_valuable(products):
    most_valuable = products[0]

    for product in products:
        if product.price*product.quantity > most_valuable.price*most_valuable.quantity:
            most_valuable = product
            value = product.price*product.quantity
            
    most_valuable.show()
    print("Total value :", round((value),2), "$")
    
show_most_valuable(products)
