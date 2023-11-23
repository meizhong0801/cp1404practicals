"""
Use 2 functions for converting Celsius to Fahrenheit and vice versa.

"""


# Define a menu string to display the program's options.
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)  #Display the menu.
    choice = input(">>> ").upper()

    # Keep running the program until the user chooses to quit
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


#  converts Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


# converts Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


# Call the main function to start the program
main()


"""

Testing

C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
>>> c
Celsius: 33
Result: 91.40 F
C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
>>> f
Fahrenheit: 66
Result: 18.89 C
C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
>>> q
Thank you.

"""
