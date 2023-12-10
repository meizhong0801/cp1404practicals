"""
CP1404/CP5632 - Practical
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Set is_finished to True if a valid integer is entered
    except ValueError:  # Catch a ValueError if the input is not a valid integer
        print("Please enter a valid integer.")
print("Valid result is:", result)

