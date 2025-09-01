# Assignment 1: Design Your Own Class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city
    def introduce(self):
        print(f"I am {self.name}, my power is {self.power}, and I protect {self.city}.")

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed
    def introduce(self):
        super().introduce()
        print(f"I can fly at {self.flight_speed} km/h!")

# Example usage
hero1 = Superhero("Shadow", "Invisibility", "Metro City")
hero2 = FlyingSuperhero("Skybolt", "Lightning", "Sky City", 800)
hero1.introduce()
hero2.introduce()

# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Example usage
vehicles = [Car(), Plane()]
for v in vehicles:
    v.move()
