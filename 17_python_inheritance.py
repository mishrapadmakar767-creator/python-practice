
# Python Inheritance

# 1. Parent Class
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


# 2. Child Class
class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def show_course(self):
        print("Course:", self.course)


# 3. Create Object
student = Student("Padmakar", "B.Com")

student.introduce()
student.show_course()


# 4. Method Overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


animal = Animal()
dog = Dog()

animal.sound()
dog.sound()
