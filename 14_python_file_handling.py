# Python File Handling

# 1. Write to a file
with open("sample.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("Learning File Handling.\n")

print("File written successfully.")

# 2. Read the file
with open("sample.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)

# 3. Append new content
with open("sample.txt", "a") as file:
    file.write("This is new content.\n")

print("Content appended successfully.")

# 4. Read all lines
with open("sample.txt", "r") as file:
    lines = file.readlines()

print("Total Lines:", len(lines))

# 5. Write multiple lines
with open("marks.txt", "w") as file:
    file.writelines([
        "Maths: 85\n",
        "English: 90\n",
        "Accounts: 88\n"
    ])

print("Marks file created successfully.")
