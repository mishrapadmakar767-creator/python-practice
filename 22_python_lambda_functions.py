
# Python Lambda Functions

# 1. Lambda Function for Addition
add = lambda a, b: a + b
print("Addition:", add(10, 20))


# 2. Lambda Function for Square
square = lambda n: n ** 2
print("Square:", square(5))


# 3. Lambda Function for Even or Odd
check_number = lambda n: "Even" if n % 2 == 0 else "Odd"
print("Number 8:", check_number(8))
print("Number 7:", check_number(7))


# 4. Lambda with map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n ** 2, numbers))
print("Squares:", squares)


# 5. Lambda with filter()
values = [10, 15, 20, 25, 30]
even_numbers = list(filter(lambda n: n % 2 == 0, values))
print("Even Numbers:", even_numbers)


# 6. Lambda with sorted()
students = [
    ("Rahul", 75),
    ("Amit", 90),
    ("Padmakar", 85)
]

sorted_students = sorted(students, key=lambda student: student[1])
print("Sorted by Marks:", sorted_students)


# 7. Lambda for Discount Calculation
price = 1000
discount_price = lambda p: p - (p * 10 / 100)
print("Price After 10% Discount:", discount_price(price))
