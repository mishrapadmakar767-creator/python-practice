# Python break, continue and pass

# 1. Break Statement
print("Break Example:")

for number in range(1, 6):
    if number == 4:
        break
    print(number)

# 2. Continue Statement
print("Continue Example:")

for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# 3. Pass Statement
print("Pass Example:")

for number in range(1, 4):
    if number == 2:
        pass
    print(number)

# 4. Find the First Multiple of 7
for number in range(1, 30):
    if number % 7 == 0:
        print("First multiple of 7:", number)
        break
