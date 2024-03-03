# Correct each program

# Program 1
def greet(name):
    print("Hello, " + name + "!")

name = input('What is your name?: ')
greet(name)

# Program 2
x = 5
y = 10
result = x + y
print("Result:", result)

# Program 3
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area
radius = float(input('Enter a radius for me to calculate the area of!: '))
print(calculate_area(radius))

# Program 4
number = float(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Program 5
def add_numbers(a, b):
    return a + b
a = float(input('Enter a first number !!!!!!: '))
b = float(input('Enter a second number !!!!!!: '))
print(add_numbers(a, b))

# Program 6
def print_message(message):
    print(message)

message = str(input('Say something!: '))
print_message(message)

# Program 7
numbers = [1, 2, 3, 4, 5]
average = sum(numbers) / len(numbers)
print("Average:", average)

# Program 8
for i in range(5):
    print(i)

# Program 9
def multiply(a, b):
    result = a * b
    return result

a = float(input('Enter a first number !!!!!!: '))
b = float(input('Enter a second number !!!!!!: '))
print(multiply(a, b))

# Program 10
def check_temperature(temp):
    if temp > 30:
        print("It's hot outside.")
    else:
        print("It's cool outside.")

temp = float(input('What is the temperature outside?: '))
check_temperature(temp)