
# Python CSV File Handling

import csv

# 1. Create Student Data
students = [
    ["Name", "Age", "Marks"],
    ["Amit", 20, 75],
    ["Rahul", 21, 90],
    ["Neha", 19, 85],
    ["Priya", 20, 92]
]

# 2. Write Data to CSV File
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully")


# 3. Read CSV File
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    print("Student Records:")
    for row in reader:
        print(row)


# 4. Read Only Student Names
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Student Names:")
    for row in reader:
        print(row["Name"])


# 5. Calculate Average Marks
marks = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        marks.append(int(row["Marks"]))

average = sum(marks) / len(marks)
print("Average Marks:", average)


# 6. Find Students Scoring 80 or Above
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Students with Marks >= 80:")
    for row in reader:
        if int(row["Marks"]) >= 80:
            print(row["Name"], "-", row["Marks"])
