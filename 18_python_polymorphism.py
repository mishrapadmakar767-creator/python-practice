
# Python Polymorphism

# 1. Same Method, Different Classes

class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# 2. Polymorphism Using a Function

def make_sound(animal):
    animal.sound()


make_sound(dog)
make_sound(cat)


# 3. Polymorphism with Different Objects

class Calculator:
    def calculate(self, a, b):
        print("Sum:", a + b)


class Multiplier:
    def calculate(self, a, b):
        print("Product:", a * b)


obj1 = Calculator()
obj2 = Multiplier()

obj1.calculate(10, 5)
obj2.calculate(10, 5)
