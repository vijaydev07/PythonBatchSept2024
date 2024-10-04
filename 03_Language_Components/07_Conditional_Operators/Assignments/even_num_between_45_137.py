#!usr/bin/python

"""
Purpose: Display all the even numbers between 45 to 137

"""

even_nums = []

for val in range(45,137):
    if (val % 2 == 0):
        print(f"{val} is even number")
        even_nums.append(val)

print(f"{even_nums}")