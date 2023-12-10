"""
Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that many
lines of output. Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS.
"""


from random import randint
quick_pick_number = int(input("How many quick picks? "))

for _ in range(quick_pick_number):
    numbers = []
    while len(numbers) < 6:
        number = randint(1, 45)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    print(" ".join([str(num) for num in numbers]))




