"""
CP1404/CP5632 - Practical
Answer the following questions:

"""

# 1. When will a ValueError occur?
# "ValueError" will occur if the inputs provided for the numerator or denominator are not valid integers.

# 2. When will a ZeroDivisionError occur?
# "ZeroDivisionError" will occur if the user enters a denominator value of zero.

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes, by checking if the denominator is 0 before performing the division.


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

