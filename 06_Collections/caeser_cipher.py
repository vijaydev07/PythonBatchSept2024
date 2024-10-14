#!/usr/bin/python3

"""
Purpose: produce a caeser cipher text with given shift value for the given text message
"""

result = []
text = "Attack is planned to happen on next sunday"
print("Original text : ", text)
text = text.lower()
modified_text = ""
shift_val = 3

for each_char in text:

    if each_char.isalpha(): # to check character is a letter
        shifted_char = chr((ord(each_char) - ord('a') + shift_val) % 26 + ord('a'))
        result.append(shifted_char)
    
    else:
        result.append(each_char) # non-alphabet chars remain unchanged

modified_text = ''.join(result)

print("Modified Caesar cipher text: ", modified_text)

