"""
CP1404/CP5632 - Practical
Answer the following questions:

1. When will a ValueError occur?
"ValueError" will occur if the user inputs a non-integer value for the numerator or denominator.

2. When will a ZeroDivisionError occur?
"ZeroDivisionError" will occur if the user enters a denominator value of zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, below are updated program.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("ZeroDivisionError: Cannot divide by zero!")

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

except ZeroDivisionError:
    print("Cannot divide by zero!")


print("Finished.")