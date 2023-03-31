"""
CP1404/CP5632 - Practical
Answer the following questions:

1. When will a ValueError occur?
"ValueError" will occur if the user inputs a non-integer value or a string for the numerator or denominator.

2. When will a ZeroDivisionError occur?
"ZeroDivisionError" will occur if the user enters a denominator value of zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, below are updated program.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Invalid input, denominator can not be zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

except ZeroDivisionError:
    print("Cannot divide by zero!")


print("Finished.")

# test
# Enter the numerator: a
# Numerator and denominator must be valid numbers!
# Finished.
# Enter the numerator: 0
# Enter the denominator: 0
# ZeroDivisionError: Cannot divide by zero!
# Cannot divide by zero!
# Enter the numerator: 55
# Enter the denominator: 7
# 7.857142857142857
# Finished.