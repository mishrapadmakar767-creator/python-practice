
# Python *args and **kwargs

# 1. Using *args
def add_numbers(*args):
    print("Numbers:", args)
    print("Total:", sum(args))


add_numbers(10, 20)
add_numbers(10, 20, 30, 40)


# 2. Using *args to Find Maximum
def find_maximum(*numbers):
    if numbers:
        print("Maximum:", max(numbers))
    else:
        print("No numbers provided")


find_maximum(12, 45, 23, 67, 34)


# 3. Using **kwargs
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


show_details(name="Padmakar", course="B.Com", city="Prayagraj")


# 4. Using Both *args and **kwargs
def student_info(*args, **kwargs):
    print("Subjects:", args)
    print("Details:", kwargs)


student_info("Python", "SQL", name="Padmakar", marks=85)


# 5. Normal Function with *args
def calculate_average(*marks):
    if marks:
        average = sum(marks) / len(marks)
        print("Average Marks:", average)
    else:
        print("No marks provided")


calculate_average(80, 90, 70, 60)
