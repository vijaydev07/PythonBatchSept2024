#!/usr/bin/python

"""
Purpose: Performing for loop & enumerate function on range object

"""

for i in range(7): #iterating the range function using for loop
    print(i, end="") # 0123456
print()

# using enumerate function on range object to get the index

for i in enumerate(range(5)):
    # print(i) # It prints the tuple values
    print(f"At position {i[0]} the value is {i[1]}")
print()

# using 2 loop variables in for loop

for loop_index, val in enumerate(range(4)):
    print(f"At position {loop_index}, the value is: {val}")