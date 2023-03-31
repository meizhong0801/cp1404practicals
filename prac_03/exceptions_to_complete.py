"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        break

    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)

# test
# Enter a valid integer: 7
# Valid result is: 7
# Enter a valid integer: 0.9
# Please enter a valid integer.
# Enter a valid integer: 0
# Valid result is: 0
