
# Python map(), filter() and reduce()

from functools import reduce

# 1. map() - Square of Every Number
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda n: n ** 2, numbers))
print("Squares:", squares)


# 2. map() - Convert Numbers to Strings
number_strings = list(map(str, numbers))
print("Number Strings:", number_strings)


# 3. filter() - Select Even Numbers
values = [10, 15, 20, 25, 30, 35]

even_numbers = list(filter(lambda n: n % 2 == 0, values))
print("Even Numbers:", even_numbers)


# 4. filter() - Marks Greater Than 60
marks = [45, 78, 90, 32, 65, 55]

passed_marks = list(filter(lambda m: m >= 60, marks))
print("Marks 60 or Above:", passed_marks)


# 5. reduce() - Sum of All Numbers
total = reduce(lambda a, b: a + b, numbers)
print("Total:", total)


# 6. reduce() - Product of All Numbers
product = reduce(lambda a, b: a * b, numbers)
print("Product:", product)


# 7. Find Maximum Value Using reduce()
maximum = reduce(lambda a, b: a if a > b else b, values)
print("Maximum:", maximum)
