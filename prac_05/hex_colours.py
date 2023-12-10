"""
Based on the state name example program above, create a program that allows you to look up hexadecimal colour
codes like those at http://www.color-hex.com/color-names.html

"""

# Define a dictionary that maps color names to corresponding hexadecimal color codes.
COLOR_TO_CODE = {
    "apricot": "#fbceb1",
    "amethyst": "#9966cc",
    "aqua": "#00ffff",
    "beaver": "#9f8170",
    "blueviolet": "#8a2be2",
    "byzantium": "#702963",
    "CadetBlue4": "#53868b",
    "crystal": "#a7d8de",
    "darkkhaki": "#bdb76b",
    "cream": "#fffdd0",
}


# Define a main function to handle user input and look up color codes.
def main():
    color_name = input("Enter color name (blank to quit): ").lower()
    while color_name != "":
        if color_name in COLOR_TO_CODE:
            print(f"{color_name.capitalize()} is {COLOR_TO_CODE[color_name]}")
        else:
            print("Invalid color name")

        # Prompt the user again for another color name or to quit.
        color_name = input("Enter color name (blank to quit): ").lower()


main()


