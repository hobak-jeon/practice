"""Module providing list examples for Python programming."""

import copy

integers = [1, 2, 5, 4, 7, 3]
chars = ["u", "a", "e", "c", "k", "i"]
eastern_langs = ["Korean", "Japanese", "Chinese"]
western_langs = ("English", "German", "Spanish")
langs = eastern_langs + list(western_langs)
new_integers_1 = integers[::]
new_integers_2 = integers[::]
new_integers_3 = integers[::]
new_integers_4 = integers[::]
new_integers_5 = integers[::]
new_integers_6 = integers[::]


# Concatenate lists.
duplicates = chars * 3 + integers + chars + eastern_langs + list(western_langs)

# Append object to the end of the list.
integers.append(1)  # [1, 2, 5, 4, 7, 3, 1]

# Insert object before index.
integers.insert(1, 2)  # [1, 2, 2, 5, 4, 7, 3, 1]


# Remove and return item at index (default last).
last_integer = integers.pop()
integer_at_1 = integers.pop(1)

# Remove first occurrence of value and return "None".
integers.remove(1)

# Remove all items from list.
# Clear item(s) in place.
new_integers_1.clear()

# Delete items(s) in place.
del new_integers_2[:]

# Assign a new empty list to a variable.
new_integers_3 = []

# Make a list empty in place.
new_integers_4[:] = []

# Clear item(s) in place.
new_integers_5 *= 0


# Reverse a list.
integers.reverse()  # Reverse a list in place.
reversed_integers = list(
    reversed(integers)
)  # reversed() returns a new reversed iterator.


# list.index(item[, start[, end]])
# Return first index of value from list.
# Raises a ValueError if there is no such item.
# A function such as str.find() is not supported in list.
print(f"integers = {integers}")
if 3 not in integers:  # [3, 7, 4, 5, 2]
    print("3 is not in integers.")
else:
    print(f"3's index = {integers.index(3)}")

# integers.index("3", 1) # ValueError: '3' is not in integers[1:].

# The differences between "+=" and "+".
# Operator "+=" works in place for mutable objects like "list", "dict", "set".
integers += [4]

# Operator "+" creates a new list.
integers = integers + [5]


# Sort items of list in place.
langs.sort()
langs.sort(key=len, reverse=False)

# Return a new sorted list from the items in iterable.
sorted_eastern_langs = sorted(eastern_langs)
sorted_western_langs = sorted(western_langs, key=len, reverse=True)
print(sorted("This is a test string from Andrew".lower().split(), key=len))


# Shallow and deep copy operations.
org_integers_for_shallow_copy = [[0], 1]
org_integers_for_deep_copy = [[4], 5]

# Shallow copy.
integers_by_shallow_copy_1 = org_integers_for_shallow_copy.copy()
integers_by_shallow_copy_2 = org_integers_for_shallow_copy.copy()

integers_by_shallow_copy_1[0][0] = (
    2  # integers_by_shallow_copy_1 = [[2], 1], org_integers_for_shallow_copy = [[2], 1]
)
integers_by_shallow_copy_2[1] = (
    3  # integers_by_shallow_copy_2 = [[2], 3], org_integers_for_shallow_copy = [[2], 1]
)

# Deep copy.
integers_by_deep_copy_1 = copy.deepcopy(org_integers_for_deep_copy)
integers_by_deep_copy_2 = copy.deepcopy(org_integers_for_deep_copy)

integers_by_deep_copy_1[0][0] = (
    6  # integers_by_deep_copy_1 = [[6], 5], org_integers_for_deep_copy = [[4], 5]
)
integers_by_deep_copy_2[1] = (
    7  # integers_by_deep_copy_2 = [[4], 7], org_integers_for_deep_copy = [[4], 5]
)
