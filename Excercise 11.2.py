
"""
Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar.
Electric cars have the capacity of the battery in kilowatt-hours as their property.
Gasoline cars have the volume of the tank in liters as their property. Write initializers for the subclasses.
For example, the initializer of electric cars receives the registration number, maximum speed and battery capacity as its parameter.
It calls the initializer of the base class to set the first two properties and then sets its capacity.
Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l).
Select speeds for both cars, make them drive for three hours and print out the values of their kilometer counters.
"""

class Car:

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = maximum_speed
        self.travelled_distance = 0

    def accelerator(self, speed_change):

        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def distance(self, hours_number):
        new_distance = self.current_speed * hours_number
        self.travelled_distance += new_distance

    def print_information(self):

        print(f"This car has registration number: {self.registration_number}")

class Electric_Car(Car):
    def __init__(self, registration_number, maximum_speed, battery):
        self.battery = battery
        super().__init__(registration_number, maximum_speed)


    def print_information(self):
        super().print_information()
        print(f"has battery capacity {self.battery} kWh")


class Gasoline_Car(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        self.tank_volume = tank_volume
        super().__init__(registration_number, maximum_speed)


    def print_information(self):
        super().print_information()
        print(f"has tank volume {self.tank_volume}l")


cars = []
cars.append(Electric_Car("ABC-15", 180, 52.5))
cars.append(Gasoline_Car("ABC-15", 165, 32.3))

for car in cars:
    car.print_information()
    car.accelerator(50)
    car.distance(3)
    print(f"has travelled {car.travelled_distance} km")


