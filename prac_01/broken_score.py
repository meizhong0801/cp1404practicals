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


# get valid score input
while True:
    try:
        score = int(input("Enter score: "))
        if 0 <= score <= 100:
            break
        else:
            print("Invalid score. Score must be between 0 and 100 inclusive.")
    except ValueError:
        print("Invalid input. Please enter a valid integer score.")

# determine score category
if score >= 90:
    print("your score is excellent!")
elif score >= 50:
    print("your score is pass.")
else:
    print("your score is bad :(")


"""

test

Enter score: -1
Invalid score. Score must be between 0 and 100 inclusive.
Enter score: 101
Invalid score. Score must be between 0 and 100 inclusive.
Enter score: 50
your score is pass.
Enter score: 90
your score is excellent!
Enter score: 0
your score is bad :(

"""