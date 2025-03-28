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


# Arguments usage.
def positional_arguments(i, j, *args):
    """0. Function providing an example for positional arguments (*args)."""
    print(i, j)  # 1 2
    print(args)  # (3, 4, 5)


def keyword_arguments(q, r, **kwargs):
    """1. Function providing an example for keyword arguments (**kwargs)."""
    print(q, r)
    print(kwargs)


def keyword_only_arguments(m, n, *, o, p=10):
    """2. Function providing an example for keyword-only arguments (*)."""
    # Arguments must be passed as keyword arguments after "*".
    print(m, n, o, p)


positional_arguments(1, 2, 3, 4, 5)  # Deliver a tuple (*args = (3, 4, 5)) to function.

keyword_arguments(
    7, 8, x=100, y=200
)  # Deliver a dictionary ({'x': 100, 'y': 200}) to function.

keyword_only_arguments(1, 2, o=3)  # 1 2 3 10
keyword_only_arguments(3, 4, o=5, p=11)  # 3 4 5 11
# list.sort(*, key=None, reverse=False)


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
