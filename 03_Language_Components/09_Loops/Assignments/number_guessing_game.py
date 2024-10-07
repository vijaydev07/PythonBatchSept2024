#!/usr/bin/python3

"""
Purpose: Number guessing game

"""

LUCKY_NUMBER = 67
attempt = 0

while True:
    attempt += 1
    print(f"\n {attempt = }: ",end="")
    
    given_number = int(input('Enter a number between 0 & 100: '))
        
    # Check if the number is within the valid range
    if given_number < 0 or given_number > 100:
        print("Please enter a number within the range of 0 to 100.")
        attempt -= 1

    if given_number == LUCKY_NUMBER:
        print('You guessed correctly!')
        break
    elif given_number > LUCKY_NUMBER:
        print('Reduce your guessing number.')
    else:
        print('Increase your guessing number.')
    

# validate the attempts to give the score
if 1 <= attempt <= 3:
    points = 100
elif 4 <= attempt <= 9:
    points = 60
elif 10 <= attempt <= 16:
    points = 20
elif 17 <= attempt <= 25:
    points = 5
else:
    points = 0

print(f"\n Your score: {points} points")
