# Python Dictionaries

student = {
    "name": "Padmakar",
    "age": 20,
    "course": "B.Com",
    "marks": 85
}

print("Student Details:", student)
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])

# Access Values Safely
print("City:", student.get("city", "Not Available"))

# Add and Update Values
student["city"] = "Prayagraj"
student["marks"] = 90
print("Updated Dictionary:", student)

# Dictionary Methods
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# Remove an Item
student.pop("age")
print("After Removing Age:", student)

# Loop Through Dictionary
for key, value in student.items():
    print(key, ":", value)
