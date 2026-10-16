# Python Sets

numbers = {10, 20, 30, 40, 50}

print("Original Set:", numbers)
print("Number of Elements:", len(numbers))
print("20 Exists:", 20 in numbers)

# Add Elements
numbers.add(60)
print("After Add:", numbers)

numbers.update([70, 80])
print("After Update:", numbers)

# Remove Elements
numbers.remove(30)
print("After Remove:", numbers)

numbers.discard(100)
print("After Discard:", numbers)

# Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)
