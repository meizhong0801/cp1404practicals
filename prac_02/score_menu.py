"""
The menu should have four separate options:

(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
When the user quits, say some kind of "farewell".

"""

import random

EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
MIN_SCORE = 0
MAX_SCORE = 100

# Define the menu with four options
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    # Print the menu and get the user's choice
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score_category(score)
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()

    # Say farewell when the user quits
    print("Farewell!")


# get a valid user score input
def get_valid_score():
    score = int(input("Please enter your score (0-100 inclusive): "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Your score is invalid!")
        score = int(input("Please enter your score (0-100 inclusive): "))
    return score


# determines the score category based on the input score
def determine_score_category(score):
    if score >= EXCELLENT_THRESHOLD:
        return "Your score is excellent!"
    elif score >= PASS_THRESHOLD:
        return "Your score is pass!"
    else:
        return "Your score is bad!!"


# print stars based on the input score
def print_stars(score):
    print('*' * score)


main()
