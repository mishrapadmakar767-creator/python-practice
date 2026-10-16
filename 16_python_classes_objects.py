# Python Classes and Objects

# 1. Create a Class
class Student:
    def __init__(self, name, course, marks):
        self.name = name
        self.course = course
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)

    def check_result(self):
        if self.marks >= 40:
            return "Pass"
        return "Fail"


# 2. Create Objects
student1 = Student("Padmakar", "B.Com", 85)
student2 = Student("Rahul", "B.Com", 35)

# Display Student Details
student1.display()
print("Result:", student1.check_result())

print()

student2.display()
print("Result:", student2.check_result())


# 3. Class with a Method
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calc = Calculator()

print("Sum:", calc.add(10, 20))
print("Product:", calc.multiply(5, 4))
