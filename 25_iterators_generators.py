
# Python Iterators and Generators

# 1. Using an Iterator
numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print("First:", next(iterator))
print("Second:", next(iterator))
print("Third:", next(iterator))
print("Fourth:", next(iterator))


# 2. Loop Through an Iterator
fruits = ["Apple", "Banana", "Mango"]

fruit_iterator = iter(fruits)

for fruit in fruit_iterator:
    print(fruit)


# 3. Create a Generator
def count_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


for number in count_numbers():
    print("Number:", number)


# 4. Generator for Squares
def square_generator(numbers):
    for number in numbers:
        yield number ** 2


values = [1, 2, 3, 4, 5]

for square in square_generator(values):
    print("Square:", square)


# 5. Generator for Even Numbers
def even_generator(limit):
    for number in range(1, limit + 1):
        if number % 2 == 0:
            yield number


print("Even Numbers:", list(even_generator(10)))
