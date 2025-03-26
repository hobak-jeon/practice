"""Module providing string examples for programming in python."""

FRUITS_1 = "apple#banana#cherry#orange"
FRUITS_2 = "apple banana cherry orange"
NAME = "hayden"
WEATHER = "A fine day"
NUMBERS = "123456789012345"

# String object is immutable.
# NAME[0] = 'H' wrong! using str.replace() instead of assignment.
NEW_NAME = NAME.replace("h", "H")

# str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found.
INDEX_1 = NUMBERS.find("1")  # returns 0.
INDEX_2 = NUMBERS.find("11")  # returns -1.
INDEX_3 = NUMBERS.rfind("5")  # returns 14

# str.index(sub[, start[, end]])
# Like find(), but raise ValueError when the substring is not found.
INDEX_4 = NUMBERS.index("6")  # returns 5.
# INDEX_5 = NUMBERS.index("11")  # ValueError: substring not found

# Split a string into lists.
# Setting the maxsplit parameter to 3, will return a list with 4 string elements.
lst_fruit_1 = FRUITS_1.split("#", 2)  # ['apple', 'banana', 'cherry#orange']
lst_fruit_2 = FRUITS_2.split()  # ['apple', 'banana', 'cherry', 'orange']
# The default means split according to any white space, and discard empty strings from the result.

# Convert a string to a list.
lst_name = list(NAME)  # ['h', 'a', 'y', 'd', 'e', 'n']

# Reverse string
REVERSED_NUMBERS_1 = NUMBERS[-1::-1]
REVERSED_NUMBERS_2 = NUMBERS[::-1]
