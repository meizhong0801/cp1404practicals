"""
Use 2 functions (NOT one!) for converting Celsius to Fahrenheit and vice versa.
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()

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
# Fahrenheit: 50
# Result: 10.00 C
# C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit
# >>> g
# Invalid option
# C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit
# >>> q
# Thank you.
