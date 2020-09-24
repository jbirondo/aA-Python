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

# # Write your function, here.

# def remainder(el1, el2):
#     return(el1 % el2)

# print(remainder(1, 3))  # > 1
# print(remainder(3, 4))  # > 3
# print(remainder(5, 5))  # > 0
# print(remainder(7, 2))  # > 1

# ---

# # Write your function, here.

# def string_int(str):
#     return(int(str))

# print(string_int("6"))  # > 6
# print(string_int("1000"))  # > 1000
# print(string_int("12"))  # > 12

# ---

# # Write your function, here.

# def calculate_exponent(el1, el2):
#     return(el1 ** el2)

# print(calculate_exponent(5, 5))  # > 3125
# print(calculate_exponent(10, 10))  # > 10000000000
# print(calculate_exponent(3, 3))  # > 27

# ---

# # Write your function, here.

# def long_burp(num):
#     return("Bu" + "r" * num + "p")

# print(long_burp(3))  # > "Burrrp"
# print(long_burp(5))  # > "Burrrrrp"
# print(long_burp(9))  # > "Burrrrrrrrrp"

# ---

# # Write your function, here.

# def cap_space(str):
#     res = ""
#     for letter in str:
#         if letter.isupper():
#             res += " {}".format(letter.lower())
#         else:
#             res += letter
#     return res

# print(cap_space("helloWorld"))  # > "hello world"
# print(cap_space("iLoveMyTeapot"))  # > "i love my teapot"
# print(cap_space("stayIndoors"))  # > "stay indoors"

# ---

# Write your function, here.

# def concat_name(first, last):
#     return("{}, {}".format(last, first))

# print(concat_name("First", "Last"))  # > "Last, First"
# print(concat_name("John", "Doe"))  # > "Doe, John"
# print(concat_name("Mary", "Jane"))  # > "Jane, Mary"

# ---

# # Write your function, here.

# def char_count(el1, el2):
#     return(el2.count(el1))

# print(char_count("a", "App Academy"))  # > 1
# print(char_count("c", "Chamber of Secrets"))  # > 1
# print(char_count("b", "big fat bubble"))  # > 4

# ---

# # Write your function, here.

# def factorial(num):
#     res = 1
#     for el in range(2, num + 1):
#         res *= el
#     return res

# print(factorial(1))  # > 1
# print(factorial(8))  # > 40320
# print(factorial(12))  # > 479001600

# ---

# # Write your function, here.

# def divisible_by_five(num):
#     return True if num % 5 == 0 else False

# print(divisible_by_five(5))  # > True
# print(divisible_by_five(-55))  # > True
# print(divisible_by_five(37))  # > False

# # ---

# # Write your function, here.

# def is_last_character_n(str):
#     return str[-1] == "n"

# print(is_last_character_n("Aiden"))  # > True
# print(is_last_character_n("Piet"))  # > False
# print(is_last_character_n("Bert"))  # > False
# print(is_last_character_n("Dean"))  # > True

# ---

# # Write your function, here.

# def compare(el1, el2):
#     return len(el1) == len(el2)

# print(compare("AB", "CD"))  # > True
# print(compare("ABC", "DE"))  # > False
# print(compare("hello", "App Academy"))  # > False


# ---
# Write your function, here.

# def is_valid_hex_code(str):
#     if str[0] != "#":
#         return False
#     if len(str) != 7:
#         return False
#     for letter in str[1:]:
#         if letter.upper() not in "ABCDEF1234567890":
#             return False
#     return True

# print(is_valid_hex_code("#CD5C5C"))  # > True
# print(is_valid_hex_code("#EAECEE"))  # > True
# print(is_valid_hex_code("#eaecee"))  # > True

# print(is_valid_hex_code("#CD5C58C"))
# # Prints False
# # Length exceeds 6

# print(is_valid_hex_code("#CD5C5Z"))
# # Prints False
# # Not all alphabetic characters in A-F

# print(is_valid_hex_code("#CD5C&C"))
# # Prints false
# # Contains unacceptable character

# print(is_valid_hex_code("CD5C5C"))
# # Prints False
# # Missing #

# ---

# # Write your function, here.
# def first_before_second(str, el1, el2):
#     return(len(str) - str[::-1].find(el1) < str.find(el2))

# print(first_before_second("a rabbit jumps joyfully", "a", "j"))
# #> True
# # Every instance of "a" occurs before every instance of "j".

# print(first_before_second("knaves knew about waterfalls", "k", "w"))
# #> True

# print(first_before_second("happy birthday", "a", "y"))
# #> False
# # The "a" in "birthday" occurs after the "y" in "happy".

# print(first_before_second("precarious kangaroos", "k", "a"))

# ---
# Write your function, here.
# There are hints after the print statements

def seq_of_numbers(string):
    start = 0
    end = 1
    l = []
    res= ""
    while end <= len(string):
        if all_same(string[start:end]):
            end += 1
        else:
            l.append(string[start:end - 1])
            start = end - 1
    l.append(string[start:end])

    for ele in l:
        res += str(ele.count(ele[0])) + ele[0]

    return res

def all_same(str):
    for i in range(1, len(str)):
        if str[i] != str[0]:
            return False
    return True



# print(seq_of_numbers("1211"))
# This is "one 1, one 2, two 1s"
# Prints "111221"

# print(seq_of_numbers("111221"))
# # This is "three 1s, two 2s, and one 1"
# # Prints "312211"

print(seq_of_numbers("31131211131221"))
# # This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
# #    one 3, one 1, two 2s, and one 1"
# # Prints "13211311123113112211"


###########################################################
# AN ALGORITHM
# An algorithm for performing this without a data structure
# means you have to think about what you're trying to look
# for.
#
# If you scan the string two characters at a time, when they
# change, you know that you have started a new sequence of
# numbers. You can add the current number of characters that
# you've scanned to a result.
#
# For example, say you had "111221". You would start the
# count at 1 and compare the characters at indices 0 and 1.
# Since they are the same, you would increment the current
# count to two, because you will have found two 1s. Then,
# you would compare the characters at indices 1 and 2.
# Again, they are both 1s, so you would increment the count
# to 3. The next comparison, the one at indices 2 and 3
# yields the characters "1" and "2". At this point, the
# characters have changed. The current count is 3, and the
# current character is "1", so you would concatenate those
# onto a result "31". Then, you would set the current count
# back to 1 (because you have found one 2), and continue
# with the same process.


############################################################
# PSEUDOCODE
#
# Concatenate an empty space to the end of the value passed
#    into the function. This will let you compare the entire
#    length of the original string with a guarantee that the
#    two last characters do not match.
# Create an empty string to which you will append the
#    counts and digits
# Initialize an index to 0 for looping over the string
# Initialize a counter variable to record the count of the
#    current character
# Using the index variable, loop from 0 to the length of the
#    string minus 1 (because you don't want to examine the
#    last character, the space that you added)
#   If the current character is not equal to the next
#      character, then concatenate the current count and the
#      current character to the result string and set the
#      current count back to 1
#   Otherwise, just increment the current character count by
#      1
#   Increment the index by 1
# Return the result

