"""
The menu should have four separate options:

(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
Handle each of these (except quit) separately, and consider how you can reuse your functions.
In main(), before the menu loop, get the valid score.
When the user quits, say some kind of "farewell".

"""

import random

EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
MIN_SCORE = 0
MAX_SCORE = 100
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
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

    print("Farewell!")


def get_valid_score():
    score = int(input("Please enter your score (0-100 inclusive): "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Your score is invalid!")
        score = int(input("Please enter your score (0-100 inclusive): "))
    return score


def determine_score_category(score):
    if score >= EXCELLENT_THRESHOLD:
        return "Your score is excellent!"
    elif score >= PASS_THRESHOLD:
        return "Your score is pass!"
    else:
        return "Your score is bad!!"


def print_stars(score):
    print('*' * score)


main()


# Test

# -1, 0, 20, 50, 60, 90, 92, 100, 101

# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> g
# Please enter your score (0-100 inclusive): -1
# Your score is invalid!
# Please enter your score (0-100 inclusive): 0
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> p
# Your score is bad!!
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> s
#
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> g
# Please enter your score (0-100 inclusive): 20
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> p
# Your score is bad!!
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> s
# ********************
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> g
# Please enter your score (0-100 inclusive): 40
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> g
# Please enter your score (0-100 inclusive): 50
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> p
# Your score is pass!
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> s
# **************************************************
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> g
# Please enter your score (0-100 inclusive): 60
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> p
# Your score is pass!
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> s
# ************************************************************
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> g
# Please enter your score (0-100 inclusive): 90
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> p
# Your score is excellent!
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> s
# ******************************************************************************************
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> g
# Please enter your score (0-100 inclusive): 100
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> p
# Your score is excellent!
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> s
# ****************************************************************************************************
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> g
# Please enter your score (0-100 inclusive): 101
# Your score is invalid!
# Please enter your score (0-100 inclusive): 100
# (G)et a valid score
# (P)rint result
# (S)how stars
# (Q)uit
# >>> q
# Farewell!
