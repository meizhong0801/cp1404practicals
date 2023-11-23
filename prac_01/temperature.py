"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


# Define the menu with conversion options
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)


# Get the user's choice
choice = input(">>> ").upper()

# Continue looping until the user chooses to quit ("Q")
while choice != "Q":
    if choice == "C":   # Conversion from Celsius to Fahrenheit
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":  # Conversion from Fahrenheit to Celsius
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")

    print(MENU)   # Display the menu again and get the user's choice
    choice = input(">>> ").upper()
print("Thank you.")


"""

test

C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
>>> f
Fahrenheit: 66
Result: 18.89 C
C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
>>> c
Celsius: 55
Result: 131.00 F
C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
>>> q
Thank you.

"""