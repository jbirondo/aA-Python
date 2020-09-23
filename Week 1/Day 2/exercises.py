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

def is_same_num(el1, el2):
    return el1 == el2

print(is_same_num(4, 8))  # >  False
print(is_same_num(2, 2))  # >  True
print(is_same_num(2, "2"))  # >  False
