class Vehicle:
    def move(self):
        print("A vehicle can move.")


class Car(Vehicle):
    def drive(self):
        print("The car is being driven.")


class ElectricCar(Car):
    def charge(self):
        print("The electric car is charging.")


my_car = ElectricCar()
my_car.move()
my_car.drive()
my_car.charge()
