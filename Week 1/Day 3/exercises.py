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
