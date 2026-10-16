# Python Loops

# For Loop
print("Numbers from 1 to 5:")
for number in range(1, 6):
    print(number)

# Loop Through a List
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print("Fruit:", fruit)

# While Loop
count = 1

while count <= 5:
    print("Count:", count)
    count += 1

# Sum of Numbers from 1 to 10
total = 0

for number in range(1, 11):
    total += number

print("Sum:", total)

# Multiplication Table
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
