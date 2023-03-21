"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")


# test

# C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit
# >>> c
# Celsius: 30
# Result: 86.00 F
# C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit
# >>> f
# Fahrenheit: 40
# Result: 4.44 C
# C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit
# >>> q
# Thank you.