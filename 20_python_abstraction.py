
# Python Abstraction

from abc import ABC, abstractmethod


# Abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Child Class 1
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Child Class 2
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# Create Objects
rectangle = Rectangle(10, 5)
square = Square(4)

print("Rectangle Area:", rectangle.area())
print("Square Area:", square.area())
