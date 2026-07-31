from abc import ABC, abstractmethod


# 1. ABSTRACTION: An abstract blueprint that cannot be directly created
class Vehicle(ABC):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        # 2. ENCAPSULATION: __fuel is private; cannot be accessed directly outside the class
        self.__fuel = 100

    # An abstract method that MUST be implemented by child classes
    @abstractmethod
    def move(self):
        pass

    # Getter method to safely read private encapsulation data
    def check_fuel(self):
        return f"Fuel level: {self.__fuel}%"


# 3. INHERITANCE: Car inherits everything from Vehicle
class Car(Vehicle):
    def __init__(self, make: str, model: str, doors: int):
        super().__init__(make, model)  # Call parent constructor
        self.doors = doors

    # 4. POLYMORPHISM: Specifying how a Car moves
    def move(self):
        return f"The {self.make} {self.model} drives forward on 4 wheels."


# 3. INHERITANCE: Boat inherits everything from Vehicle
class Boat(Vehicle):
    # 4. POLYMORPHISM: Specifying how a Boat moves differently
    def move(self):
        return f"The {self.make} {self.model} cuts through the waves via propeller."


# --- Execution ---
if __name__ == "__main__":
    # Creating concrete objects from our child classes
    my_car = Car("Tesla", "Model 3", 4)
    my_boat = Boat("Yamaha", "212X")

    # Demonstrating Polymorphism
    # We treat them both as generic vehicles, but they act uniquely
    garage = [my_car, my_boat]

    for vehicle in garage:
        print(vehicle.move())
        print(vehicle.check_fuel())
        print("-" * 40)
