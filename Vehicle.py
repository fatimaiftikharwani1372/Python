class Vehicle:
    def __init__(self, vehicle_name, rent):
        self.vehicle_name = vehicle_name
        self.rent = rent

    def display_vehicle(self):
        print("Vehicle Name:", self.vehicle_name)
        print("Rent per day:", self.rent)


class Car(Vehicle):
    def __init__(self, vehicle_name, rent, seats):
        super().__init__(vehicle_name, rent)
        self.seats = seats

    def display_vehicle(self):
        super().display_vehicle()
        print("Number of Seats:", self.seats)


class Bike(Vehicle):
    def __init__(self, vehicle_name, rent, engine_capacity):
        super().__init__(vehicle_name, rent)
        self.engine_capacity = engine_capacity

    def display_vehicle(self):
        super().display_vehicle()
        print("Rent:", self.rent)
        print("Engine Capacity:", self.engine_capacity)


print("FATIMA WANI")
obj1 = Car("Honda City", 2000, 2)
obj2 = Car("Sedan", 1000, 5)
obj3 = Bike("Yamaha", 40, 150)
obj4 = Bike("Suzuki", 35, 125)

obj1.display_vehicle()
obj2.display_vehicle()
obj3.display_vehicle()
obj4.display_vehicle()