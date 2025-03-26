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
print(b)
