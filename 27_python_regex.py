
# Python Regular Expressions (Regex)

import re

# 1. Search for a Word
text = "Python is easy to learn"

result = re.search("easy", text)
print("Word Found:", result.group() if result else "Not Found")


# 2. Find All Numbers
text = "My marks are 85, 90 and 78"

numbers = re.findall(r"\d+", text)
print("Numbers:", numbers)


# 3. Replace a Word
text = "I like Java"
new_text = re.sub("Java", "Python", text)
print("Updated Text:", new_text)


# 4. Check if Text Starts with Python
text = "Python is powerful"

result = re.match("Python", text)
print("Starts with Python:", bool(result))


# 5. Extract Email Addresses
text = "Contact us at abc@gmail.com or xyz@yahoo.com"

emails = re.findall(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    text
)
print("Emails:", emails)


# 6. Remove Extra Spaces
text = "Python    is   very    useful"

clean_text = re.sub(r"\s+", " ", text).strip()
print("Clean Text:", clean_text)


# 7. Find Words Starting with P
text = "Python Pandas NumPy Power BI"

words = re.findall(r"\bP\w*", text)
print("Words Starting with P:", words)
