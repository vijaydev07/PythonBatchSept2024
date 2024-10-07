#!/usr/bin/python3

"""
Purpose: Print the full diamond format
"""
# for upper half
for num in range(1, 9): 

    print( ( 8 - num ) * ' ' + ( 2 * num - 1 ) * '*')
    
# for lower half
for num in range(7,0,-1):

    print( ( 8 - num ) * ' ' + ( 2 * num - 1 ) * '*')