import math
import numpy as np


# Task one:

name = input('Please enter your name: ')
if name.capitalize() == 'Denys':
    print('We have the same name')


# Task two:

x = float(input('Please enter x: '))
if -math.pi <= x <= math.pi:
    print(math.cos(3 * x))
else:
    print('Please use x in range from -pi to pi')


# Task three:

a, b, c = int(input('Please type the first number: ')), int(input('Please type the second number: ')), \
          int(input('Please type the third number: '))
discriminant = b ** 2 - 4 * a * c
if discriminant < 0:
    print('The function has no real roots')
elif discriminant == 0:
    print(f'x equals {-b / (2 * a)}')
else:
    print(f'x_1 = {(-b + discriminant ** 0.5) / (2 * a)}, x_2 = {(-b - discriminant ** 0.5) / (2 * a)}')


# Task four:

menu = input('Please select math operation:\n1. addition\n2. subtraction\n3. multiplication\n4. division\n'
             '5. power\n6. square root\n7. cube root\n8. sine of the number\n9. cosine of the number\n'
             '10. tangents on the number\n11. exit\nType number: ')
match menu:
    case '1':
        a, b = float(input("Please type the first number to add: ")), \
               float(input("Please type the second number to add: "))
        print(f'The sum of {a} and {b} is {a + b}')
    case '2':
        a, b = float(input("Please type the first number to subtract: ")), \
               float(input("Please type the second number to subtract: "))
        print(f'The difference of {a} and {b} is {a - b}')
    case '3':
        a, b = float(input("Please type the first number to multiply: ")), \
               float(input("Please type the second number to multiply: "))
        print(f'The product of multiplication of {a} and {b} is {a * b}')
    case '4':
        a, b = float(input("Please type the first number (dividend): ")), \
               float(input("Please type the second number (divisor): "))
        print(f'The quotient of division of {a} and {b} is {a / b}')
    case '5':
        a, b = float(input("Please type the first number (base): ")), \
               float(input("Please type the second number (exponent): "))
        print(f'The result of exponentiation of base {a} and power {b} is {a ** b}')
    case '6':
        a = float(input("Please type the number to get square root: "))
        print(f'The square root of {a} is {a ** 0.5}')
    case '7':
        a = float(input("Please type the number to get cube root: "))
        print(f'The cube root of {a} is {np.cbrt(a)}')
    case '8':
        a = float(input("Please type the number to get sine: "))
        print(f'The sine of {a} is {math.sin(a)}')
    case '9':
        a = float(input("Please type the number to get cosine: "))
        print(f'The cosine of {a} is {math.cos(a)}')
    case '10':
        a = float(input("Please type the number to get tangents: "))
        print(f'The tangents of {a} is {math.tan(a)}')
    case '11':
        print('Bye!')
    case _:
        print('Wrong input, use numbers 1-11')

# Task five:

x = int(input('Please enter a number: '))
print(f'{x} is an even number') if x % 2 == 0 else print(f'{x} is an odd number')


# Task six:

day = input('Type a day of the week: ')
working_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
weekends = ['saturday', 'sunday']
if day in working_days:
    print(f'{day.capitalize()} is a work day')
elif day in weekends:
    print(f'{day.capitalize()} is weekend')
else:
    print('Invalid input, type day of the week')
