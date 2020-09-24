# # DO NOT EDIT - Starting with a simple lists of colors and numbers
# colors = ["blue", "Green", "PURPLE", "blue-green", "sky blue"]
# numbers = [2, 34, 8.5, -22.0, 33//4, 2**5]
# print('COLORS', colors)
# print('NUMBERS', numbers)

# # 1. Print the total number of colors (length of the list)
# print(len(colors))

# # 2. Print the first color
# print(colors[0])

# # 3. Print the second and third colors
# print(colors[1:3])

# # 4. Print the last two colors
# print(colors[-2:])

# # 5. Print the smallest number in the numbers list
# print(sorted(numbers)[0])

# # 6. Print the largest number in the numbers list
# print(sorted(numbers, reverse=True)[0])

# # 7. Sort the numbers

# numbers = sorted(numbers)
# # UNCOMMENT WHEN YOU WORK ON #7
# print ('SORTED NUMBERS', numbers)

# # 8. Sort the colors alphabetically ignoring case
# colors = sorted(colors, key=lambda x: x.lower())
# # UNCOMMENT WHEN YOU WORK ON #8
# print ('SORTED COLORS', colors)

# There are two ways to declare dictionaries
# Create a dictionary and assign it to the d1 variable using the dict()
# constructor that has key/value pairs
#   key: "module", value: "Python 3"
#   key: "subject", value: "Dictionaries"
# d1 =  dict(module="Python 3", subject="Dictionaries")
# print(d1)

# # Create a dictionary and assign it to the d2 variable using the dictionary
# # literal that has key/value pairs
# #   key: "module", value: "Python 3"
# #   key: "subject", value: "Dictionaries"
# d2 =  {
#     "module": "Python 3",
#     "subject": "Dictionaries"
# }


# # Unlike JavaScript, the keys in Python dictionaries can be any kind of
# # value, not just strings or Symbols. Add a key to d1 that is the number
# # one with the value "one". Then, add another key to d1 that is a string
# # that contains the character 1 and give it the value of "one". Then,
# # print the dictionary to see what's in there.

# d1[1] = "one"
# d1["1"] = "one"

# # Convert d1 to a list using the list() method. Then, print it. What gets
# # put into the list?
# d1_as_list =  list(d1)
# print(d1_as_list)


# # Now, check that the following keys are in d1
# #  "module"    should be True
# #  "subject"   should be True
# #  "age"       should be False
# #  1           should be True
# #  "1"         should be True
# #  "one"       should be False
# #  True        should be False

# # DO NOT EDIT
# odds = 1, 3, 5, 7, 9
# evens = 2, 4, 6, 8

# # Step 1: Print out the result of adding evens to odds
# print(evens + odds)

# # Step 2: Print out the result of multiplying odds by three
# print([x * 3 for x in odds])

# # Step 3A: Use print to find out if odds is less than evens
# print(odds < evens)

# # Step 3B: Print out your explanation of why 3A has that result
# print("Tuples are compared position by position")

# # Step 4: Print out the average of the numbers in evens using one line of code
# print(sum(evens) / len(evens))

# # Step 5A: Write a function 'minmaxmean' that accepts an iterable and
# #         returns the minimum value, the maximum value and the average (mean)

# def minmaxmean(iter):
#     mini = min(iter)
#     maxi = max(iter)
#     mean = sum(iter) / len(iter)
#     return("Min = {}, Max = {}, Mean = {}".format(mini, maxi, mean))

# # Step 5B: Use print to confirm you function is working on evens and odds

# print(minmaxmean(evens))
# print(minmaxmean(odds))

# # BONUS: Call your function with a new tuple of your own creation
# #        And print the results in a pretty way

# nums = 123,234,345,456,567
# print(minmaxmean(nums))

# print('THREE CASES FOR RANGE')
# print('A) End Value')

# # STEP 1: Change the zero in the range to 10
# #         Notice how "10" is not included in the output
# for i in range(10):
#     print(i)

# print('B) Start & End Values')

# # STEP 2: Code a `for` loop to print numbers 5 through 9
# for i in range(5, 10):
#     print(i)

# print('C) Only Even Values')

# # STEP 3: Print 0, 2, 4, 6 and 8 using a for loop
# #         Hint - range can take a 3rd parameter for the step distance

# for i in range(0, 9, 2):
#     print(i)

# # Powers of 2 from 1 to 16
# # Write a for loop that uses the range function to
# # print the powers of 2 from 2 - 65536, that is
# # from 2^1st - 2^16th powers
# for i in range(1, 17):
#     print(2 ** i)

# # Write your function, here.
# def get_first_value(l):
#     return l[0]

# print(get_first_value([1, 2, 3]))  # > 1
# print(get_first_value([80, 5, 100]))  # > 80
# print(get_first_value([-500, 0, 50]))  # > -500

# # Write your function, here.

# def get_sum_of_elements(l):
#     return sum(l)

# print(get_sum_of_elements([2, 7, 4]))  # > 13
# print(get_sum_of_elements([45, 3, 0]))  # > 48
# print(get_sum_of_elements([-2, 84, 23]))  # > 105

# Write your function, here.

# def get_indices(l, c):
#     arr = []
#     for x in range(0, len(l)):
#         if l[x] == c:
#             arr.append(x)
#     return arr


# print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
# # Prints [0, 1, 3, 5]

# print(get_indices([1, 5, 5, 2, 7], 7))
# # Prints [4]

# print(get_indices([1, 5, 5, 2, 7], 5))
# # Prints [1, 2]

# print(get_indices([1, 5, 5, 2, 7], 8))
# # Prints []

# Your code, here.

# def can_nest(list1, list2):
#     if min(list1) > min(list2) and max(list1) < max(list2):
#         return True
#     return False

# print(can_nest([1, 2, 3, 4], [0, 6]))  # > True
# print(can_nest([3, 1], [4, 0]))  # > True
# print(can_nest([9, 9, 8], [8, 9]))  # > False
# print(can_nest([1, 2, 3, 4], [2, 3]))  # > False

# GUEST_LIST = {
#     "Kurt": "Germany",
#     "Julia": "France",
#     "Ito": "Japan",
#     "Katherine": "England",
#     "Sam": "Argentina"
# }


# # # Write your function, here.
# def greeting(key):
#     if key in GUEST_LIST:
#         return "Hi! I'm {} from {}".format(key, GUEST_LIST[key])
#     else:
#         return "Hi! I'm a guest."

# print(greeting("Kurt"))  # > "Hi! I'm Kurt from Germany."
# print(greeting("Sam"))  # > "Hi! I'm Sam from Argentina."
# print(greeting("Monty"))  # > "Hi! I'm a guest."

# Write your function, here.

# def has_key(d, k):
#     if k in d:
#         return True
#     return False

# print(has_key({"a": 44, "b": 45, "c": 46}, "d"))
# # False

# print(has_key({"craves": True, "midnight": True, "snack": True}, "morning"))
# # False

# print(has_key({"pot": 1, "tot": 2, "not": 3}, "not"))
# # True

# # Write your function, here.
# def find_smallest_num(l):
#     return min(l)

# print(find_smallest_num([34, 15, 88, 2]))  # > 2
# print(find_smallest_num([34, -345, -1, 100]))  # > -345
# print(find_smallest_num([-76, 1.345, 1, 0]))  # > -76
# print(find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]))  # > -0.9999
# print(find_smallest_num([7, 7, 7]))  # > 7

# # Write your function, here.

# def is_empty(d):
#     a = True if len(d) == 0 else False
#     return a

# print(is_empty({}))  # > True
# print(is_empty({"a": 1}))  # > False

# # Write your function, here.
# def difference(l):
#     return max(l) - min(l)

# print(difference([10, 15, 20, 2, 10, 6]))
# # 20 - 2 = 18

# print(difference([-3, 4, -9, -1, -2, 15]))
# # 15 - (-9) = 24

# print(difference([4, 17, 12, 2, 10, 2]))

# Write your function, here.

# def first_last(l):
#     return [l[0], l[-1]]

# print(first_last([5, 10, 15, 20, 25]))  # > [5, 25]
# print(first_last([13, None, False, True]))  # > [13, True]
# print(first_last([None, 4, "6", "hello", None]))  # > [None, None]

# Write your function, here.
def find_digit_amount(i):
    return len(str(abs(i)))
print(find_digit_amount(123))  # > 3
print(find_digit_amount(-56))  # > 2
print(find_digit_amount(7154))  # > 4
print(find_digit_amount(61217311514))  # > 11
print(find_digit_amount(0))  # > 1
