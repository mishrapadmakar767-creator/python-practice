# Python Exception Handling

# 1. Basic Try-Except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# 2. Handling ValueError
try:
    number = int("hello")
except ValueError:
    print("Error: Invalid number.")

# 3. Try-Except-Else
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division error.")
else:
    print("Result:", result)

# 4. Finally Block
try:
    print("Executing try block.")
except Exception:
    print("An error occurred.")
finally:
    print("Finally block executed.")

# 5. Multiple Exceptions
try:
    numbers = [10, 20, 30]
    print(numbers[5])
except IndexError:
    print("Error: Index out of range.")
except Exception as error:
    print("Unexpected error:", error)

# 6. Raise an Exception
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    return "Eligible"

try:
    print(check_age(20))
except ValueError as error:
    print(error)
