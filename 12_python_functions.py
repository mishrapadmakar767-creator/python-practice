# Python Functions

# 1. Simple Function
def greet():
    print("Hello, Welcome to Python!")

greet()

# 2. Function with Parameters
def greet_user(name):
    print("Hello,", name)

greet_user("Padmakar")

# 3. Function with Return Value
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)

# 4. Default Parameter
def introduce(name, course="Python"):
    print(name, "is learning", course)

introduce("Padmakar")
introduce("Padmakar", "Data Analytics")

# 5. Even or Odd Function
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

print("12 is:", check_even_odd(12))
print("7 is:", check_even_odd(7))

# 6. Find Square
def square(number):
    return number ** 2

print("Square:", square(5))
