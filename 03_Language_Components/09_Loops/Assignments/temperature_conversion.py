#!/usr/bin/python

"""
    '10c' ->> celcis -> farhent
    '10' ->> celus -> farhent
    '10 f' ->> farhent -> celius
        
        
        user input : 23c
        output     : xF
        
        user input : 23F
        output     : xC
        
        23c, 23C, 23F, 23f
        23C, 23F
        23 C
        23C
"""

user_input = input("Enter celsius or Fahrenheit value:").lower()

input_size = len(user_input)
last_char = user_input[input_size-1]

modified_input = user_input.rstrip('cf')

if(last_char == "c"):
    f_heat = (1.8 * float(modified_input)) + 32
    print(f"user input : {user_input}\noutput     : {f_heat:.1f}F")

elif(last_char == "f"):
    f_heat = (float(modified_input) - 32) *(5/9)
    print(f"user input : {user_input}\noutput     : {f_heat:.1f}C")

else:
    print("Enter valid celsius or fahrenheit format value, ends with c or f")
