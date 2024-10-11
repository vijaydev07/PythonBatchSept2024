#!/usr/bin/python3

"""
Applying logical and relational operational operations on sets
"""


set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_c = {1, 2}
set_d = {6, 7}

# Logical operations
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)

# Relational operations
print("\nIs set_c a subset of set_a?", set_c <= set_a)
print("Is set_a a superset of set_c?", set_a >= set_c)
print("Are set_a and set_d disjoint?", set_a.isdisjoint(set_d))