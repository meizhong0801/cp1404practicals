"""
get score
while score is out of 0 to 100
    print invalid score!
    get score again
if score >= 90
    print your score is excellent
elif score >=50
    print your score is pass
else
    print your score is bad
"""

import random

EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
MIN_SCORE = 0
MAX_SCORE = 100


def main():
    # Get a valid user score input
    score = int(input("Please enter your score(0~100):  "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Your score is invalid!")
        score = int(input("Please enter your score(0~100):  "))

    # determine score category and print the result
    result = determine_score_category(score)
    print(result)

    # generate a random score and determine its category
    random_score = random.randint(MIN_SCORE, MAX_SCORE)
    print(f"Random score: {random_score}")
    random_result = determine_score_category(random_score)
    print(random_result)


def determine_score_category(score):
    if score >= EXCELLENT_THRESHOLD:
        return "Your score is excellent!"
    elif score >= PASS_THRESHOLD:
        return "Your score is pass!"
    else:
        return "Your score is bad!!"


main()


