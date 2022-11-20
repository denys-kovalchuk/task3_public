from collections import namedtuple
# Task one:

# full_name = input('Please type your full name: ')
# counter = 0
# for char in full_name:
#     if char.isdigit():
#         print('Error, name contains digits')
#         counter += 1
#         break
# if counter < 1:
#     print(f'All good, name "{full_name.title()}" has no digits')


# Task two:

# a, b = int(input('Enter the first number in range: ')), int(input('Enter the second number in range: '))
# if len(range(a, b + 1)) >= 5:
#     print(range(a, b + 1)[1] + range(a, b + 1)[-2] + sum(range(a, b + 1)) / len(range(a, b + 1)))
# else:
#     print('Error, range should have at least 5 numbers')


# Task three:

# r, g, b = int(input('Enter the intensity of red color (0 - 255): ')), \
#           int(input('Enter the intensity of green color (0 - 255): ')), \
#           int(input('Enter the intensity of blue color (0 - 255): '))
# print((r, g, b))


# Task four:

Marks = namedtuple('Student', 'Name Algebra Geometry History Computer_Science Geography')
pupil_1 = Marks('John', 90, 100, 80, 85, 90)
pupil_2 = Marks('Bob', 80, 90, 100, 75, 95)
print(pupil_1)
print(pupil_2)

# Task five:

# my_tuple = ()
# while True:
#     user_input = input('Press "q" to stop. Type a number: ')
#     if user_input == 'q':
#         break
#     my_tuple += float(user_input),
# print(sorted(my_tuple))


# Task six:

# review = input('Please enter your review: ')
# print(len(review))
# if len(review) > 60 and 'menu' in review and 'gym' in review and 'service' in review:
#     print('Congratulations, you have been granted a 15% discount for your next visit')
