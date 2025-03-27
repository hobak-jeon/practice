"""Module providing list examples for Python programming."""

from functools import reduce

integers = [1, 2, 5, 4, 7, 3]
chars = ["u", "a", "e", "c", "k", "i"]
estern_langs = ["Korean", "Japanese", "Chinese"]
western_langs = ("English", "German", "Spanish")
langs = estern_langs + list(western_langs)

# Make new lists.
new_integers_1 = integers[::]
new_integers_2 = integers[::]
new_integers_3 = integers[::]
new_integers_4 = integers[::]
new_integers_5 = integers[::]
new_integers_6 = integers[::]

# Concatenate lists.
duplicates = chars * 3 + integers + chars + estern_langs + list(western_langs)

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

# Make the list empty in place.
new_integers_4[:] = []

# Clear item(s) in place.
new_integers_5 *= 0


# The differences between "+=" and "+".
# Operator "+=" works in place for mutable objects like "list", "dict", "set".
integers += [4]

# Operator "+" creates a new list.
integers = integers + [5]

# Work in place and returns "None".
integers.append(6)

# Remove and return item at index (default last) in place.
integers.pop()


# Sort items of list in place.
langs.sort()
langs.sort(key=len, reverse=False)
