
# Python List Comprehension

# 1. Create a List of Squares
numbers = [1, 2, 3, 4, 5]

squares = [n ** 2 for n in numbers]
print("Squares:", squares)


# 2. Get Even Numbers
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even Numbers:", even_numbers)


# 3. Get Odd Numbers
odd_numbers = [n for n in numbers if n % 2 != 0]
print("Odd Numbers:", odd_numbers)


# 4. Convert Names to Uppercase
names = ["rahul", "amit", "padmakar"]

uppercase_names = [name.upper() for name in names]
print("Uppercase Names:", uppercase_names)


# 5. Apply an If-Else Condition
results = ["Pass" if marks >= 40 else "Fail"
           for marks in [85, 32, 67, 25]]

print("Results:", results)


# 6. Filter Numbers Greater Than 10
values = [5, 12, 8, 20, 15, 3]

greater_than_10 = [n for n in values if n > 10]
print("Greater Than 10:", greater_than_10)
