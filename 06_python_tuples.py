# Python Tuples

fruits = ("Apple", "Banana", "Mango", "Orange")

print("Original Tuple:", fruits)
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])
print("First Two Fruits:", fruits[:2])
print("Total Fruits:", len(fruits))
print("Mango Exists:", "Mango" in fruits)

# Tuple Methods
print("Count of Apple:", fruits.count("Apple"))
print("Index of Mango:", fruits.index("Mango"))

# Convert Tuple into List
fruit_list = list(fruits)
fruit_list.append("Grapes")
print("Updated List:", fruit_list)

# Convert List back into Tuple
updated_tuple = tuple(fruit_list)
print("Updated Tuple:", updated_tuple)
