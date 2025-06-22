# reduce() Exercise
#
# Given a list of booleans, use reduce() and a lambda to determine if
# at least one of the values in the list is True.
# Test it with all 3 lists.

from functools import reduce

flags1 = [True, False, True, True]
flags2 = [False, False]
flags3 = []

def at_least_one_true(acc, current):
    return acc or current
# Using reduce to check if at least one value is True
result1 = reduce(at_least_one_true, flags1)
result2 = reduce(at_least_one_true, flags2)
result3 = reduce(at_least_one_true, flags3, False)  # Providing False
print(f"Flags1 has at least one True: {result1}")
print(f"Flags2 has at least one True: {result2}")
print(f"Flags3 has at least one True: {result3}")