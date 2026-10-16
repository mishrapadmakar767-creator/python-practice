
# Python JSON Handling

import json

# 1. Python Dictionary to JSON String
student = {
    "name": "Padmakar",
    "course": "B.Com",
    "marks": 85,
    "passed": True
}

json_data = json.dumps(student)
print("JSON String:", json_data)


# 2. Pretty-Print JSON
pretty_json = json.dumps(student, indent=4)
print("Formatted JSON:")
print(pretty_json)


# 3. JSON String to Python Dictionary
json_text = '{"name": "Rahul", "marks": 90}'

data = json.loads(json_text)
print("Name:", data["name"])
print("Marks:", data["marks"])


# 4. Access JSON Data
students = """
[
    {"name": "Amit", "marks": 75},
    {"name": "Rahul", "marks": 90},
    {"name": "Neha", "marks": 85}
]
"""

student_list = json.loads(students)

for item in student_list:
    print(item["name"], "-", item["marks"])


# 5. Save JSON to a File
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file saved successfully")


# 6. Read JSON from a File
with open("student.json", "r") as file:
    loaded_data = json.load(file)

print("Loaded Student:", loaded_data["name"])
