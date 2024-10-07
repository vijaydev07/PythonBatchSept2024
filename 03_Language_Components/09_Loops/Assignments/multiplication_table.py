#!/usr/bin/python3

"""
Purpose: It's to print the multiplication table from rev order

"""

# WAP to display the multiplication table from 10 to 1, for the first 10 tables
MAX_TABLE = 10

first = 0
while first < MAX_TABLE:
    first += 1
    # print(f'{first = }')


    second = 10
    while second > 0:
        print(f"{first:2} * {second:2} = {first * second:3}")
        second -= 1

    # print('----------')
    print('-' * 12)

print()
print()


# Assignment - Display the multiplication table horizontally

for i in range(1, 11):  
    row = []  # Initializing a list row

    for j in range(1, 11):  
        product = j * i  
        # Appending the formatted output to the row list using zfill
        row.append(f"{str(j).zfill(2)} * {str(i).zfill(2)} = {str(product).zfill(3)}")

    
    print(" | ".join(row))