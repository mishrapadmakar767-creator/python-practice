# Python Lists

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original List:", fruits)
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])
print("First Two Fruits:", fruits[:2])

# Add Items
fruits.append("Grapes")
print("After Append:", fruits)

fruits.insert(1, "Pineapple")
print("After Insert:", fruits)

# Remove Items
fruits.remove("Banana")
print("After Remove:", fruits)

removed_fruit = fruits.pop()
print("Popped Fruit:", removed_fruit)
print("After Pop:", fruits)

# Other List Operations
print("Number of Fruits:", len(fruits))
print("Mango Exists:", "Mango" in fruits)

fruits.sort()
print("Sorted List:", fruits)
