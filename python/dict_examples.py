"""Module providing dict examples for Python programming."""

from collections import defaultdict

coordinate_xy: dict[str, int] = dict(x=10, y=11)
alphanumeric_code: dict[
    str, int | None
] = {}  # Support type hint with default value "None" from Python 3.10.
alphanumeric_code["A"] = 65
alphanumeric_code["B"] = 66
alphanumeric_code.setdefault("C")  # {'A': 65, 'B': 66, 'C': None}
alphanumeric_code.setdefault("D", 68)  # {'A': 65, 'B': 66, 'C': None, 'D': 68}
alphanumeric_code.pop("C")  # {'A': 65, 'B': 66, 'D': 68}
alphanumeric_code.setdefault("C", 67)  # {'A': 65, 'B': 66, 'D': 68, 'C': 67}
alphanumeric_code["Z"] = 91  # {'A': 65, 'B': 66, 'D': 68, 'C': 67, 'Z': 91}
key, value = alphanumeric_code.popitem()  # Z 91

grades: defaultdict[str, int] = defaultdict(
    int
)  # Support defaultdict (type hint) from Python 3.9.
grades["A"] = 90
grades["B"] = 80
grades["C"] = 70

for key, val in grades.items():  # grades.items() returns a list of items.
    print(key, val)

pairs: defaultdict[str, list[int]] = defaultdict(list)
pairs["A"] = [1, 2, 3]
pairs["B"] = [2, 4, 6]
pairs["C"] = [3, 6, 9]

pairs["D"].append([4, 8, 12])
# append() is a method of a list.
# pairs["D"]  -> Make an empty list as value with key "D".
# [].append([4, 8, 12]) -> append an object[4, 8, 12] to the end of the list.

if "A+" in grades:
    print("I got A+.")  # The key is in the dict.

# sorted(dict) returns a new list with the items sorted by the value of the items int dict.
reversed_grades = dict(sorted(grades.items(), reverse=True))
