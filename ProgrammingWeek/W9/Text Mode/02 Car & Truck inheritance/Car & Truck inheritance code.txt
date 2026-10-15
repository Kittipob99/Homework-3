#Written in Python IDLE 3.14.6
class Vehicle:
    def __init__(self, license_plate, brand, model, year, daily_rate):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        
    def show_info(self):
        print("License :", self.license_plate)
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Year :", self.year)
        print("Daily rate :", self.daily_rate, "$")

    def calculate_rental_cost(self, days):
        return self.daily_rate * days

class Car(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, seats):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.seats = seats

    def show_info(self):
        super().show_info()
        print("Seats :", self.seats)

    def calculate_rental_cost(self, days):
        if days == 5:
            return self.daily_rate * 5
        else:
            return self.daily_rate * days

class Truck(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, payload):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.payload = payload

    def show_info(self):
        super().show_info()
        print("Payload :", self.payload, "Tons")

# สร้าง Object
car = Car("กก-1234", "Toyota", "Yaris", 2023, 1000, 5)

truck = Truck("ขข-5678", "Isuzu", "D-Max", 2022, 2000, 1000)


# แสดงข้อมูล
print("===== CAR =====")
car.show_info()

print("Rental cost for 5 days :", car.calculate_rental_cost(5), "$")

print()

print("===== TRUCK =====")
truck.show_info()

print("Rental cost for 5 days :", truck.calculate_rental_cost(5), "$")
