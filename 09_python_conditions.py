# Python If-Else Conditions

age = 20

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# If-Elif-Else
marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Marks:", marks)
print("Grade:", grade)

# Even or Odd
number = 12

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Check Positive, Negative or Zero
number = -5

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")
