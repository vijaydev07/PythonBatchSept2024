#!/usr/bin/python

"""

    celcius -> farhent
        farhenheit = (1.8 * celsius) + 32  # PEMDAS
    
    farhent -> celcius

"""

celsius_value = int(input("Enter celsius heat value: "))

fahrenheit_value = (1.8 * celsius_value) + 32

print(f"Fahrenheit temperature - {fahrenheit_value}, Celsius temperature - {celsius_value} ")