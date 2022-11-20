# Task one:

a, b = int(input('Type the first number in range: ')), int(input('Type the second number in range: '))
total = 0
for number in range(a, b + 1):
    total += number
print(f'The total sum of numbers between {a} and {b} is {total}')


# Task two:

a = int(input('Type a number to get its factorial: '))
factorial = 1
for number in range(1, a + 1):
    factorial *= number
print(f"The factorial of {a} is {factorial}")


# Task three:

for i in range(1):
    for j in range(12):
        print("*" * j, end='')
        print()


# Task four:

a, b = int(input('Type the first number in range: ')), int(input('Type the second number in range: '))
average = sum(range(a, b + 1)) / len(range(a, b + 1))
conditional_total = 0
for number in range(a, b + 1):
    if number % average == 0:
        conditional_total += number
print(f'The total sum of numbers between {a} and {b} that can be divided by an average is {conditional_total}')


# Task five:

a, b = int(input('Type the width: ')), int(input('Type the height: '))
for i in range(1):
    print("*" * a, end='')
    print()
    for j in range(b-2):
        print("*" + ' ' * (a - 2) + '*', end='')
        print()
    print("*" * a, end='')
    print()


# Task six:

attempt = 1
while attempt < 4:
    login, password = input('Enter your login: '), input('Enter your password: ')
    if login == 'login' and password == 'password':
        print(f'Авторизацію успішно пройдено з «{attempt}» спроби')
        break
    print(f'Invalid login/password {3-attempt} attempts left')
    attempt += 1
else:
    print('System locked for 3 min')
