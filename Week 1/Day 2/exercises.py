# print("** Doubling Penny **")

# # How many times would a penny need to double to generate a million dollars?
# count = 0
# total = 0

# # STEP 2: Write the while loop
# while total < 100000000:
#     if total == 0:
#         total = 1
#     else:
#         total *= 2
#     count += 1


# print('Double', count, 'times')

# # How much money has been generated at that point?
# print('${:,}'.format(total))

# ---

# '''
# This is a simple script to practice creating a few functions in Python

# Please follow the steps outlined below.
# '''

# # STEP 1 - Write a function named `welcome` that prints a welcome message

# def welcome():
#     print("Hello there")

# # Step 2 - Write a function named `calc_sum` that
# #   - takes in two numbers and
# #   - returns their sum

# def calc_sum(el1, el2):
#     return el1 + el2


# # DO NOT EDIT - The guts of the program
# welcome()
# print(calc_sum(1, 2), 'is 3?', calc_sum(1, 2) == 3)
# print(calc_sum(-10, -2), 'is -12?', calc_sum(-10, -2) == -12)
# print(calc_sum(1.1, -2.2), 'is -1.1?', calc_sum(1.1, -2.2) == -1.1)
# print(calc_sum('a', 'b'), 'is ab?', calc_sum('a', 'b') == 'ab')
# print(calc_sum([1, 2], [3, 4]), 'is [1,2,3,4]?',
#       calc_sum([1, 2], [3, 4]) == [1, 2, 3, 4])

# ---

# # Define your function "addition" here

# def addition(el1, el2):
#     return el1 + el2

# print(addition(2, 3))   #> 5
# print(addition(-3, -6)) #> -9
# print(addition(7, 3))   #> 10

# ---

# Write your function, here.

# def is_same_num(el1, el2):
#     return el1 == el2

# print(is_same_num(4, 8))  # >  False
# print(is_same_num(2, 2))  # >  True
# print(is_same_num(2, "2"))  # >  False

# ---

# Your function here

# def min2sec(num):
#     return num * 60


# print(min2sec(5))  # > 300
# print(min2sec(3))  # > 180
# print(min2sec(2))  # > 120

# ---

# # Write your function, here.
# # Parameters are in this order: chickens, cows, pigs

# def how_many_legs(chickens, cows, pigs):
#     return(chickens * 2 + cows * 4 + pigs * 4)

# print(how_many_legs(2, 3, 5))  # > 36
# print(how_many_legs(1, 2, 3))  # > 22
# print(how_many_legs(5, 2, 8))  # > 50

# ---
# # Create your function, here.

# def increment(num):
#     return num + 1

# print(increment(0))  # > 1
# print(increment(9))  # > 10
# print(increment(-3))  # > -2

# ---

# Write your function, here.

def remainder(el1, el2):
    return(el1 % el2)

print(remainder(1, 3))  # > 1
print(remainder(3, 4))  # > 3
print(remainder(5, 5))  # > 0
print(remainder(7, 2))  # > 1
