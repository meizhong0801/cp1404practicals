"""
Ask the user for a number of scores
Generate that many random numbers (scores) between 0 and 100 inclusive
For each of those scores, write the "result" to a file called results.txt as below:
Example file output for 4 random scores:

66 is Passable
4 is Bad
92 is Excellent
51 is Passable
"""

import random

EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
MIN_SCORE = 0
MAX_SCORE = 100


def main():
    score_number = int(input("Please enter your number of scores:  "))
    while score_number <= 0:
        print("Your number of scores is invalid!")
        score_number = int(input("Please enter your number of scores:  "))
    f = open("results.txt", "a")
    for i in range(score_number):
        random_score = random.randint(MIN_SCORE, MAX_SCORE)
        result = determine_score_category(random_score)
        f.write(f"{random_score} is {result}\n")
        # print(f"{random_score} is {result}")
    f.close()


def determine_score_category(score):
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASS_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()


# Test
# Please enter your number of scores:  0
# Your number of scores is invalid!
# Please enter your number of scores:  -1
# Your number of scores is invalid!
# Please enter your number of scores:  4
# 66 is Passable
# 11 is Bad
# 95 is Excellent
# 54 is Passable