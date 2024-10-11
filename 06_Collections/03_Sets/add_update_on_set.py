#!/usr/bin/python3

"""
Performing add and update operations on sets 
"""

sample_set = set()  # {}
given_str = "Python"

# add function will add only single value or multiple values in tuples
sample_set.add(given_str)

print(f"{sample_set = }")

# update function will add only iterable objects

sample_set.update("Tomato")
print(f"{sample_set = }")