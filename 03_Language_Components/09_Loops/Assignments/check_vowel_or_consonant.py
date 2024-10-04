#!src/bin/python

"""
Purpose: To check whether the given character
        is vowels or consonant

        vowels - aeiou

in operator  works with any iterable object
"""

letter = input("Enter a letter to know it is vowel or consonant: ").upper()

VOWELS = ["A","E","I","O","U"]

if letter in VOWELS:  # using if loop and list DS
    print(f"Given letter {letter} is Vowel")
else:
    print(f"Given letter {letter} is Consonant")
