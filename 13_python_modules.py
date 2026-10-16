# Python Modules

# 1. Using the math module
import math

print("Square Root:", math.sqrt(64))
print("Power:", math.pow(2, 3))
print("Factorial:", math.factorial(5))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))

# 2. Using the random module
import random

numbers = [10, 20, 30, 40, 50]

print("Random Choice:", random.choice(numbers))
print("Random Number:", random.randint(1, 10))

# 3. Using the statistics module
import statistics

marks = [70, 80, 90, 85, 75]

print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))

# 4. Using aliases
import math as m

print("Square Root of 81:", m.sqrt(81))
