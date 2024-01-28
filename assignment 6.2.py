#Q3: Nuances of Employing Multiple Inheritance in Python
# a. Method Resolution Order (MRO)
class Base:
    def method(self):
        print("Base method")

class Mixin1(Base):
    def method(self):
        print("Mixin1 method")
        super().method()

class Mixin2(Base):
    def method(self):
        print("Mixin2 method")
        super().method()

class MyClass(Mixin1, Mixin2):
    pass

# Example usage:
obj = MyClass()
obj.method()  # Output follows MRO: Mixin1 method -> Mixin2 method -> Base method

# b. Super() Function
class Parent:
    def __init__(self):
        self.value = 42

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value *= 2

# Example usage:
obj = Child()
print(obj.value)  # Output: 84

# c. Composition Over Inheritance
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

# Example usage:
my_car = Car()
my_car.engine.start()  # Composition over inheritance
