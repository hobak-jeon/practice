"""Module providing basic examples for programming in python."""

import collections

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
    print(m, n, o, p)


positional_arguments(1, 2, 3, 4, 5)
keyword_only_arguments(1, 2, o=3)  # 1 2 3 10
keyword_only_arguments(3, 4, o=5, p=11)  # 3 4 5 11
list.sort(key=len, reverse=False)  # list.sort(*, key=None, reverse=False)
