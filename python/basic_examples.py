"""Module providing basic examples for programming in python."""

import collections
import copy

STR_ALPHABET = "abcdef"
lst_chars = ["u", "a", "e", "c", "k", "i"]
dic_grades = collections.defaultdict(int)
dic_grades["A"] = 90
dic_grades["B"] = 80
dic_grades["C"] = 1


# For loops
for ch in STR_ALPHABET:
    print(ch)

for idx, val in enumerate(lst_chars):
    print(idx, val)

for key, val in dic_grades.items():
    print(key, val)

for countdown in 5, 4, 3, 2, 1, "Yeah!":
    print(countdown)

for x in [0, 1, 2]:
    pass

for _ in range(10):
    print("Hi!")

for x in range(6):
    print(x)

    if x == 7:
        break
else:
    print("Finally finished!")

_, b = range(2)
print(b)  # 1


# Mutable and immutable
numbers: list[int] = [1, 2, 3]
numbers_lst_1: list[list[int]] = [[1], [2], [3]]
numbers_lst_2: list[list[int]] = [[1, 2], [2, 3], [3, 4]]
numbers_lst_3: list[list[int]] = [[4], [5], [6]]

for item in numbers:
    # 'item' is a number literal: item = 1, item = 2, item = 3
    item *= 2
# numbers = [1, 2, 3]

for item in numbers_lst_1:
    # 'item' is a list: item = [1], item = [2], item = [3]
    item[0] *= 2
# numbers_lst_1 = [[2], [4], [6]]

for item in numbers_lst_2:
    # 'item' is a list: item = [1, 2], item = [2, 3], item = [3, 4]
    for element in item:
        # 'element' is a number literal: element = 1, ... , element = 4
        element *= 2
# numbers_lst_2 = [[1, 2], [2, 3], [3, 4]]

for item in numbers_lst_3:
    # 'item' is a list: item = [4], item = [5], item = [6]
    item *= 2
# number_lst_2 = [[4, 4], [5, 5], [6, 6]]


# Differences between 'is' and  '=='.
# The 'is' operator in Python is used to check if two variables point to the same object.
# Unlike the '==' operator, which checks if the values of two objects are equal.
# The 'is' operator goes one step further to ensure that they are, in fact, the exact same object.

# Return a shallow copy of the list.
org_lst = [1, 2, 3]
lst_by_shallow_copy = org_lst.copy()
lst_by_deep_copy = copy.deepcopy(org_lst)

if org_lst is lst_by_shallow_copy:
    # 'is' compares id(org_lst) with id(lst_by_shallow_copy).
    print("same id.")
else:
    print("different id.")

if org_lst == lst_by_shallow_copy:
    # '==' compares value of 'org_lst' with value of 'lst_by_shallow_copy'.
    print("same value.")
else:
    print("different value.")


if org_lst is lst_by_deep_copy:
    # 'is' compares id(org_lst) with id(lst_by_deep_copy).
    print("same id.")
else:
    print("different id.")

if org_lst == lst_by_deep_copy:
    # '==' compares value of 'org_lst' with value of 'lst_by_deep_copy'.
    print("same value.")
else:
    print("different value.")
