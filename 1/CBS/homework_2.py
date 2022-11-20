import math


# Task one:

first, second = input('Please type the first word: '), input('Please type the second word: ')
print(f'{first}, {second}')


# Task two:

a, b, x = int(input('Please type the first number: ')), int(input('Please type the second number: ')), \
          int(input('Please type the third number: '))
print(a * b * x)


# Task three:

a, b, c = int(input('Please type the first number: ')), int(input('Please type the second number: ')), \
          int(input('Please type the third number: '))
x_1 = (-b+(b**2 - 4 * a * c)**0.5) / (2 * a)  # можливо в умові помилка і має бути "-" замість "+"
x_2 = (-b-(b**2 - 4 * a * c)**0.5) / (2 * a)  # можливо в умові помилка і має бути "-" замість "+"
print(f'x1 = {x_1}, x2 = {x_2}')


# Task four:

x = input('Please type 10 symbols: ')
ascii_sum = 0
for symbol in x:
    ascii_sum += ord(symbol)
print(ascii_sum)


# Task five:

text = input('Type text to reverse it: ')
print(text[::-1])


# Task six:

radius = int(input('Please enter the radius: '))
print(round(math.pi * radius ** 2, 2))


# Task seven:

length = 700
velocity = 90
time = length/velocity
print(time)


# Task eight:

name = input('Type your name: ')
age = input('Type your age: ')
print("My name is " + name.capitalize() + ' and my age is ' + age)
