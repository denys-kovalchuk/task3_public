# Task one:

my_list = [1, 4, -10, 25, 0.1, 0, 214]

print(f'Max value in my_list {my_list} is {max(my_list)}')
print(f'Min value in my_list {my_list} is {min(my_list)}')
print(f'Sum of elements in my_list {my_list} is {sum(my_list)}')
print(f'Average of elements in my_list {my_list} is {round(sum(my_list) / len(my_list), 2)}')


# Task two:

my_list_1 = list(map(int, input('Type numbers for the first list: ').split()))
my_list_2 = list(map(int, input('Type numbers for the second list: ').split()))
my_list_3 = [number for number in my_list_1 if number not in my_list_2]
my_list_3.extend([number for number in my_list_2 if number not in my_list_1])
my_list_3 = list(set(my_list_3))
print(my_list_3)
print(my_list_3[::-1])
print(sorted(my_list_3))
print(sorted(my_list_3, reverse=True))


# Task three:


a, b = int(input('Type the first number in range: ')), int(input('Type the last number in range: '))
numbers = [number for number in range(a, b + 1)]
prime_numbers = []
for number in numbers:
    counter = 0
    for i in range(1, number):
        if number % i == 0:
            counter += 1
    if counter == 1:
        prime_numbers.append(number)
print(prime_numbers)
choice = input('Press "1" to count the sum of prime numbers, press "2" to return their product: ')
if choice == '1':
    print(f'The sum of prime numbers is {sum(prime_numbers)}')
elif choice == '2':
    product = 1
    for number in prime_numbers:
        product *= number
    print(f'The product of prime numbers is {product}')
else:
    print('Wrong input, try "1" or "2"')


# Task four:

my_list = [1, 4, -10, 25, 0.1, 0, 214]
choice = input(f'Press "1" to print {my_list} in reverse order. Press "2" to print it in ascending order: ')
if choice == '1':
    print(f'Reverse order is {my_list[::-1]}')
elif choice == '2':
    print(f'Ascending order is {sorted(my_list)}')
else:
    print("Wrong input, try '1' or '2'")

# Task five:

int_list = [number for number in range(1, 100)]
new_list = [number for number in int_list if number % 2 == 0]
repeat = int(input('Enter the number to repeat the new_list: '))
new_list *= repeat
print(new_list)
int_list.clear()


# Task six:

user_number = int(input('Type a number to find it in the list: '))
if user_number in new_list:
    print(f'Number {user_number} occurs {repeat} times in the list. '
          f'Indexes are: {[index for index, value in enumerate(new_list) if value == user_number]}')
else:
    print(f'Number {user_number} is not in the list')
